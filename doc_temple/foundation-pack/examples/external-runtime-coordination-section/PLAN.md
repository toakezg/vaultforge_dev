# Plan

## Section Thread Model

- `creative-bridge` is a promoted worker section under root coordination.
- section threads should read root startup docs before section docs.
- this section should coordinate around the external runtime, not silently become
  the external runtime.

## Current Direction

- keep the bridge legible
- protect the external runtime from accidental migration by drift
- surface shared needs to `shared-core` when they are no longer local experiments

## Watchpoints

- coordination docs can be mistaken for runtime ownership if warnings are weak
- bridge changes can affect shared contracts if they are not reported upward
- external paths can get stale if no one tends the docs

## Forward Look

- decide migration only with explicit intent
- improve bridge inventory and curation as the lane matures
- keep the line between experiments and shared behavior clear
