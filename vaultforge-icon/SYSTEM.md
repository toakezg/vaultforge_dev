# Icon System

## Role

This folder is the lightweight icon lane for VaultForge.

It exists to keep icon-specific notes, prompt plans, asset review, and small
helper tools together without turning the lane into a second engine.

## Boundaries

- Icon workflow coordination belongs here.
- Shared generation behavior belongs in `..\vaultforge-engine`.
- General art playground work belongs in `..\vaultforge-art`.
- Client/business packaging belongs in `..\vaultforge-business` unless the work
  is only an icon-lane proof or local icon pack.
- `svg-forge` is an existing subtool for raster-to-SVG conversion and should be
  validated or improved in place before any larger rewrite.

## Rules

- Keep this lane note-first and tool-light.
- Do not spend API money or run live generation unless a task explicitly allows
  it.
- Local file/folder writes are approved when the task explicitly scopes them
  and every written path stays inside the lane/write scope. Record the intended
  write scope before proceeding.
- Do not create generated artifacts or generated output folders unless the task
  explicitly approves those outputs by path.
- Do not move or delete existing assets unless Nath explicitly asks.
- Prefer dry-run validation and documented blockers over speculative rewrites.
- Treat build-note role and skill ideas as process prompts first; create real
  Codex skills only after repeated runs prove the workflow is stable.
- Keep optional creative roles bounded: they may propose directions after
  verified work, but they must not expand the active task without Coordinator
  selection.
- Treat one workflow cycle as one full ordered role rotation, such as
  Coordinator -> Builder -> Reviewer -> Recorder. A 7-cycle run means repeating
  that full rotation up to seven times; estimate whether the task is large
  enough before attempting all seven.
- A normal rotation may land the active task plus up to two small related
  additional tasks when they are docs-only, share the same lane scope, and do
  not trigger stop gates.
- When a review finds a future live/non-dry-run need, park it as
  `#live-required` and state the missing live run instead of stopping the whole
  run if approved dry-run or build work can continue safely.
- Use `#nath` only for hard gates: direction changes from the main icon
  generator goal, ownership changes, secrets/cloud permissions, paid/live work
  that cannot be deferred, asset moves/deletes, folder icon application, or real
  taste decisions.
- Scoped local writes inside an explicitly approved lane/write scope are not a
  hard gate by themselves. Secrets/cloud auth, paid/API work, asset moves or
  deletes, generated artifacts without path approval, folder-icon application,
  ownership changes, and taste decisions remain hard gates.
- Record icon-lane changes in `CHANGELOG.md`.
- Record new icon threads or handoffs in `SIGN_UP.md`.
- Add new `SIGN_UP.md` dated entries and new `CHANGELOG.md` entries above
  older entries so the newest state is easiest to find.
- Update root routing docs when icon-lane ownership changes.
- Every icon task line must include at least one section tag and one task-type
  tag, for example `#icon #docs`, `#icon #validation`, or `#icon #tools`.
- Any task that requires Nath to approve, decide, unblock, or step in at a hard
  gate must also include `#nath`.
- Any task that needs future non-dry-run validation must include
  `#live-required` and state the missing live run.
- Use `#approved` as the approval stamp for tasks Nath has explicitly cleared.
  Keep it as a separate tag with a space before the task id marker.
- Active and next icon tasks should use Obsidian Tasks priority markers by
  icon-local importance.
- Active and next icon tasks should carry a short stable `🆔` id.
- `TASKS.md` should keep an automatic `tasks` query filtered with
  `tag includes icon` above manual task sections.
