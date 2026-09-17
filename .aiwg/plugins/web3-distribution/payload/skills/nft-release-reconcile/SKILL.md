---
name: nft-release-reconcile
description: Reconcile intended NFT allocations and release policy against finalized chain events, ownership, metadata, and publication state.
triggers:
  - reconcile NFT release
  - verify NFT owners after mint
  - resume interrupted NFT mint
commandHint:
  modelRole: reasoning
  modelTier: advanced
---

# NFT Release Reconciliation

1. Pin the intended allocation ledger and deployed-contract manifest by hash.
   Select a finalized observation block and record number, hash, finality rule,
   chain ID, RPC operator, and observation time.
2. Acquire event/log evidence over an explicit block range and record raw
   response hashes. Cross-check the final block hash and contract state through
   an independent RPC operator.
3. For every allocation identity, compare intended recipient and quantity to
   mint/redeem events, transfer events, current owner or balance, token URI,
   immutable content identifier, and frozen-state requirements. Keep event-time
   and current-state conclusions distinct.
4. Reject duplicate allocation identities, duplicated mint events, missing
   entries in a `complete` reconciliation, owners/balances that contradict the
   declared policy, content identifier drift, and evidence from the wrong
   contract or chain.
5. Interrupted execution is resumable only from a reconciliation result.
   Produce `confirmed`, `pending`, `failed`, `unexpected`, and `ambiguous` sets.
   The next mint plan may contain only policy-permitted pending entries.
6. Use `templates/nft-reconciliation.json`. A partial reconciliation may be
   valid evidence, but it cannot close a release requiring completeness.
7. Update the reconciliation gate and required actions. Do not mutate the
   allocation source to make observations appear consistent.

