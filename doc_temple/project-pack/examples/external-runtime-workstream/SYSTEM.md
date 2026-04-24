# SYSTEM

## Role

This folder is the external-runtime coordination lane for `Example Project`.

It is an active workstream in the root-and-workstreams model.

## Boundaries

This workstream owns:

- exports
- asset handoff rules
- bridge notes
- coordination around the external runtime

This workstream does not own:

- internal shared APIs
- project-wide planning
- setup ownership

Related or dependent workstreams to respect:

- platform-core
- delivery-lane
- project-setup

External dependency path, if applicable:

- `../external-runtime/` or another project-specific location

## Rules

- keep this workstream focused on the bridge to the external runtime
- use root startup docs before deep local work
- record dependency-sensitive changes carefully
- update local `CHANGELOG.md` for workstream changes
- keep `SIGN_UP.md` usable as a short thread trace
