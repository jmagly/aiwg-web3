#!/usr/bin/env python3

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / ".aiwg/plugins/web3-distribution/payload/skills/nft-release-verify/scripts/release_ledger.py"
SPEC = importlib.util.spec_from_file_location("release_ledger", VALIDATOR)
assert SPEC and SPEC.loader
release_ledger = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(release_ledger)


def sha(label: str) -> str:
    return hashlib.sha256(label.encode()).hexdigest()


def observations(prefix: str) -> list[dict[str, str]]:
    return [
        {"operator": f"{prefix}-operator-a", "backend": f"{prefix}-backend-a", "observedAt": "2026-09-16T12:00:00Z", "result": "pass"},
        {"operator": f"{prefix}-operator-b", "backend": f"{prefix}-backend-b", "observedAt": "2026-09-16T12:01:00Z", "result": "pass"},
    ]


def gate(gate_id: str, status: str = "passed") -> dict[str, object]:
    return {
        "id": gate_id,
        "status": status,
        "evidence": [f"evidence/{gate_id}.json"] if status == "passed" else [],
        "actions": [] if status == "passed" else [f"complete {gate_id}"],
    }


def ready_ledger() -> dict[str, object]:
    return {
        "apiVersion": "aiwg.web3/nft-release-ledger/v1",
        "releaseId": "fixture-release",
        "candidateRevision": 1,
        "environment": "production",
        "generatedAt": "2026-09-16T12:02:00Z",
        "productionReady": True,
        "sources": [
            {"label": "allocation", "uri": "git+https://example.invalid/repo@abc#allocation.json", "sha256": sha("allocation"), "evidenceClass": "frozen-source"}
        ],
        "allocations": [
            {"identity": "token:1", "recipient": "0x0000000000000000000000000000000000000001", "quantity": 1},
            {"identity": "token:2", "recipient": "0x0000000000000000000000000000000000000002", "quantity": 1},
        ],
        "authorities": [
            {"action": "deploy", "target": "fixture-contract", "chainId": 31337, "actor": "fixture-signer", "costCeiling": "0.1 ETH", "authorizedBy": "fixture-session:deploy", "scope": "live"},
            {"action": "mint", "target": "fixture-contract", "chainId": 31337, "actor": "fixture-signer", "costCeiling": "0.1 ETH", "authorizedBy": "fixture-session:mint", "scope": "live"},
        ],
        "observations": {"chain": observations("chain"), "publication": observations("publication")},
        "gates": [gate(gate_id) for gate_id in release_ledger.GATE_IDS],
        "requiredActions": [],
    }


def expect_reject(label: str, ledger: dict[str, object], pattern: str) -> None:
    try:
        release_ledger.validate_ledger(ledger)
    except release_ledger.LedgerError as error:
        assert pattern in str(error), f"{label}: {error}"
        return
    raise AssertionError(f"{label}: unexpectedly passed")


def main() -> None:
    fixture = ready_ledger()
    assert release_ledger.validate_ledger(fixture) == {"passed": 8, "blocked": 0, "unverified": 0}

    duplicate = copy.deepcopy(fixture)
    duplicate["allocations"].append(copy.deepcopy(duplicate["allocations"][0]))
    expect_reject("duplicate allocation", duplicate, "duplicate allocation identity")

    interrupted = copy.deepcopy(fixture)
    interrupted["productionReady"] = False
    interrupted["gates"][5] = gate("mint-ownership-reconciliation", "blocked")
    interrupted["gates"][6] = gate("public-release-receipt", "unverified")
    interrupted["requiredActions"] = [
        "complete mint-ownership-reconciliation",
        "complete public-release-receipt",
    ]
    assert release_ledger.validate_ledger(interrupted) == {"passed": 6, "blocked": 1, "unverified": 1}

    false_ready = copy.deepcopy(interrupted)
    false_ready["productionReady"] = True
    expect_reject("reconciliation mismatch", false_ready, "productionReady must be false")

    same_backend = copy.deepcopy(fixture)
    same_backend["observations"]["publication"][1]["backend"] = same_backend["observations"]["publication"][0]["backend"]
    expect_reject("publication source independence", same_backend, "two independent backends")

    no_mint_authority = copy.deepcopy(fixture)
    no_mint_authority["authorities"] = [no_mint_authority["authorities"][0]]
    expect_reject("mint authority", no_mint_authority, "requires mint authority")

    with tempfile.TemporaryDirectory(prefix="aiwg-web3-nft-release-") as directory:
        path = Path(directory) / "ledger.json"
        path.write_text(json.dumps(interrupted, indent=2) + "\n", encoding="utf-8")
        first = release_ledger.validate_file(path)
        second = release_ledger.validate_file(path)
        assert first == second
        assert first["canonicalSha256"] == hashlib.sha256(release_ledger.canonical_bytes(interrupted)).hexdigest()

    independent_fixture = ROOT / "tests/fixtures/independent-nft-project/release-ledger.interrupted.json"
    first_fixture_result = release_ledger.validate_file(independent_fixture)
    second_fixture_result = release_ledger.validate_file(independent_fixture)
    assert first_fixture_result == second_fixture_result
    assert first_fixture_result["releaseId"] == "independent-community-art-release"
    assert first_fixture_result["summary"] == {"passed": 6, "blocked": 1, "unverified": 1}

    print("PASS: NFT release ledger, interruption, duplicate allocation, readiness mismatch, source independence, authority, and reproducibility")


if __name__ == "__main__":
    main()
