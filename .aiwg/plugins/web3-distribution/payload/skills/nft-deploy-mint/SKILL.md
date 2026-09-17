---
name: nft-deploy-mint
description: Prepare, authorize, execute, and reconcile NFT deployment and mint transactions without treating submission as completion.
triggers:
  - deploy NFT contract
  - mint NFT release
  - execute NFT release transactions
commandHint:
  modelRole: coding
  modelTier: advanced
---

# NFT Deployment and Mint

Use this skill for live chain mutations only after planning, content, and
publication gates pass.

## Preflight

1. Verify chain ID from two independent RPC operators at a finalized block.
2. Bind source commit, compiler/tool versions, artifact hashes, constructor or
   initializer arguments, expected deployer/signer, nonce policy, contract
   addresses when already deployed, immutable content identifiers, allocation
   root, supply cap, and role assignments into a reviewed deployment manifest.
3. Simulate every transaction against the target network state. Record calls,
   state changes, events, gas estimate, fee/value ceiling, and expected
   postconditions. Simulation evidence never authorizes execution.
4. Require a live authority record for the exact action. Deployment authority
   does not imply mint authority; mint authority does not imply metadata freeze,
   role transfer, treasury movement, or DNS authority.

## Execution and recovery

5. Before signing, display target chain, sender, nonce, destination/creation,
   value, calldata or artifact hash, fee ceiling, and irreversible effects.
6. Record transaction hash immediately after submission. On timeout or
   transport failure, stop. Query independent RPC sources by hash and by
   sender/nonce. Resume only after classifying the transaction as pending,
   included, replaced, dropped, or unknown.
7. Never resend an unknown transaction with the same business effect. A
   replacement must be explicit and linked to the original nonce/hash.
8. For batched or sequential minting, checkpoint each confirmed item or range.
   On interruption, derive the resume set from finalized chain events and
   ownership state, not from the last local loop index.
9. Mark deployment or mint passed only after required finality and independent
   verification of bytecode/source, roles, supply, events, owners, token URIs,
   allocation root, and content identifiers. Record failed and skipped items;
   do not rewrite the intended allocation ledger.

