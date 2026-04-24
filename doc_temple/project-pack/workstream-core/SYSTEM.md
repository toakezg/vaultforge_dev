# SYSTEM

## Role

This folder is `{workstream_role}` for `{project_name}`.

It is an active workstream in the root-and-workstreams model.

## Boundaries

This workstream owns:

- `{workstream_owns}`

This workstream does not own:

- `{workstream_does_not_own}`

Related or dependent workstreams to respect:

- `{related_workstreams}`

External dependency path, if applicable:

- `{external_dependency_path_optional}`

## Rules

- keep this workstream focused on its lane role
- use root startup docs before deep local work
- `{cross_stream_reporting_rule}`
- update local `CHANGELOG.md` for workstream changes
- update root `CHANGELOG.md` when the change affects shared contracts,
  architecture, or routing
- keep `SIGN_UP.md` usable as a short thread trace
- tag every task with at least one workstream tag and one task-type tag
- use local priority markers for active and next tasks
- give active and next tasks stable ids when dependency chains matter
- use recurrence markers only for genuine recurring work
- keep an automatic `tasks` query above manual task sections if you use it
