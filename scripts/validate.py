from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
wrapper = root / ".aiwg/plugins/web3-distribution"
w = json.loads((wrapper / "manifest.json").read_text())
payload = (wrapper / w["pluginConfig"]["payloadPath"]).resolve()
assert payload.is_relative_to(wrapper.resolve()), "payload escapes wrapper"
p = json.loads((payload / "manifest.json").read_text())
assert w["type"] == "plugin" and p["type"] == "framework"
assert w["pluginConfig"]["payloadType"] == p["type"]
assert w["version"] == p["version"]
for provider in ("claude", "codex"):
    assert provider in w["platforms"] and provider in p["platforms"]
for phase in ("scope", "design", "build", "verify", "release", "operate"):
    assert (payload / "flows" / (phase + ".md")).is_file()
agents = {path.stem for path in (payload / "agents").glob("*.md")}
skills = {path.parent.name for path in (payload / "skills").glob("*/SKILL.md")}
assert {"web3-lifecycle-coordinator", "nft-release-steward"} <= agents
assert {
    "web3-intake",
    "nft-release-plan",
    "nft-content-prepare",
    "nft-publication-pin",
    "nft-deploy-mint",
    "nft-release-reconcile",
    "nft-release-verify",
} <= skills
validator = payload / "skills/nft-release-verify/scripts/release_ledger.py"
assert validator.is_file(), "NFT release validator missing"
for f in payload.rglob("*"):
    assert not f.is_symlink(), f"symlink: {f}"
    if f.suffix == ".md":
        text = f.read_text()
        for forbidden in ("/home/manitcor", "roko.network", "pwROKO", "roko-frontend-lead"):
            assert forbidden not in text, f"project coupling: {f}: {forbidden}"
print("PASS: payload containment, identity, versions, providers, lifecycle artifacts, and project-coupling checks")
