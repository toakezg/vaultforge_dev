# Changelog

## 2026-05-10

- Adopted the approved engine registry shape in the business wrapper: selected
  business preset/style aliases now pass directly to the engine, approved
  production modifiers pass as native `--constraint` values, and remaining
  brand-tone modifiers stay business-owned prompt context.
- Added `BUSINESS_PAID_LAUNCH_DECISION_NOTE.md` as the Nath-facing decision
  surface for service positioning, pricing shape, licensing wording,
  publication channel, pilot/live generation scope, revision policy, and
  example/privacy choices without approving launch by default.
- Added `NATH_START.md` as the business-lane operator start note with read
  order, feature map, safe examples, hard gates, standard handoff guidance, and
  future work.
- Updated the business README and Obsidian MOC stub to point new business-lane
  work at the new start note and current operator surfaces.
- Replaced the stale missing `catch-up-here.txt` startup reference in
  `CODEX_START.md` with `NATH_START.md` and fixed the visible `-WWhatIf`
  typo in `client-pack-readme.txt`.

## 2026-05-09

- Added `BUSINESS_OUTPUT_REVIEW_CHECKLIST.md` to define the curation path from
  gallery/contact-sheet review into selected, rejected, archived, and packaged
  client-ready files.
- Added `BUSINESS_SERVICE_CATALOG.md` as an internal preset/style/mod service
  menu from current wrapper names and prompt-bank usage, while keeping pricing,
  licensing, publication, live generation, and engine registry changes gated.
- Added `delivery-package-template\` with export, preview, source, review,
  archive, and usage-note folders plus a client-facing README template for
  reviewed business delivery packages.
- Added `my-prompts-bank\_intake\client-intake-template.md` as a non-runnable
  client brief template for converting service-style requests into later
  runnable business prompt notes.
- Added `BUSINESS_CLIENT_READY_CRITERIA.md` to define the business lane's paid-client readiness target and split the next safe packaging/intake/catalog slices from Nath-gated launch decisions.
- Added `BUSINESS_FRAGMENT_LIBRARY_CANDIDATES.md` to review business preset/style/mod migration candidates and record the hard gate before moving lane-owned fragments into shared engine libraries.
- Fixed `run-client-pack.ps1 -WhatIf` so pack previews no longer create or append `logs/run-log.csv` by default; added `-LogWhatIf` for intentional preview audit rows.
- Recorded the manifest ownership decision after native metadata adoption: business `run.json` and `gallery-entry.json` stay authoritative for client/job/gallery review, while engine image sidecars remain per-image technical provenance.
- Passed business `-InputImage` and `-ReferenceImage` through to the shared engine's native `--input-image` and `--reference-image` flags now that the engine exposes them, resolving relative paths before the engine call.
- Passed native engine `--client`, `--job`, `--tag`, and `--variants` through `run_business.ps1` while preserving business output routing, prompt composition, and wrapper-owned `run.json` / `gallery-entry.json` manifests.
- Switched the business wrappers' default engine root from the stale fixed `E:\tools\vaultforge\vaultforge-engine` path to the sibling `..\vaultforge-engine` path, while keeping `-EngineRoot` and `-ArtRoot` overrides available.
- Verified the business wrapper path with PowerShell parser checks, direct `-WhatIf`, direct `-DryRun`, smoke batch dry-run, markdown-bank `-WhatIf`, and pack-runner `-WhatIf`.

## 2026-04-16

- Reviewed the business open-task queue against root and engine docs so the remaining business integration work matches the actual shared-engine state.
- Replaced the stale business blocker on completed engine metadata work with a ready wrapper-adoption task for native engine `--client`, `--job`, `--tag`, and `--variants`.
- Clarified in business planning that `--tweak` remains wrapper-owned prompt context for now, while `-InputImage` and `-ReferenceImage` stay blocked on shared engine API plumbing.
- Added a follow-up task to review whether business should keep authoritative `run.json` and `gallery-entry.json` files or merge engine sidecar metadata during the native metadata pass.
- Added the business task-property rule: active and next tasks now carry stable `🆔` ids, recurring loops should use `🔁`, and dependencies should use `⛔`.
- Linked current business integration tasks to the engine work they depend on so the lane can see blocked versus ready work more clearly.

## 2026-04-15

- Added `my-prompts-bank\vaultforge` as a runnable system-brand prompt pack generated from the existing VaultForge company brief.
- Added the first real client markdown prompt-bank folders under `my-prompts-bank\empower-you-plan-management` and `my-prompts-bank\jubal`.
- Added reusable `client-pack`, `logo`, `icon`, `cover`, and `brand-board` notes for real business clients so the markdown bank is no longer limited to `example-client`.
- Updated prompt-bank inventory notes, business sign-up, and task tracking to reflect reusable real client packs being ready.

## 2026-04-14

- Added the business open-task query block so `TASKS.md` self-populates not-done business tasks.

## 2026-04-13

- Added the business-local task priority rule and marked current open business tasks with Obsidian Tasks priority markers.
- Hard-set the business task tag rule and tagged existing business task lines with section and task-type tags.
- Added the business section to the root/section thread model.
- Updated business startup docs so dedicated business threads read root overhead context before lane-specific docs.
- Added `SIGN_UP.md` as the business thread sign-in and handoff trace.
- Tightened `run_business.ps1` dry-run behavior: plain `-DryRun` no longer writes business metadata or workspace output folders, `-DryRun -WriteMetadata` keeps fixture metadata, and `-WhatIf` previews engine commands without calling the engine.
- Added markdown-bank `-WriteMetadata` pass-through for deliberate dry-run fixture creation.
- Added the first runnable markdown example pack under `my-prompts-bank\example-client`.
- Added contact-sheet generation from `gallery-entry.json` run folders.
- Added an HTML gallery builder that writes `generated\_gallery\index.html`.
- Added a prompt-note updater for `status`, `image`, `rating`, and `notes` frontmatter.
- Archived duplicate manual one-off plumber prompts under `my-prompts-bank\_archive\legacy-one-offs`.
- Recorded engine-native business flags as a later dedicated engine pass in the 1-7 tracking note.
- Added `run_business_md_bank.ps1` and `run_business_md_bank.bat` for markdown prompt-bank execution.
- Added simple frontmatter parsing for business prompt notes, with status filtering, template skipping, dry-run support, and source note preservation.
- Added comma-separated style/mod normalization in `run_business.ps1` so batch-spawned markdown runs can pass multiple values reliably.
- Added markdown-bank guards so directory runs skip non-prompt notes such as READMEs and dashboards.
- Added `SourcePromptFile` support to the business wrapper so runs can save `prompt.source.md`.
- Added a starter Dataview dashboard note for prompt queue, review, client grouping, style signals, and image-field browsing.
- Updated business docs, plan, and tasks to reflect the markdown bank runner landing while keeping the existing text-pack runner intact.

## 2026-04-11

- Added the first VaultForge Business wrapper lane.
- Added separate business output routing under `generated`.
- Added metadata files for each run.
- Added starter docs and markdown prompt templates.
- Added dry-run smoke runner.
