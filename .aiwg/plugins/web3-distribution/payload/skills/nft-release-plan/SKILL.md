---
name: nft-release-plan
description: Create or resume an evidence-bound NFT release ledger and determine which preparation and live-execution gates are ready.
triggers:
  - plan an NFT release
  - resume NFT release
  - NFT release ledger
commandHint:
  modelRole: reasoning
  modelTier: advanced
---

# NFT Release Plan

Use this skill before any other NFT release skill.

1. Resolve the consumer artifact root with `aiwg artifacts path --json
   --check-write`. Write release evidence beneath
   `<artifact_root>/web3/releases/<release-id>/`; never fall back to a local
   `.aiwg` directory when the resolved root differs.
2. Read the Web3 project profile, existing ledger, collection/contract
   specification, allocation source, content policy, network configuration,
   and applicable approvals. Unknown facts remain `unverified`.
3. Create `release-ledger.json` from `templates/nft-release-ledger.json`. Use a
   stable release ID. Record source path, SHA-256, immutable source reference,
   and evidence class for every input.
4. Reject duplicate allocation keys. The project profile defines the identity
   key, such as token ID, claim ID, or `(contract, token ID)`. Do not silently
   combine recipients or select the last duplicate.
5. Walk gates in this order: snapshot → allocation → content → publication →
   deployment → mint → reconciliation → final verification. Mark a gate
   `passed` only when its evidence list is nonempty and its required checks
   succeed. Otherwise use `blocked` or `unverified` with concrete actions.
6. Classify the next action as `prepare`, `simulate`, or `live`. Preparation
   and simulation can produce reviewed commands and manifests. Live actions
   require a separate authority record naming target, chain, actor, action,
   value/cost ceiling, time scope, and authorizing session instruction.
7. Validate the ledger with the script shipped alongside
   `nft-release-verify`. Report the release ID, passed/blocked/unverified gates,
   exact next gate, and whether live authority is present. Never report the
   release ready while a required gate is blocked or unverified.

