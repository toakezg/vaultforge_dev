# System

## Role

This folder is `{section_role}` for `{project_name}`.

It is a promoted section in the root-and-sections thread model.

## Boundaries

This section owns:

- `{section_owns}`

This section does not own:

- `{section_does_not_own}`

Upstream or sibling sections to respect:

- `{upstream_sections}`

External runtime or dependency path, if applicable:

- `{external_runtime_path_optional}`

## Rules

- keep this section focused on its lane role
- use root startup docs before section work
- `{cross_lane_reporting_rule}`
- update local `CHANGELOG.md` for section changes
- update root `CHANGELOG.md` when the change affects coordination or shared
  contracts
- keep `SIGN_UP.md` usable as a short thread trace
- tag every task with at least one section tag and one task-type tag
- use section-local priority markers for active and next tasks
- give active and next tasks stable ids when dependency chains matter
- use recurrence markers only for genuine recurring work
- keep an automatic `tasks` query above manual task sections
