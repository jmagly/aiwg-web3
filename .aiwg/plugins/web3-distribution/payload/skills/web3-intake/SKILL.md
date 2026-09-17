---
name: web3-intake
description: Establish a Web3 project's chain, application, evidence and execution boundaries before selecting lifecycle work.
triggers:
  - scope a web3 project
  - web3 lifecycle intake
commandHint:
  modelRole: reasoning
  modelTier: advanced
---

# Web3 Intake

1. Read project instructions and supplied requirements. Identify the requested phase and already-authorized operations.
2. Record chain family and network identity, asset units/decimals, contract ABI/address sources, frontend/toolchain versions from the lockfile, wallet and RPC requirements, and selected modules. Mark unknowns explicitly.
3. Identify trust boundaries, signing/custody interfaces without reading secret values, finality expectations, data provenance, rollback limitations and project-selected acceptance budgets.
4. Discover existing AIWG specialists needed by the work. Distinguish installed capability from planned framework modules.
5. Produce a scope record using templates/project-profile.md and an evidence ledger using templates/gate-evidence.md under the consumer's resolved artifact root.
6. Move to design only when scope, authority and missing-input handling are explicit. Carry unresolved items forward with owners; never fill contract addresses or economic policy from examples.
