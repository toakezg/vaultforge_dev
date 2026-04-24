# Shared-Platform Profile

Use this profile when a workstream owns shared runtime pieces, contracts,
adapters, reusable utilities, or other lower-level foundations used elsewhere
in the project.

Good fits:

- core libraries
- shared APIs
- schema or contract layers
- reusable runtime helpers

## Apply these changes to `workstream-core/`

### `CODEX_START.md`

Make the current rule explicit about:

- protecting shared contracts
- checking downstream impact before changing foundations
- reporting breaking-shape changes upward

### `SYSTEM.md`

Emphasize:

- shared contracts
- reusable logic
- low-level adapters
- compatibility expectations

State clearly what this workstream owns versus what higher-level lanes should
keep locally.

### `PLAN.md`

Use direction bullets around:

- contract stability
- compatibility
- refactor safety
- migration planning

### `TASKS.md`

Expect task types such as:

- `#contracts`
- `#runtime`
- `#adapters`
- `#compat`
- `#refactor`

## Optional extra files

Consider adding:

- a local `README.md`
- compatibility note
- schema note
- migration note
