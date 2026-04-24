# Delivery-Lane Profile

Use this profile when a workstream is a workflow lane for prompts, outputs,
review surfaces, content handling, delivery helpers, or operator-facing logic.

Good fits:

- production lanes
- review lanes
- output handling
- prompt or wrapper layers

## Apply these changes to `workstream-core/`

### `CODEX_START.md`

Make the current rule explicit about:

- keeping the lane thin and workflow-oriented where practical
- not duplicating shared platform logic locally
- reporting stable shared needs upward when they emerge

### `SYSTEM.md`

Emphasize:

- wrappers
- routing
- review surfaces
- operator-facing naming or conventions
- local delivery rules

State clearly what stays lane-owned versus what should move into shared
platforms later.

### `PLAN.md`

Use direction bullets around:

- ownership
- flow clarity
- routing and metadata
- future extraction of stable shared pieces

### `TASKS.md`

Expect task types such as:

- `#prompts`
- `#routing`
- `#review`
- `#outputs`
- `#workflow`

## Optional extra files

Consider adding:

- a local `README.md`
- naming rules note
- quick-run note
- review checklist
