# THREAD MAP

## How To Use This Map

- start here before cross-workstream edits
- choose one owner first
- report shared impacts back to root

## Root-Owned Work

Root owns:

- architecture
- project-level planning
- routing
- shared documentation

## Active Workstreams

### platform-core

- Path: `./platform-core/`
- Role: shared runtime and contract foundation
- Owns:
  - shared adapters
  - schemas
  - reusable low-level helpers
- Does not own:
  - workflow wrappers
  - review surfaces
  - setup tooling
- Related workstreams:
  - delivery-lane
  - creative-runtime
- Report upward when:
  - shared contracts or architecture boundaries change

### delivery-lane

- Path: `./delivery-lane/`
- Role: workflow, prompts, outputs, and review handling
- Owns:
  - wrappers
  - routing
  - review surfaces
  - output shaping
- Does not own:
  - shared contracts
  - setup scripts
  - external runtime ownership
- Related workstreams:
  - platform-core
  - creative-runtime
- Report upward when:
  - stable shared fragments should move into `platform-core`

### creative-runtime

- Path: `./creative-runtime/`
- Role: coordination around an external creative toolchain
- Owns:
  - exports
  - asset handoff rules
  - bridge notes
- Does not own:
  - shared internal APIs
  - project-wide planning
  - setup ownership
- Related workstreams:
  - platform-core
  - delivery-lane
- Report upward when:
  - dependency shifts affect project architecture or shared workflows

### project-setup

- Path: `./project-setup/`
- Role: bootstrap, local setup, and tooling conventions
- Owns:
  - setup guidance
  - local environment rules
  - scaffold helpers
- Does not own:
  - delivery behavior
  - shared runtime contracts
  - external runtime coordination
- Related workstreams:
  - platform-core
  - delivery-lane
  - creative-runtime
- Report upward when:
  - setup choices create project-wide constraints

## Shared-Change Rule

If work changes shared contracts, architecture, or routing, update root docs as
part of the same change.
