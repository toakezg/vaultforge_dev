# SYSTEM

## Purpose

This workspace is the VaultForge vault factory and workflow hub.

It exists to keep reusable vault assets, launchers, notes, and pipeline helpers together so new work can start from a clean and documented base.

Root also acts as the overhead coordinator for dedicated section threads.

## Operating Principles

- Keep the vault-side layer lightweight and note-friendly.
- Prefer thin wrappers over duplicated engines.
- Store prompt notes and planning notes in plain Markdown.
- Keep outputs local to the vault when that improves review and reuse.
- Treat sibling projects as dependencies when they already solve the heavy part of the workflow.
- Avoid baking domain-specific assumptions into every workflow unless they are clearly useful.
- Use root for coordination and section folders for focused worker tasks.
- Keep cross-section handoffs visible in `THREAD_MAP.md`, section changelogs, and root `CHANGELOG.md` when needed.

## Integration Rules

- Vault creation behavior lives in the root `.bat` launchers and `_template/`.
- Documentation and planning live in root Markdown notes.
- `THREAD_MAP.md` decides which section should own a task.
- Reusable prompt banks and output folders live under purpose-named folders such as `ICON/`.
- Shared reusable generation code now lives in `vaultforge-engine`.
- Some older/root wrappers may still delegate to the old art runtime/reference prototype at `F:\tools\image_generation\vaultforge-art` until each lane gets an explicit compatibility pass.
- Treat `vaultforge-art` as the art/playground lane, not the permanent shared engine.
- Treat `vaultforge-image` as the image-only lane for quick intake and
  lane-local outputs, not as a replacement for art or business.
- If a wrapper depends on another local project, the dependency path must be explicit and documented.

## Documentation Rules

- `PLAN.md` tracks direction, intent, tradeoffs, and watchpoints.
- `TASKS.md` tracks the actionable work pool.
- `CURRENT_STATE.md` records the current recovery snapshot for app UI/thread-list drift.
- `THREAD_MAP.md` maps thread roles, section ownership, and handoff rules.
- `CHANGELOG.md` records notable structural changes with newest entries first.
- `NOTE/` holds topic notes, implementation notes, and quick guides.
- `ICON/` holds icon-related prompt banks, generated outputs, and local assets.
- `CODEX_START.md` is the preferred boot note for new Codex threads.
- Promoted sections should keep their own `CODEX_START.md`, `SYSTEM.md`, `PLAN.md`, `TASKS.md`, `CHANGELOG.md`, and `SIGN_UP.md`.
- Every Markdown task line must include at least one section tag and one task-type tag, for example `#engine #docs`, `#business #gallery`, `#coding #api`, `#xp4l #planning`, `#art #architecture`, or `#root #threading`.
- Active and next tasks should use Obsidian Tasks priority markers by section-local importance: 🔺 highest, ⏫ high, 🔼 medium, 🔽 low, ⏬ lowest. Leave no marker only for unranked inbox or backlog tasks.
- Active and next tasks should also carry a short stable `🆔` id so `before this` and `after this` links stay usable across sections.
- Use `🔁` only for true recurring work. Prefer `when done` for recurring maintenance or review loops.
- Use `⛔ task-id` for `before this` dependencies, and express `after this` by linking the follow-up task back to the current task's `🆔`.
- Hold `due`, `scheduled`, `start`, and `created` for a later rules pass.
- Each promoted section `TASKS.md` should include a `tasks` code block above manual active/next sections, filtered by that section tag, so open work self-populates without manual copying.

## Root And Section Model

- Root is the coordinator and architect.
- `vaultforge-engine` is the shared generator contract section.
- `vaultforge-business` is the client/business workflow section.
- `vaultforge-coding` is the local-first coding bridge section.
- `vaultforge-xp4l` is the XP4Life interpretation and progression section.
- `vaultforge-image` is the lightweight image lane for prompt intake, thin
  wrappers, and lane-local outputs.
- `vaultforge-art` is the art/playground coordination section; its runtime worktree is still a sibling dependency until an explicit migration task changes that.
- `vaultforge-icon` is the icon workflow section; it owns icon notes, icon review, and the existing `svg-forge` subtool.
- Parked folders such as `vaultforge-core`, `vaultforge-design`, `vaultforge-system`, and `vaultforge-init` are not active thread bases until root promotes them.

## Current Design Decision

XP4Life Icons Part A is implemented here as a vault-local prompt bank plus a launcher batch file.

That launcher currently calls the existing sibling `vaultforge-art` Python generator with:

- prompt folders from this vault
- output folders in this vault
- the existing `icon` preset and compatible style flags from the art project

That keeps the workflow local and reusable without forking the image engine. Future wrapper changes should move toward `vaultforge-engine` only through explicit dry-run compatibility passes.
