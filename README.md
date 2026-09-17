# AIWG Web3

An independently versioned, opt-in AIWG framework for the Web3 application and operations lifecycle.

**Status: development scaffold.** The lifecycle, intake skill, package wrapper and implementation backlog exist. Generalized specialist agents and operational adapters are not yet released. Packaging success does not establish production readiness.

Canonical engineering tracker: https://git.integrolabs.net/roctinam/aiwg-web3/issues
Public distribution repository: https://github.com/jmagly/aiwg-web3

## Use on demand

Use AIWG 2026.9.12 (the version tested during scaffold creation) and Git access to the chosen repository. Select a reviewed immutable commit; no release tag is claimed yet.

```bash
aiwg install https://github.com/jmagly/aiwg-web3.git \
  --ref <reviewed-commit> --package web3-distribution \
  --project-local --deploy --provider claude
```

For Codex, substitute `--provider codex`. The Gitea remote is `https://git.integrolabs.net/roctinam/aiwg-web3.git`; use an identical verified commit. Private repositories require authenticated Git access. Installation without a publisher signature provides integrity-only status; signed releases remain a tracked deliverable.

## Develop and package

```bash
python3 scripts/validate.py
aiwg package-plugin web3-distribution --dry-run
aiwg package-plugin web3-distribution --provider all --output dist/plugins
```

Canonical framework content lives in `.aiwg/plugins/web3-distribution/payload/`. The wrapper owns delivery; its payload is `type: framework`. There is one content source, with no fork of AIWG core or copied provider deployment trees.

See [design](docs/design.md), [roadmap](docs/roadmap.md), [source audit](docs/source-audit.md), [distribution](docs/distribution.md), and [references](docs/references.md).

## License

No redistribution license has been selected. `UNLICENSED` is intentional during preparation; the owner must select a license and review source rights before a distributable release. See the licensing issue in the roadmap.
