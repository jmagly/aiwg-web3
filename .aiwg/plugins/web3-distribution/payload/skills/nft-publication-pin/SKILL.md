---
name: nft-publication-pin
description: Prepare and verify immutable NFT content publication with independent persistence and retrieval evidence.
triggers:
  - pin NFT content
  - publish NFT metadata to IPFS
  - verify NFT content persistence
commandHint:
  modelRole: coding
  modelTier: standard
---

# NFT Publication and Pinning

The content gate must pass before this skill begins.

1. Build the immutable publication payload deterministically and record its
   root identifier, file inventory, and SHA-256 manifest. Rebuilding identical
   bytes must yield the same content identifier under the selected protocol.
2. Prepare provider commands without executing them unless live publication is
   authorized for the exact service, account, payload root, and cost ceiling.
   Read credentials only through approved project interfaces and never include
   them in arguments, logs, receipts, or the release ledger.
3. Record persistence observations from at least two independent operators or
   storage systems. Account aliases, gateways, regions, or endpoints owned by
   one backend do not count as independent.
4. Record retrieval observations from at least two independently operated
   gateways/clients when the release policy requires public retrieval. Each
   observation names operator, transport, content identifier, time, sampled
   paths, returned hashes, and result.
5. A provider “pin accepted” response is not persistence proof. A gateway HTTP
   success is not integrity proof. Rehash retrieved bytes and compare them to
   the release manifest.
6. Classify fixture, local-node, staging, and production evidence explicitly.
   Fixture evidence cannot satisfy a production publication gate.
7. Use `templates/nft-publication-evidence.json` and update the publication gate
   only when independence, durability, retrieval, and byte-integrity policies
   all pass. Publication approval does not authorize deployment or minting.

