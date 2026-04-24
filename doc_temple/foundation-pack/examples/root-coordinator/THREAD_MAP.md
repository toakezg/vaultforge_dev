# Example Project Thread Map

Date: YYYY-MM-DD

`Example Project` uses a root-and-sections thread model.

Root is overhead coordination. Promoted sections are focused worker bases.

## Root Thread

Use root for:

- cross-lane planning
- architecture decisions
- section promotion or parking
- thread routing
- handoffs between sections
- high-level changelog updates

## Shared Core

Use `shared-core` for:

- shared runtime behavior
- shared metadata contracts
- compatibility and validation
- cross-lane reusable features

## Delivery Lane

Use `delivery-lane` for:

- wrappers
- prompt banks
- output routing
- review surfaces
- delivery-oriented workflow helpers

## Creative Bridge

Use `creative-bridge` for:

- coordination above an external runtime
- bridge expectations
- prompt experiments and curation
- migration decisions

## Project Init

Use `project-init` for:

- bootstrap scripts
- installers
- environment setup
- first-run tooling docs

## Parked Or Supporting Folders

List folders here when they exist but are not promoted sections yet.
