# System

## Role

This folder is the operator workflow and delivery section for `Example Project`.

It is a promoted section in the root-and-sections thread model.

## Boundaries

This section owns:

- wrappers
- prompt banks
- output routing
- review surfaces
- delivery-oriented metadata and operator guidance

This section does not own:

- shared runtime contracts
- cross-lane API primitives
- external runtime experimentation
- bootstrap tooling ownership

Upstream or sibling sections to respect:

- root
- shared-core
- creative-bridge
- project-init

External runtime or dependency path, if applicable:

- none by default

## Rules

- keep this section focused on operator workflow
- use root startup docs before section work
- report shared fragment candidates upward when they stabilize
- update local `CHANGELOG.md` for section changes
- keep `SIGN_UP.md` usable as a short thread trace
- tag every task with at least one section tag and one task-type tag
