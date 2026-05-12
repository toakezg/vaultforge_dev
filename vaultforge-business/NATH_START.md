[[]]# NATH START - VaultForge Business

This is the quick start note for using the `vaultforge-business` lane.

VaultForge Business is the client-facing brand-asset lane. It turns client or
project briefs into reusable prompt notes, routed generation runs, review
surfaces, and delivery-package folders without mixing business work into the art
playground.

## First Read

For a fresh business-lane thread, read in this order:

1. `..\CODEX_START.md`
2. `..\CURRENT_STATE.md`
3. `..\THREAD_MAP.md`
4. `CODEX_START.md`
5. `README.md`
6. `SYSTEM.md`
7. `PLAN.md`
8. `TASKS.md`
9. `CHANGELOG.md`
10. `SIGN_UP.md`
11. `BUSINESS_CLIENT_READY_CRITERIA.md`
12. `my-prompts-bank\README.md`

Use `THREAD_MAP.md` before touching anything that might belong to root,
`vaultforge-engine`, `vaultforge-art`, or another lane.

## What This Lane Does

VaultForge Business currently handles:

- client and project intake notes
- markdown prompt-bank workflows
- business wrapper commands around the shared engine
- client, asset, job, preset, style, mod, and tag metadata
- business-owned `run.json` and `gallery-entry.json` manifests
- generated-output review summaries
- contact sheets and HTML gallery surfaces
- prompt note status/rating/image updates
- client delivery package skeletons
- operator-facing service catalog and output review checklist

The shared image generation engine lives in `..\vaultforge-engine`. Business
keeps the client workflow, prompt context, routing, review, and packaging
surface here.

## Main Files And Folders

Use these as the lane map:

- `README.md` - operator guide and command examples.
- `SYSTEM.md` - business ownership, naming, presets, styles, mods, and manifest rules.
- `PLAN.md` - current phase map and completed milestones.
- `TASKS.md` - active and next business work.
- `SIGN_UP.md` - compact handoff trace for business threads.
- `my-prompts-bank\` - reusable markdown prompt notes and intake templates.
- `my-prompts-bank\_intake\client-intake-template.md` - non-runnable client brief template.
- `delivery-package-template\` - client delivery folder skeleton.
- `generated\` - local generated outputs, review surfaces, gallery, and contact sheets.
- `logs\run-log.csv` - pack-runner execution log when runs intentionally log.
- `BUSINESS_CLIENT_READY_CRITERIA.md` - definition of client-ready.
- `BUSINESS_SERVICE_CATALOG.md` - internal preset/style/mod service menu.
- `BUSINESS_OUTPUT_REVIEW_CHECKLIST.md` - selection and packaging checklist.
- `BUSINESS_PAID_LAUNCH_DECISION_NOTE.md` - Nath-facing launch decision surface.
- `BUSINESS_FRAGMENT_LIBRARY_CANDIDATES.md` - business-owned fragment migration review and gate.

## Main Tools

Use batch files for normal Windows operation. Use PowerShell scripts when you
need exact switches or review-safe checks.

- `run_business.bat` / `run_business.ps1` - run or preview one business prompt.
- `run_business_md_bank.bat` / `run_business_md_bank.ps1` - run or preview markdown prompt-bank notes.
- `run-client-pack.bat` / `run-client-pack.ps1` - run root text or JSON prompt packs.
- `run_business_smoke.bat` - safe smoke dry-run.
- `build-review-summary.bat` - build `generated\_review\business-summary.md`.
- `build-contact-sheets.bat` - build contact sheets beside generated runs.
- `build-gallery.bat` - build `generated\_gallery\index.html`.
- `update-prompt-note.bat` - update prompt-bank status, image, rating, and notes.

## Safe Examples

Preview one direct business prompt without calling the engine:

```powershell
.\run_business.ps1 -Prompt "Clean local service logo with simple symbol" -Client "demo-client" -AssetType "logo" -Job "first-pass" -Tag "local,premium" -WhatIf
```

Run the smoke dry-run:

```bat
run_business_smoke.bat
```

Preview the markdown prompt bank without generation:

```bat
run_business_md_bank.bat -Path ".\my-prompts-bank" -IncludeTemplates -WhatIf -Limit 1
```

Preview all runnable prompt-bank notes with three generated variants each:

```bat
run_business_md_bank.bat -Path ".\my-prompts-bank" -All -WhatIf -VariantsOverride 3
```

Dry-run draft markdown notes without business metadata fixtures:

```bat
run_business_md_bank.bat -Path ".\my-prompts-bank" -DryRun
```

Keep dry-run metadata fixtures only when you intentionally need them:

```bat
run_business_md_bank.bat -Path ".\my-prompts-bank" -DryRun -WriteMetadata
```

Preview a root pack without appending `logs\run-log.csv`:

```powershell
powershell -ExecutionPolicy Bypass -File .\run-client-pack.ps1 -InputValue "Demo Client" -Client "demo-client" -Project "logo-pack-01" -Tag "round1" -PromptFile ".\logo-pack.txt" -WhatIf
```

Build review surfaces from existing generated outputs:

```bat
build-review-summary.bat -OutFile ".\generated\_review\business-summary.md"
build-contact-sheets.bat -GeneratedRoot ".\generated"
build-gallery.bat -GeneratedRoot ".\generated"
```

Update a prompt note after review:

```bat
update-prompt-note.bat -PromptPath ".\my-prompts-bank\example-client\logo-01.md" -Status review -Rating 8 -Notes "strong option"
```

## Normal Client Workflow

1. Capture the request in `my-prompts-bank\_intake\client-intake-template.md`.
2. Convert the useful parts into one or more runnable prompt notes under a
   client folder in `my-prompts-bank`.
3. Preview with `run_business_md_bank.bat -WhatIf`.
4. Use `-DryRun` before any live generation when checking routing or metadata.
5. Review outputs through `business-summary.md`, contact sheets, gallery, and
   `BUSINESS_OUTPUT_REVIEW_CHECKLIST.md`.
6. Copy selected, reviewed files into a copy of `delivery-package-template`.
7. Keep prompts, manifests, sidecars, and references in the package `sources`
   folders for reproducibility.

## Current Hard Gates

Stop and ask Nath/root/engine before:

- pricing or public paid-service launch decisions
- licensing, terms, trademark, or commercial-use claims
- live generation when external API use or cost is not explicitly approved
- moving business presets, styles, or mods into shared engine registries
- changing cross-lane ownership, shared engine behavior, or output contracts
- deleting or moving generated assets or source prompt-bank files

## Future Work

Likely next improvements:

- One approved private pilot/demo package after Nath chooses the launch posture,
  pricing shape, publication channel, and live generation budget.
- More reviewed examples for low-evidence catalog entries such as `wordmark`, `badge-emblem`, `luxury-minimal`, and `neon-signage`.
- A clearer prompt-pack folder only after pack-runner compatibility is updated.
- More automated package assembly after the manual delivery skeleton proves stable.
- Shared fragment registry work only after root and engine approve the ownership shape.

## Standard Handoff

Before leaving a business thread:

1. Update `SIGN_UP.md` with role, scope, read files, changes, and handoff.
2. Update `CHANGELOG.md` for business behavior or doc changes.
3. Keep root docs untouched unless the change affects cross-lane coordination.
4. Record verification commands and whether live generation was avoided.
5. Leave the next safe resume prompt in `SIGN_UP.md` when work is not finished.
