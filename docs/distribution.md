# Distribution contract

Follow AIWG's standalone plugin repository and Git-native package exchange documentation linked in references.md.

The wrapper at .aiwg/plugins/web3-distribution/manifest.json points to payload/ with payloadType framework. The nested payload manifest uses frameworkConfig.path = "src/". Both versions must match.

Development installs pin a reviewed commit, use --package web3-distribution and choose --project-local plus an explicit provider. Start in a disposable Git repository. Inspect the resulting package identity and lock before running marketplace verify; do not assume an owner/name coordinate across different hosts.

Release gates tracked in the roadmap: owner license and provenance approval; payload validation; no private data; provider compatibility; reproducible archives; Git-native install/verify/remove; negative/tamper tests; immutable tag and checksum publication; optional trust-required installation with --verify after publisher signing is implemented.

Maintain the same Git commit on origin (Gitea) and github (GitHub). Mirror identity is not publisher trust. No automated push mirror, catalog submission, signing key, release tag or marketplace endorsement is implied by this scaffold.
