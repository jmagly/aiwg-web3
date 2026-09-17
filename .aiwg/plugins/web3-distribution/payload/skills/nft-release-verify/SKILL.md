---
name: nft-release-verify
description: Validate an NFT release ledger, evidence independence, authority boundaries, and final readiness using deterministic checks.
triggers:
  - verify NFT release
  - NFT release readiness
  - audit NFT release ledger
commandHint:
  modelRole: reasoning
  modelTier: advanced
---

# NFT Release Verification

Run after each candidate update and before reporting a release ready.

1. Locate this deployed skill directory and run:

   ```bash
   python3 scripts/release_ledger.py validate <release-ledger.json>
   ```

2. Rehash every recorded local source and compare it to the ledger when the
   source remains available. Resolve immutable remote references rather than
   trusting a mutable branch, endpoint, or gateway response.
3. Verify the eight ordered invariants: snapshot reconciliation, allocation
   uniqueness, content integrity, independent publication, deployed contract
   state, mint/ownership reconciliation, public release receipt, and public
   metadata privacy.
4. For chain and publication observations, validate source independence. Each
   observation declares both `operator` and `backend`; distinct URLs with the
   same backend are not independent.
5. Verify that every `passed` gate has evidence, no `blocked` or `unverified`
   required gate remains, required actions equal the union of unresolved gate
   actions, and `productionReady` is derived rather than asserted.
6. Confirm live actions each have a matching authority record. Preparation and
   simulation evidence cannot substitute for one.
7. Emit a readiness summary containing release ID, candidate revision, source
   hashes, pass/block/unverified counts, independence results, authority
   coverage, and exact actions. A failed validator or missing source makes the
   release unready.

The validator intentionally does not connect to wallets, RPC services, or
pinning providers. Acquisition belongs to project adapters; this skill checks
the normalized evidence contract.

