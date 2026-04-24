# External-Runtime Coordination Profile

Use this profile when a section is promoted for coordination, but the real
runtime still lives elsewhere.

Good fits:

- art coordination over a sibling runtime
- legacy-runtime bridge sections
- temporary migration staging sections

## Apply these changes to `section-core/`

### `CODEX_START.md`

Make the current rule explicit about:

- not moving, deleting, or rewriting the external runtime without an explicit
  migration task
- reading root docs before touching bridge behavior
- reporting shared behavior to the true shared-contract section

### `SYSTEM.md`

Emphasize:

- coordination-base identity
- external runtime path or dependency
- bridge expectations
- separation between experiments and reusable shared behavior

### `PLAN.md`

Use watchpoints around:

- accidental migration by drift
- confusion between coordination docs and runtime ownership
- bridge changes that affect shared contracts

### `TASKS.md`

Expect task types such as:

- `#architecture`
- `#compatibility`
- `#prompts`
- `#curation`
- `#docs`

## Optional extra files

Consider adding:

- migration-decision note
- bridge-inventory note
- local runtime-path quick reference
