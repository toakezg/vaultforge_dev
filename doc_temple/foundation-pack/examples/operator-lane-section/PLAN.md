# Plan

## Section Thread Model

- `delivery-lane` is a promoted worker section under root coordination.
- section threads should read root startup docs before section docs.
- this section should own workflow surfaces rather than shared runtime logic.

## Current Direction

- keep wrappers stable and understandable
- keep outputs and review surfaces organized
- move only proven reusable fragments into shared-core

## Watchpoints

- the lane can get noisy if it starts absorbing shared logic
- review and delivery rules can drift from actual outputs if docs stop moving
- local convenience rules can turn brittle if naming and routing are unclear

## Forward Look

- improve operator-facing workflow without duplicating shared contracts
- keep naming and routing explicit
- lift reusable pieces into shared-core only when confidence is high
