# Art System

## Role

`vaultforge-art` is the active art lane for VaultForge.

It is the home for art-focused prompt work, playful image generation, inbox-driven batch runs, and art output curation.

## Boundaries

- Shared generator behavior lives in `vaultforge-engine`.
- Client/business workflow stays in `vaultforge-business`.
- `run_art.bat` is the lane wrapper and should stay thin.
- `ART_KEY` is the lane-owned key path for art runs.
- Direct prompts and inbox batch prompts both belong in this lane.
- Local output routing should stay in `output\` unless a run overrides it.

## Rules

- Do not rebuild the shared engine here.
- Do not move art-specific behavior into business or icon lanes.
- Report shared-behavior needs to engine instead of cloning new engine logic.
- Keep `CHANGELOG.md` for lane changes and root `CHANGELOG.md` for cross-lane coordination.
- Every art task line must include at least one section tag and one task-type tag, for example `#art #docs`, `#art #architecture`, or `#art #prompts`.
- Active and next art tasks should use Obsidian Tasks priority markers by art-local importance: 🔺 highest, ⏫ high, 🔼 medium, 🔽 low, ⏬ lowest. Leave no marker only for unranked inbox or backlog tasks.
- Active and next art tasks should also carry a short stable `🆔` id so `before this` and `after this` links stay usable.
- Use `🔁` only for true recurring work. Prefer `when done` for recurring maintenance or review loops.
- Use `⛔ task-id` for `before this` dependencies, and express `after this` by linking the follow-up task back to the current task's `🆔`.
- Hold `due`, `scheduled`, `start`, and `created` for a later rules pass.
- `TASKS.md` should keep an automatic `tasks` code block above manual active/next sections, filtered by `#art`.
- Keep prompt files in `inbox\` and generated images in `output\`.
