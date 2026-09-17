# Web3 lifecycle framework

The framework includes Web3 lifecycle intake plus a complete NFT release skill
set: planning, content preparation, independent publication, deployment/mint,
reconciliation, and deterministic verification. Other Web3 specialist modules
remain tracked work.

Read plan-act-web3.md and actors-and-templates.md. Phases: scope, design, build, verify, release, operate. Inputs are project configuration and evidence, never embedded network identities or credentials.

NFT releases begin with `nft-release-plan` under the
`nft-release-steward`. Live chain or publication work requires exact authority;
preparation never supplies that authority. Validate normalized release ledgers
with `nft-release-verify` and its shipped `scripts/release_ledger.py`.
