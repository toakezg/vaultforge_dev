# Plan

## Section Thread Model

- `shared-core` is a promoted worker section under root coordination.
- section threads should read root startup docs before section docs.
- this section should own shared behavior that more than one lane needs.

## Current Direction

- keep shared primitives stable and lane-neutral
- protect compatibility as shared features grow
- let lane-owned workflow logic stay outside this section until it proves reusable

## Watchpoints

- this section can become bloated if every local convenience gets promoted here
- compatibility can break quietly if wrappers and direct usage drift apart
- lane-specific language can leak into shared contracts if boundaries stay fuzzy

## Forward Look

- grow shared features carefully
- keep verification close to contract changes
- split into finer shared modules only when it clearly improves maintenance
