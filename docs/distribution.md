# Distribution contract

Follow AIWG's standalone plugin repository and Git-native package exchange documentation linked in references.md.

The wrapper at .aiwg/plugins/web3-distribution/manifest.json points to payload/ with payloadType framework. The nested payload manifest uses an empty frameworkConfig and root-level artifact directories. Both versions must match.

Development installs pin a reviewed commit, use --package web3-distribution and choose --project-local plus an explicit provider. Start in a disposable Git repository. Inspect the resulting package identity and lock before running marketplace verify; do not assume an owner/name coordinate across different hosts.

Release gates tracked in the roadmap: owner license and provenance approval; payload validation; no private data; provider compatibility; reproducible archives; Git-native install/verify/remove; negative/tamper tests; immutable tag and checksum publication; optional trust-required installation with --verify after publisher signing is implemented.

Maintain the same Git commit on origin (Gitea) and github (GitHub). Mirror identity is not publisher trust. No automated push mirror, catalog submission, signing key, release tag or marketplace endorsement is implied by this scaffold.

The NFT release module adds one agent, six skills, templates, and a Python
standard-library validator. Consumer smoke tests must assert that all seven
skills and both agents deploy, then run the validator against the independent
fixture. Installation alone does not authorize live actions described by the
skills.

## Verified development scaffold

AIWG 2026.9.12 installed commit `a2a7eb838cb1f2e75c4009acf0ba6a4c2abc2503` from GitHub into a disposable Claude consumer and from Gitea into a disposable Codex consumer. Both deployed the coordinator and intake skill and passed offline marketplace verification with integrity-only status. See install-verification.json and packaging-verification.json.

Artifact directories must be at the framework payload root. Merely placing them under the scaffold-generated src/ directory produced a success message without deployed artifacts in the initial smoke. Validation therefore checks actual installed agent and skill presence.
