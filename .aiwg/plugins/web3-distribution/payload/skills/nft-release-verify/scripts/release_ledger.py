#!/usr/bin/env python3
"""Deterministic structural validator for the AIWG Web3 NFT release ledger."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

API_VERSION = "aiwg.web3/nft-release-ledger/v1"
GATE_IDS = (
    "snapshot-reconciliation",
    "allocation-uniqueness",
    "content-integrity",
    "independent-publication",
    "deployed-contract-state",
    "mint-ownership-reconciliation",
    "public-release-receipt",
    "public-metadata-privacy",
)
STATUSES = {"passed", "blocked", "unverified"}
SHA256 = re.compile(r"^[0-9a-f]{64}$")
LIVE_GATE_ACTION = {
    "deployed-contract-state": "deploy",
    "mint-ownership-reconciliation": "mint",
}


class LedgerError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise LedgerError(message)


def require_keys(value: dict[str, Any], keys: tuple[str, ...], label: str) -> None:
    missing = [key for key in keys if key not in value]
    require(not missing, f"{label} missing required keys: {', '.join(missing)}")


def validate_sources(sources: Any) -> None:
    require(isinstance(sources, list), "sources must be an array")
    labels: set[str] = set()
    for index, source in enumerate(sources):
        require(isinstance(source, dict), f"source {index} must be an object")
        require_keys(source, ("label", "uri", "sha256", "evidenceClass"), f"source {index}")
        label = source["label"]
        require(isinstance(label, str) and label, f"source {index} label must be nonempty")
        require(label not in labels, f"duplicate source label: {label}")
        labels.add(label)
        require(isinstance(source["uri"], str) and source["uri"], f"source {label} uri must be nonempty")
        require(bool(SHA256.fullmatch(str(source["sha256"]))), f"source {label} sha256 is invalid")
        require(
            source["evidenceClass"] in {"frozen-source", "simulation", "production"},
            f"source {label} evidenceClass is invalid",
        )


def validate_allocations(allocations: Any) -> None:
    require(isinstance(allocations, list), "allocations must be an array")
    identities: set[str] = set()
    for index, allocation in enumerate(allocations):
        require(isinstance(allocation, dict), f"allocation {index} must be an object")
        require_keys(allocation, ("identity", "recipient", "quantity"), f"allocation {index}")
        identity = str(allocation["identity"])
        require(identity, f"allocation {index} identity must be nonempty")
        require(identity not in identities, f"duplicate allocation identity: {identity}")
        identities.add(identity)
        require(isinstance(allocation["recipient"], str) and allocation["recipient"], f"allocation {identity} recipient must be nonempty")
        require(isinstance(allocation["quantity"], int) and allocation["quantity"] > 0, f"allocation {identity} quantity must be positive")


def independent(observations: Any, label: str) -> None:
    require(isinstance(observations, list), f"{label} observations must be an array")
    operators: set[str] = set()
    backends: set[str] = set()
    for index, observation in enumerate(observations):
        require(isinstance(observation, dict), f"{label} observation {index} must be an object")
        require_keys(observation, ("operator", "backend", "observedAt", "result"), f"{label} observation {index}")
        require(observation["result"] == "pass", f"{label} observation {index} did not pass")
        operators.add(str(observation["operator"]))
        backends.add(str(observation["backend"]))
    require(len(operators) >= 2, f"{label} evidence requires at least two independent operators")
    require(len(backends) >= 2, f"{label} evidence requires at least two independent backends")


def validate_authority(authorities: Any, action: str) -> None:
    require(isinstance(authorities, list), "authorities must be an array")
    matches = [entry for entry in authorities if isinstance(entry, dict) and entry.get("action") == action]
    require(matches, f"passed live gate requires {action} authority")
    for entry in matches:
        require_keys(
            entry,
            ("action", "target", "chainId", "actor", "costCeiling", "authorizedBy", "scope"),
            f"{action} authority",
        )
        require(entry["scope"] == "live", f"{action} authority scope must be live")
        require(bool(entry["authorizedBy"]), f"{action} authority must identify authorizing instruction")


def validate_ledger(ledger: Any) -> dict[str, int]:
    require(isinstance(ledger, dict), "ledger must be an object")
    require_keys(
        ledger,
        (
            "apiVersion",
            "releaseId",
            "candidateRevision",
            "environment",
            "generatedAt",
            "productionReady",
            "sources",
            "allocations",
            "authorities",
            "observations",
            "gates",
            "requiredActions",
        ),
        "ledger",
    )
    require(ledger["apiVersion"] == API_VERSION, f"apiVersion must be {API_VERSION}")
    require(isinstance(ledger["releaseId"], str) and ledger["releaseId"], "releaseId must be nonempty")
    require(isinstance(ledger["candidateRevision"], int) and ledger["candidateRevision"] >= 1, "candidateRevision must be >= 1")
    require(ledger["environment"] in {"development", "staging", "production"}, "environment is invalid")
    require(isinstance(ledger["productionReady"], bool), "productionReady must be boolean")
    validate_sources(ledger["sources"])
    validate_allocations(ledger["allocations"])

    gates = ledger["gates"]
    require(isinstance(gates, list) and len(gates) == len(GATE_IDS), "ledger must contain exactly eight gates")
    actual_ids = tuple(gate.get("id") if isinstance(gate, dict) else None for gate in gates)
    require(actual_ids == GATE_IDS, "gate IDs or order are invalid")
    unresolved: set[str] = set()
    counts = {"passed": 0, "blocked": 0, "unverified": 0}
    gate_by_id: dict[str, dict[str, Any]] = {}
    for gate in gates:
        require_keys(gate, ("id", "status", "evidence", "actions"), f"gate {gate.get('id', '?')}")
        status = gate["status"]
        require(status in STATUSES, f"gate {gate['id']} status is invalid")
        require(isinstance(gate["evidence"], list), f"gate {gate['id']} evidence must be an array")
        require(isinstance(gate["actions"], list), f"gate {gate['id']} actions must be an array")
        if status == "passed":
            require(gate["evidence"], f"passed gate {gate['id']} must include evidence")
            require(not gate["actions"], f"passed gate {gate['id']} cannot have unresolved actions")
        else:
            require(gate["actions"], f"unresolved gate {gate['id']} must include actions")
            unresolved.update(str(action) for action in gate["actions"])
        counts[status] += 1
        gate_by_id[gate["id"]] = gate

    required_actions = ledger["requiredActions"]
    require(isinstance(required_actions, list), "requiredActions must be an array")
    require(len(required_actions) == len(set(required_actions)), "requiredActions contains duplicates")
    require(set(str(action) for action in required_actions) == unresolved, "requiredActions does not match unresolved gate actions")

    observations = ledger["observations"]
    require(isinstance(observations, dict), "observations must be an object")
    if gate_by_id["independent-publication"]["status"] == "passed":
        independent(observations.get("publication"), "publication")
    if any(gate_by_id[gate_id]["status"] == "passed" for gate_id in LIVE_GATE_ACTION):
        independent(observations.get("chain"), "chain")
    for gate_id, action in LIVE_GATE_ACTION.items():
        if gate_by_id[gate_id]["status"] == "passed":
            validate_authority(ledger["authorities"], action)

    ready = all(gate["status"] == "passed" for gate in gates)
    require(ledger["productionReady"] == ready, f"productionReady must be {str(ready).lower()}")
    return counts


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode()


def validate_file(path: Path) -> dict[str, Any]:
    ledger = json.loads(path.read_text(encoding="utf-8"))
    counts = validate_ledger(ledger)
    return {
        "releaseId": ledger["releaseId"],
        "candidateRevision": ledger["candidateRevision"],
        "productionReady": ledger["productionReady"],
        "summary": counts,
        "canonicalSha256": hashlib.sha256(canonical_bytes(ledger)).hexdigest(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    validate = subparsers.add_parser("validate")
    validate.add_argument("ledger", type=Path)
    args = parser.parse_args()
    try:
        result = validate_file(args.ledger)
    except (OSError, json.JSONDecodeError, LedgerError) as error:
        print(str(error), file=sys.stderr)
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

