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
assert list((payload / "agents").glob("*.md"))
assert list((payload / "skills").glob("*/SKILL.md"))
for f in payload.rglob("*"):
    assert not f.is_symlink(), f"symlink: {f}"
    if f.suffix == ".md":
        text = f.read_text()
        for forbidden in ("/home/manitcor", "roko.network", "pwROKO", "roko-frontend-lead"):
            assert forbidden not in text, f"project coupling: {f}: {forbidden}"
print("PASS: payload containment, identity, versions, providers, phases and project-coupling checks")
