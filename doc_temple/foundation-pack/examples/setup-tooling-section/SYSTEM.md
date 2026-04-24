# System

## Role

This folder is the setup and tooling section for `Example Project`.

It is a promoted section in the root-and-sections thread model.

## Boundaries

This section owns:

- setup scripts
- installer helpers
- environment assumptions
- first-run tooling docs

This section does not own:

- shared runtime feature growth
- delivery workflow ownership
- external runtime experiments
- coordinator-level routing decisions

Upstream or sibling sections to respect:

- root
- shared-core
- delivery-lane
- creative-bridge

External runtime or dependency path, if applicable:

- none by default

## Rules

- keep setup behavior explicit and repeatable
- use root startup docs before section work
- document environment assumptions where operators will actually find them
- update local `CHANGELOG.md` for section changes
- keep `SIGN_UP.md` usable as a short thread trace
- tag every task with at least one section tag and one task-type tag
