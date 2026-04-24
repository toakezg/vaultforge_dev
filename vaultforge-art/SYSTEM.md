# Art System

## Role

This folder is the art/playground coordination base for VaultForge.

It exists so art-specific threads have a home under root overhead without moving the current sibling art runtime.

## Boundaries

- Current runtime art worktree: `E:\tools\image_generation\vaultforge-art`.
- Shared generator contracts belong in `vaultforge-engine`.
- Client/business workflow belongs in `vaultforge-business`.
- Art prompt experiments, playground presets, creative packs, and art curation belong with the art lane.

## Rules

- Do not treat messy art experiments as engine debt until both art and business need the behavior.
- Do not migrate the sibling art worktree into root without an explicit migration plan.
- Report shared behavior needs to engine instead of building a second engine here.
- Update `CHANGELOG.md` for art coordination changes and root `CHANGELOG.md` for cross-lane changes.
- Every art task line must include at least one section tag and one task-type tag, for example `#art #docs`, `#art #architecture`, or `#art #prompts`.
- Active and next art tasks should use Obsidian Tasks priority markers by art-local importance: 🔺 highest, ⏫ high, 🔼 medium, 🔽 low, ⏬ lowest. Leave no marker only for unranked inbox or backlog tasks.
- Active and next art tasks should also carry a short stable `🆔` id so `before this` and `after this` links stay usable.
- Use `🔁` only for genuine recurring work. Prefer `when done` for recurring maintenance or review loops.
- Use `⛔ task-id` for `before this` dependencies, and express `after this` by linking the follow-up task back to the current task's `🆔`.
- Hold `due`, `scheduled`, `start`, and `created` for a later rules pass.
- `TASKS.md` should keep an automatic `tasks` code block filtered with `tag includes art` above manual task sections.
