# {project_name} Thread Map

Date: YYYY-MM-DD

`{project_name}` uses a root-and-sections thread model.

Root is overhead coordination. Promoted sections are focused worker bases.

## Root Thread

Use root for:

- cross-lane planning
- architecture decisions
- section promotion or parking
- thread routing
- handoffs between sections
- high-level changelog updates

Read first:

- `CODEX_START.md`
- `README.md`
- `SYSTEM.md`
- `THREAD_MAP.md`
- `PLAN.md`
- `TASKS.md`
- `CHANGELOG.md`

Report changes to:

- `CHANGELOG.md`
- affected section changelogs when root changes a section contract

## Promoted Sections

Replace or extend the blocks below with real sections.

### `{section_name}`

Use `{section_name}` for:

- `{section_owns}`

Read first:

- `..\CODEX_START.md`
- `..\SYSTEM.md`
- `..\THREAD_MAP.md`
- `CODEX_START.md`
- `SYSTEM.md`
- `PLAN.md`
- `TASKS.md`
- `CHANGELOG.md`
- `SIGN_UP.md`

Report changes to:

- `{section_slug}\CHANGELOG.md`
- root `CHANGELOG.md` when the change affects coordination or shared contracts

## Parked Or Supporting Folders

List folders here that exist but are not promoted thread bases yet.

Promotion should mean:

- a clear section role
- a local six-file doc set
- a root thread-map update
