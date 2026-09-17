# Source audit and extraction provenance

Audit date: 2026-09-16. Local inspection covered 42 checkouts representing 21 distinct Git common directories. Ten custom marketing agents (4,097 lines) have identical documentation copies and identical copies in three additional worktrees. These are ten distinct roles. Runtime effectiveness and remote completeness were not established.

The following references are access-controlled source material. No original agent bodies, machine paths, private topology or credentials are copied into this repository. Hashes identify inspected working-file bytes; the recorded checkout HEAD alone does not establish that every file was clean.

| Source role | Lines | SHA-256 | Source reference |
|---|---:|---|---|
| roko-3d-engineer | 330 | `0c65f385e0455e3e6f09ab9e589f53227aca8eccbe075b0cc86d9b92e1dafea5` | [source](https://git.integrolabs.net/roko/roko-marketing/src/commit/54ea5c454d46232ede157e666597c399b9e36ef1/.claude/agents/roko-3d-engineer.md) |
| roko-devops-engineer | 545 | `e1ed747995de23f82b7e053b14a7a8f6598365174d8e72ee07faf05541c1df05` | [source](https://git.integrolabs.net/roko/roko-marketing/src/commit/54ea5c454d46232ede157e666597c399b9e36ef1/.claude/agents/roko-devops-engineer.md) |
| roko-frontend-lead | 176 | `06305c849ddb24887a74c9a3b7898951ffc2c4388d68f8e4244a4a79bc66cdf2` | [source](https://git.integrolabs.net/roko/roko-marketing/src/commit/54ea5c454d46232ede157e666597c399b9e36ef1/.claude/agents/roko-frontend-lead.md) |
| roko-performance-optimizer | 415 | `07e2b18bb0e805dd037d4e5121bffff2013bb16977ddfe3cdc1e44369c330fbc` | [source](https://git.integrolabs.net/roko/roko-marketing/src/commit/54ea5c454d46232ede157e666597c399b9e36ef1/.claude/agents/roko-performance-optimizer.md) |
| roko-pmo | 449 | `3083e3069c1f6973473eb82ec9c0083e14a6b84eae61642f9e93cc18b8ca2100` | [source](https://git.integrolabs.net/roko/roko-marketing/src/commit/54ea5c454d46232ede157e666597c399b9e36ef1/.claude/agents/roko-pmo.md) |
| roko-qa-lead | 343 | `a9d05709f054588d2fbc003a17ae2daccf58d29b85b65a899c211b62a5edc81b` | [source](https://git.integrolabs.net/roko/roko-marketing/src/commit/54ea5c454d46232ede157e666597c399b9e36ef1/.claude/agents/roko-qa-lead.md) |
| roko-security-auditor | 580 | `7a3ce9b5ecaa4adad1cccc6b8ed7f43b0e7420327acaaec7e5d4a95ed66d03be` | [source](https://git.integrolabs.net/roko/roko-marketing/src/commit/54ea5c454d46232ede157e666597c399b9e36ef1/.claude/agents/roko-security-auditor.md) |
| roko-technical-architect | 465 | `45ce700d68424f0dce268f35731eb383c0788ea8cb13fccd2df9ad1a69966749` | [source](https://git.integrolabs.net/roko/roko-marketing/src/commit/54ea5c454d46232ede157e666597c399b9e36ef1/.claude/agents/roko-technical-architect.md) |
| roko-ui-ux-designer | 548 | `f2ba5de5aa6f30a3a59cd631fe9655007c0cfcd4cfaea5dbd7de934efbfc52b7` | [source](https://git.integrolabs.net/roko/roko-marketing/src/commit/54ea5c454d46232ede157e666597c399b9e36ef1/.claude/agents/roko-ui-ux-designer.md) |
| roko-web3-specialist | 246 | `ddb175a3c4beff70af664f372f48a64ff1f7c42d9daeed7e6eb8ef6fe3e68d4c` | [source](https://git.integrolabs.net/roko/roko-marketing/src/commit/54ea5c454d46232ede157e666597c399b9e36ef1/.claude/agents/roko-web3-specialist.md) |

## Findings

- Web3 role: old Wagmi hooks despite a newer stack declaration; fixed token/governance policy; unresolved analytics-specialist handoff.
- 3D role: ascending LOD thresholds with first-match greater-than-or-equal select the first level for every nonnegative distance.
- Security role: substring hostname trust; text search of ABI calldata; SQL character stripping; blanket inline-script allowance; invalid incident example; unsuitable default logging sink.
- Performance role: ID-only memo comparison can suppress updates; conflicting metric budgets; unsupported nanosecond browser claims.
- Supporting roles: duplicated standard AIWG responsibilities, fixed provider/brand/project requirements, frozen sample schedules, untested scaffolding.

## Disposition

Extract EVM integration and independent real-time 3D capability. Rewrite security guidance. Extend existing frontend, architecture, test, performance, design, DevOps and project-management roles rather than copying the suite. Generalize holder chain/market context as skills with their required scripts and schemas. Separate chain/host adapters from validator lifecycle. Establish the deployed NFT steward canonical source and discovery wiring.

## Adjacent sources

- `roko-holder-claims`: `.aiwg/addons/holder-chain-context/skills/holder-chain-context-skill/SKILL.md` and `.aiwg/addons/holder-market-context/skills/holder-market-context-skill/SKILL.md`.
- `itops`: `.aiwg/addons/openbao-migrate/agents/roko-launch-operator.md`.
- NFT release steward deployment input: untracked generated file at the audited
  Itops checkout (`667f0dacb89a6f7d3c3838002e962d875ec16459`), SHA-256
  `49d3007b2e029a0c37cf86eb482b6fc568b4a0879f119f8d6616aef91b13333d`.
  `aiwg show agent nft-release-steward` did not resolve and no authoritative
  upstream source was found. Its short gate vocabulary informed the audit; it
  was not copied as the distributable definition.
- NFT evidence reference: `roko-generative-nft-series` commit
  `62b65eebee4be11e3126c4bb7069957051e7d72c` introduced the production
  verification matrix and regression cases. The private repository remains
  unlicensed. This framework therefore uses newly authored, provider-neutral
  skills and a different `aiwg.web3/*` evidence contract; it does not copy the
  Roko schemas, implementation, branding, addresses, or fixtures.

## NFT release port provenance and rights

The canonical generalized source is this repository under
`.aiwg/plugins/web3-distribution/payload/`. It is currently `UNLICENSED`, so the
owner retains all rights and public redistribution is not granted. This records
the rights state without treating W3-012 as complete. Public release remains
blocked until the owner selects a license and completes the rights review.

See references.md for AIWG authoring and technical documentation. The issue backlog specifies remediation and acceptance tests.
