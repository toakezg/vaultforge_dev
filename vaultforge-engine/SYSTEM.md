# System

## Role

This folder is the stable shared generation core for VaultForge.

It should be boring, reusable, tested, and lane-neutral.

It is also a promoted section in the root/section thread model. Engine threads should read root context first, then work from this folder.

## Boundaries

- Engine code belongs here when both art and business would need it.
- Art experiments belong in `vaultforge-art`.
- Business/client workflow belongs in `vaultforge-business`.
- Do not move dirty sibling code here by rename until the copy has been verified.
- Keep Windows-first launchers and dry-run behavior in scope.
- Update `CHANGELOG.md` for engine changes and root `CHANGELOG.md` for cross-lane contract changes.
- Use `SIGN_UP.md` so dedicated engine threads can leave a compact role/handoff trace.
- Every engine task line must include at least one section tag and one task-type tag, for example `#engine #docs`, `#engine #tests`, or `#engine #api`.
- Active and next engine tasks should use Obsidian Tasks priority markers by engine-local importance: 🔺 highest, ⏫ high, 🔼 medium, 🔽 low, ⏬ lowest. Leave no marker only for unranked inbox or backlog tasks.
- Active and next engine tasks should also carry a short stable `🆔` id so `before this` and `after this` links stay usable.
- Use `🔁` only for genuine recurring work. Prefer `when done` for recurring maintenance or review loops.
- Use `⛔ task-id` for `before this` dependencies, and express `after this` by linking the follow-up task back to the current task's `🆔`.
- Hold `due`, `scheduled`, `start`, and `created` for a later rules pass.
- `TASKS.md` should keep an automatic `tasks` code block filtered with `tag includes engine` above manual task sections.

## Engine Owns

- CLI parser and config-file argument support
- prompt composition
- batch loading and state tracking
- markdown prompt cleanup
- named preset/style/mod registries when they are shared
- output naming and metadata helpers
- native `--client`, `--job`, `--tag`, and `--variants` primitives
- OpenAI image request plumbing
- future image edit/reference input primitives

## Engine Does Not Own

- client delivery folder conventions
- Dataview dashboards
- experimental art prompt packs
- business-only templates
- playground curation notes
- lane-specific prompt injection for client, job, tag, tweak, or reference context
