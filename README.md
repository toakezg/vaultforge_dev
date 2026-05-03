# VaultForge

VaultForge is the vault-side control layer for reusable Obsidian workflows.

It now uses a root/section thread model:

- root `vaultforge\` = overhead coordination, architecture, and handoffs
- `vaultforge-engine\` = shared generation machinery and contracts
- `vaultforge-business\` = client/business workflow lane
- `vaultforge-coding\` = local-first code bridge and API-driven coding lane
- `vaultforge-xp4l\` = XP4Life interpretation and progression lane
- `vaultforge-art\` = planned fresh art lane, with the old runtime/reference prototype being harvested from `F:\tools\image_generation\vaultforge-art`

This workspace currently does six useful things:

- keeps vault creation and launcher scripts in one place
- stores reusable notes and planning docs for future Codex threads
- hosts local pipeline wrappers that can hand work off to sibling tools such as the old art runtime/reference prototype at `F:\tools\image_generation\vaultforge-art`
- hosts the first shared generation prototype under `vaultforge-engine`
- carries the first dedicated code-automation bridge section under
  `vaultforge-coding`
- carries the first dedicated XP4Life interpretation section under
  `vaultforge-xp4l`

## Engine Direction

VaultForge is moving toward a cleaner split:

- `vaultforge-engine` = stable shared generation core
- `vaultforge-art` = art-facing and experimental lane
- `vaultforge-business` = business and client-facing lane

The first shared engine prototype now lives at `vaultforge-engine\src\generate.py`.
`vaultforge-business` targets that shared engine directly. Some older/root
wrappers, including the XP4Life icon launcher, still call the sibling
`F:\tools\image_generation\vaultforge-art` generator until they get their own
explicit compatibility pass. See `ARCHITECTURE - engine extraction.md`.

## Key Docs

- `SYSTEM.md` explains how this workspace is meant to operate
- `CURRENT_STATE.md` is the quick recovery anchor when Codex app project/thread visibility gets confusing
- `PLAN.md` tracks the current direction
- `TASKS.md` holds the active work pool
- `THREAD_MAP.md` tells new threads which section should own a task
- `CHANGELOG.md` records notable structural changes
- `CODEX_START.md` gives new Codex threads a clean boot sequence

## XP4Life Icons Part A

The first implemented design lane is an XP4Life icon pipeline.

- reference note: `NOTE/Icons - part A.md`
- attack plan: `NOTE/Icons - part A - todo.md`
- quick guide: `NOTE/Icons - part A - quick use guide.md`
- Obsidian use guide: `NOTE/How to - Create XP4Life Icon set (obsidian).md`
- first output review: `NOTE/Icons - part A - output review.md`
- prompt bank: `ICON/XP4Life/part-a/prompts/`
- launcher: `run-icons-part-a.bat`

The image engine is not duplicated in the XP4Life lane. This root launcher still
delegates to the existing Python generator in
`F:\tools\image_generation\vaultforge-art`.

## Quick Start

Dry-run the full prompt bank:

```bat
run-icons-part-a.bat --dry-run
```

Run only quests:

```bat
run-icons-part-a.bat quests
```

Generated files land in:

```text
ICON\XP4Life\part-a\generated\
```

## VaultForge Icons Branch

The broader client/logo-pack idea is captured in:

```text
NOTE\VaultForge Icons - branch plan.md
```

Supporting draft references live in `Reference/`.

## Section Threading

New dedicated threads should start at root, use `THREAD_MAP.md` to choose the correct section, then read that section's `CODEX_START.md`, `SYSTEM.md`, `PLAN.md`, `TASKS.md`, `CHANGELOG.md`, and `SIGN_UP.md`.

Section threads should update their own changelog first. Root `CHANGELOG.md` is for cross-lane or coordination-level changes.
