# Business Prompt Bank

This folder is the intended home for reusable business prompt notes. Keep this
bank lane-owned: it can describe clients, asset goals, presets, styles, mods,
tags, and review notes, but it should not change shared engine behavior.

## Current Inventory

### Runnable text packs

These files live at the `vaultforge-business` root because the current pack
runner accepts a plain text command file:

- `logo-pack.txt` - five logo directions.
- `icon-pack.txt` - five icon directions.
- `cover-pack.txt` - five cover/banner directions.
- `pack-dryrun-safe.txt` - one safe dry-run fixture for pack-runner checks.

Leave these filenames stable until the runner supports a configured pack folder.
`run-client-pack.ps1`, `run-client-pack.bat`, and `run_business_bank.bat` still
expect root-level text packs.

### Markdown prompt templates and runner

Reusable markdown prompt notes belong under `my-prompts-bank`. Current templates
are in `_template`:

- `logo-template.md`
- `icon-template.md`
- `cover-template.md`
- `brand-board-template.md`
- `client-pack-template.md`

The first runnable markdown example pack lives in `example-client`:

- `logo-01.md`
- `icon-01.md`
- `cover-01.md`
- `brand-board-01.md`

The first real client-ready markdown folders now live beside it:

- `empower-you-plan-management` - starter service-business pack with
  `client-pack`, `logo`, `icon`, `cover`, and `brand-board` notes.
- `jubal` - starter radio-show pack with `client-pack`, `logo`, `icon`, and
  `cover` notes.
- `vaultforge` - starter system-brand pack with `client-pack`, `logo`, `icon`,
  `cover`, and `brand-board` notes generated from the VaultForge company brief.

Use these as the canonical shape for prompt-bank entries. The markdown runner is
`run_business_md_bank.ps1`; it reads simple YAML frontmatter, skips `_template`
by default, ignores non-prompt markdown such as READMEs and dashboards, strips
the opening H1 from the prompt body, and passes the remaining body to
`run_business.ps1`.

Useful checks:

```powershell
.\run_business_md_bank.ps1 -Path ".\my-prompts-bank" -IncludeTemplates -WhatIf -Limit 1
.\run_business_md_bank.ps1 -Path ".\my-prompts-bank" -DryRun
.\run_business_md_bank.ps1 -Path ".\my-prompts-bank" -DryRun -WriteMetadata
```

The runner defaults to `status: draft`. Use `-All` when you intentionally want
to run notes with any status, or `-Status review` to target another queue.
Plain `-DryRun` does not write business metadata; add `-WriteMetadata` only when
you want dry-run fixture files in `generated`.

### Legacy one-off archive

Old manual scratch examples live in `_archive\legacy-one-offs`. Do not treat
them as canonical reusable bank entries.

## Naming Patterns

- Root executable packs use `{asset}-pack.txt`, for example `logo-pack.txt`.
- Safe fixtures use a purpose name, for example `pack-dryrun-safe.txt`.
- Markdown templates use `{asset}-template.md` inside `_template`.
- Future reusable markdown prompts should use a client or project folder plus a
  descriptive file name, for example `my-prompts-bank/example-client/logo-01.md`.
- Job names should stay short and sortable, for example `logo-pack-01` or
  `brand-board-01`.
- Use kebab-case for `client`, `asset_type`, and `job` values when possible.
- Keep `tags` as short YAML list items, for example `local` and
  `service-business`; the current runnable wrapper flattens tag context into a
  singular `-Tag` string.

## Category Boundaries

- Put runner-compatible command packs at the repo root only while the current
  runner requires them.
- Put reusable prompt-bank notes in `my-prompts-bank`.
- Put temporary manual experiments in a clearly temporary client scratch folder,
  not in the repo root.
- Keep generated outputs under `generated`; never backfill generated prompts
  into the source prompt bank without deliberate review.

## Cleanup Findings

- No exact duplicate commands were found across the three five-direction packs.
- `pack-dryrun-safe.txt` intentionally repeats the first `logo-pack.txt`
  direction with `-DryRun` for safe verification.
- The duplicate plumber prompt from the repo root and `prompt template` has been
  moved into `_archive\legacy-one-offs`.
- The main unclear boundary is that root `.txt` files currently mix executable
  pack files with manual one-off examples. New reusable prompts should go to the
  markdown bank instead of adding more root-level loose text files.

## Maintenance Rules

- Do not change pack preset/style/mod combinations during organization-only
  cleanup.
- Before adding a pack line, compare against `logo-pack.txt`, `icon-pack.txt`,
  and `cover-pack.txt` so near-duplicates are intentional.
- Keep frontmatter fields aligned with the wrapper contract:
  `client`, `asset_type`, `preset`, `styles`, `mods`, `tags`, `job`, `status`,
  `rating`, `image`, and `notes`.
- Do not add `*_slug` fields to prompt notes by hand. The wrapper computes
  slug fields in `run.json` and `gallery-entry.json` from the raw names.
- Prefer adding a new markdown prompt note over changing a proven runnable pack
  direction.
- Use `update-prompt-note.ps1` after review when you want to set `status`,
  `image`, `rating`, or `notes` without hand-editing frontmatter.

## Deferred Cleanup

- Build the planned markdown bank runner before moving root packs.
- Expand reviewed client-specific folders as more reusable packs are promoted
  out of scratch work.
- Consider a future `prompt-packs` folder only together with text-pack launcher
  updates, so existing commands keep working.
