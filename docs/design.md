# Framework design

The lifecycle is scope → design → build → verify → release → operate. Each phase has explicit inputs, outputs and gates. A framework coordinator routes to existing AIWG SDLC/operations specialists; the package does not copy those roles.

## Boundaries

- EVM application integration: wallets, chain/account state, transaction simulation and lifecycle, RPC behavior.
- Optional governance and account abstraction skills; neither is assumed for every project.
- Snapshot chain/market context as deterministic evidence workflows with adapters.
- NFT release stewardship is implemented as normalized evidence and authority
  skills. Provider, chain, wallet, storage, and mint adapters remain consumer
  responsibilities. Validator lifecycle remains a later module with separate
  execution authority and chain-specific adapters.
- Real-time 3D is an optional independent addon deliverable; ordinary graphics users must not need Web3 rules.
- Project policy supplies networks, contract ABIs, token units, providers, environments, brand assets, risk budgets and authorization. Never infer them from Roko defaults.

## Existing AIWG dependencies

Resolve blockchain-developer, frontend-specialist, architecture-designer, security-auditor, test-engineer, performance-engineer, devops-engineer, product-designer and project-manager through AIWG discovery when needed. Missing roles are explicit prerequisites; this scaffold does not silently install every AIWG framework. These are workflow dependencies, not unverified package-manager dependency declarations.

## Release contract

One canonical payload; synchronized CalVer wrapper/payload versions; reviewed immutable source commit; source provenance and license; deterministic provider archives/checksums; clean-consumer install and removal evidence; signed publisher metadata only after a reviewed custody/trust design. No production capability claim solely from prompt presence or package validation.

## NFT release module

`nft-release-steward` coordinates six skills. The normalized ledger has eight
ordered gates and derives readiness from gate state. The shipped validator is
offline and provider-neutral; acquisition adapters normalize chain and storage
observations into the evidence contract.

Preparation, simulation, publication, deployment, minting, and reconciliation
are separate authority domains. Two-source verification requires distinct
operators and backends, not merely distinct URLs. Ambiguous transactions are
reconciled by hash and sender/nonce before any retry.
