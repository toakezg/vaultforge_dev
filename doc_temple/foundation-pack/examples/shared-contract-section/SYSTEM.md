# System

## Role

This folder is the shared-contract and reusable runtime section for
`Example Project`.

It is a promoted section in the root-and-sections thread model.

## Boundaries

This section owns:

- shared runtime behavior
- shared metadata and output contracts
- compatibility helpers
- tests and validation around shared features

This section does not own:

- delivery workflow rules
- client-facing prompt banks
- external runtime experimentation
- setup tooling docs that are specific to project bootstrap

Upstream or sibling sections to respect:

- root
- delivery-lane
- creative-bridge
- project-init

External runtime or dependency path, if applicable:

- none by default

## Rules

- keep this section boring, reusable, and lane-neutral
- use root startup docs before section work
- report cross-lane contract changes back to root and affected sections
- update local `CHANGELOG.md` for section changes
- keep `SIGN_UP.md` usable as a short thread trace
- tag every task with at least one section tag and one task-type tag
