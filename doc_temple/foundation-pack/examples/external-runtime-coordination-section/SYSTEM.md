# System

## Role

This folder is the coordination bridge above an external runtime for
`Example Project`.

It is a promoted section in the root-and-sections thread model.

## Boundaries

This section owns:

- bridge documentation
- runtime path awareness
- migration decisions
- curation and experiment coordination

This section does not own:

- the external runtime itself
- shared runtime contracts
- operator delivery workflow
- bootstrap tooling behavior

Upstream or sibling sections to respect:

- root
- shared-core
- delivery-lane
- project-init

External runtime or dependency path, if applicable:

- `C:\path\to\external-runtime`

## Rules

- keep this section clearly marked as a coordination layer
- use root startup docs before section work
- report reusable behavior needs to `shared-core`
- update local `CHANGELOG.md` for section changes
- keep `SIGN_UP.md` usable as a short thread trace
- tag every task with at least one section tag and one task-type tag
