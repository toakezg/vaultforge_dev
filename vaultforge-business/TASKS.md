# Tasks

## Business Open Tasks

```tasks
not done
tag includes business
sort by priority 
```

____
## Nath's Tasks
```tasks
not done
tag includes nath
```
____
## Now

- [ ] ⏫ Record new business threads in `SIGN_UP.md` and business behavior changes in `CHANGELOG.md` #business #docs 🆔 business-thread-signup-review 🔁 every week when done 2026-04-13
- [x] 🔺 Hand engine-specific step 7 work to a dedicated engine thread instead of continuing it inside business #business #engine #nath 2026-04-13 ✅ 2026-04-13
- [x] Create starter business wrapper scripts #business #cli
- [x] Create business docs #business #docs
- [x] Create markdown prompt templates #business #prompts
- [x] Keep outputs separated from art playground output #business #routing
- [x] Complete business parity dry-run assessment against direct engine behavior #business #validation
- [x] Add prompt-bank inventory and maintenance boundaries #business #prompts
- [x] Add generated-output review summary helper #business #review
- [x] Build a markdown bank runner that reads frontmatter #business #prompts
- [x] Add generated dashboard note for Dataview #business #dashboard
- [x] Tighten business dry-run behavior so default dry-runs do not leave metadata fixtures #business #dry-run
- [x] Add real example markdown prompt notes under `my-prompts-bank` #business #prompts
- [x] Add contact sheet generation #business #gallery
- [x] Add HTML gallery from `gallery-entry.json` #business #gallery
- [x] Add prompt-bank status update helpers #business #prompts
- [x] Archive duplicate manual one-off prompt templates #business #prompts

## Next

- [x] Retarget `run_business.ps1` to call `vaultforge-engine\src\generate.py` directly after a tiny retarget pass #business #engine
- [x] 🔼 Add additional real client prompt notes under `my-prompts-bank` once reusable client packs are ready #business #prompts 2026-04-15 ✅ 2026-04-15
- [x] ⏫ Pass native engine `--client`, `--job`, `--tag`, and `--variants` through `run_business.ps1` while keeping business routing and prompt composition stable #business #engine #integration 🆔 business-engine-native-metadata-adoption ✅ 2026-05-09
- [x] ⏫ Validate backward compatibility for the current business wrappers during the native metadata integration pass #business #validation 🆔 business-wrapper-backcompat ⛔ business-engine-native-metadata-adoption ✅ 2026-05-09
- [x] 🔼 Review whether business should keep authoritative `run.json` and `gallery-entry.json` files or merge engine sidecar metadata during the native metadata pass #business #planning 🆔 business-manifest-contract-review ⛔ business-engine-native-metadata-adoption ✅ 2026-05-09
- [x] 🔽 Fix or decide the `run-client-pack.ps1 -WhatIf` logging side effect so preview commands do not append `logs/run-log.csv` rows unless that is explicitly wanted #business #cli #dry-run 🆔 business-pack-whatif-log-side-effect ✅ 2026-05-09
- [x] 🔼 Pass `-InputImage` through to the engine once shared edit plumbing exists #business #engine #api 🆔 business-input-image-support ⛔ engine-input-image-plumbing ✅ 2026-05-09
- [x] 🔼 Pass `-ReferenceImage` through to the engine once the shared reference-image contract exists #business #engine #api 🆔 business-reference-image-support ⛔ engine-reference-image-plumbing ✅ 2026-05-09
- [x] 🔼 Prepare a business-owned preset/style/mod fragment candidate review before any engine-library migration #business #engine #libraries #planning 🆔 business-fragment-library-candidates ⛔ business-wrapper-backcompat ✅ 2026-05-09
- [x] 🔼 Decide engine/business ownership and registry shape before moving stable business preset/style/mod fragments into engine libraries #business #engine #libraries #nath 🆔 business-fragment-library-ownership-gate ⛔ business-fragment-library-candidates ✅ 2026-05-10
- [x] 🔼 Move stable business preset/style/mod fragments into engine libraries after the registry shape is approved #business #engine #libraries 🆔 business-fragment-library-move ⛔ business-fragment-library-ownership-gate ✅ 2026-05-10
- [x] 🔼 Define what makes VaultForge Business finished and primed for real client use before building paid-service packaging #business #planning 🆔 business-client-ready-definition ✅ 2026-05-09
- [x] 🔼 Add a repeatable client intake markdown template for paid-service style requests #business #clients #prompts 🆔 business-client-intake-template ⛔ business-client-ready-definition ✅ 2026-05-09
- [x] 🔼 Add a delivery package skeleton with export folders and a client-facing README template #business #packaging 🆔 business-client-package-skeleton ⛔ business-client-ready-definition ✅ 2026-05-09
- [x] 🔼 Create a preset/style/mod service catalog from current business wrapper names and prompt-bank usage #business #docs #clients 🆔 business-service-catalog ⛔ business-client-ready-definition ✅ 2026-05-09
- [x] 🔼 Add a client-ready output review checklist for gallery/contact-sheet selection #business #review #packaging 🆔 business-client-output-review-checklist ⛔ business-client-ready-definition ✅ 2026-05-09
- [x] 🔼 Prepare Nath-facing pricing, licensing, publication, and paid-service launch decision note #business #planning #nath 🆔 business-paid-launch-decision-gate ⛔ business-service-catalog ✅ 2026-05-10

____
## All Tasks
```tasks
not done
```
___

## Working Rules

- Tag every task with at least one section tag and one task-type tag, for example `#business #docs` or `#business #gallery`.
- Set priority by business-local importance using Tasks markers: 🔺 highest, ⏫ high, 🔼 medium, 🔽 low, ⏬ lowest. Leave no marker only for unranked inbox or backlog tasks.
- Give active and next tasks a short stable `🆔` id so dependency chains can stay readable.
- Use `🔁` only for genuine recurring work, preferably with `when done` for review or maintenance loops.
- Use `⛔ task-id` for `before this` dependencies. Treat `after this` as the reverse link: give the current task a `🆔`, then point the follow-up task at it with `⛔`.
- Hold `due`, `scheduled`, `start`, and `created` until a later planning pass.
- Keep the automatic business `tasks` query above manual task sections so open business work self-populates.
