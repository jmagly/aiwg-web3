---
name: nft-content-prepare
description: Prepare deterministic NFT metadata and media manifests with allocation, privacy, content-policy, and hash integrity gates.
triggers:
  - prepare NFT metadata
  - build NFT release content
  - verify NFT content
commandHint:
  modelRole: coding
  modelTier: standard
---

# NFT Content Preparation

Operate only on the release selected by `nft-release-plan`.

1. Pin the collection specification, allocation ledger, generator/tool
   versions, source commit, seed or entropy evidence, and content policy by
   SHA-256 before generation.
2. Validate allocation uniqueness before writing content. Reject duplicate
   identity keys, missing recipients when the release requires recipients, and
   counts that disagree across source, generated content, and ledger.
3. Generate into a new output directory. Canonicalize JSON using the project’s
   declared serialization contract; record media type, byte length, SHA-256,
   and relative path for every file. Never embed machine-local absolute paths.
4. Run privacy and content-policy checks over public metadata and rendered
   media. Public artifacts must not contain secrets, private topology,
   unpublished wallet labels, personal data, hidden prompts, or unapproved
   project terminology.
5. Verify every metadata media reference against the manifest. For mutable
   staging URLs, keep the content gate blocked until immutable publication
   identifiers can be substituted and the manifest rebuilt.
6. Record review evidence and approval as separate objects. A generated
   approval template is not an approval. Content approval does not authorize
   pinning, deployment, or minting.
7. Update only the content gate and its evidence in the release ledger. Preserve
   prior source hashes and fail on drift unless the operator explicitly starts
   a new candidate revision.

