# Icon Sign Up

New icon threads should add a short entry here before or after their first
meaningful change.

Use this shape:

```text
## YYYY-MM-DD - thread label

- Role:
- Scope:
- Read:
- Changed:
- Handoff:
```

## Multi-Agent Handoff

- Task: Workflow B cycle 1 icon verification closure for run
  `20260510T005903-run-approved-section-local-build-slices-while-an`
- Current role: Builder -> Reviewer -> root recorder
- Last verified state:
  `icon-media-style-set-proposal` remains resolved as inactive/no-generation.
  `generated/proposals/inbox/media-style-guide-note.md` still marks the media
  style source as reference-only/inactive for proposal generation, and no media
  proposal output directory exists under `generated/proposals/`.
- Files touched:
  only `SIGN_UP.md` in this recorder update. Builder and reviewer made no
  icon-lane source changes in this cycle; the prior decision docs remain in
  place from the reviewed inactive/no-generation closure.
- Verification run:
  builder verified the media inbox note remained reference-only/inactive, no
  media/style proposal output directory existed, `run_icon_proposal.ps1` was
  not run, and `git status --short -- .` was clean from the icon lane. Reviewer
  checked the media note, status-gate decision, task/changelog/handoff/index
  records, `generated/proposals/` listings, recursive media/style output
  search, and confirmed `git diff -- vaultforge-icon` was empty before writing
  the run-packet review note.
- Blocker or decision:
  no hard gate was recorded for this verification cycle. Media styler stays
  inactive for proposal generation. No API/paid generation, generated proposal
  output folder, selected/applied output, asset move/delete, folder-icon
  application, staging, or commit happened in this cycle. The Gallable proposal
  selection task remains `#nath` and should not be taken without Nath's
  selection/taste decision.
- Resume prompt:
  Continue only with another approved safe icon slice. Do not switch into
  Gallable proposal selection unless Nath approves that decision. Do not run
  media-style proposal generation unless a future task explicitly makes the
  source active and approves generation.

## 2026-05-10 - Workflow B media style inactive decision

- Role: Builder
- Scope: record the decision that the media style guide stays inactive for
  proposal generation, without changing it to active or running generation
- Read: root coordinator routing, icon task/plan/changelog/handoff docs,
  `generated/proposals/inbox/media-style-guide-note.md`, the prior media-style
  status-gate decision, and the icon-set generation workflow contract
- Changed: updated the media-style status-gate decision note, marked
  `icon-media-style-set-proposal` landed as no-generation, and updated
  changelog/handoff records
- Handoff: reviewer should verify the source note is still reference-only, no
  `run_icon_proposal.ps1` command ran, no generated media proposal folder
  exists from this cycle, and all edits stayed inside the icon lane.

## 2026-05-09 - Workflow B icon builder gate fallback

- Role: Builder
- Scope: record the blocked media-style proposal gate, then complete the
  approved docs-only root-cooperative `$review-handoff-writer` fallback without
  creating a real skill file
- Read: root Workflow A/B guidance, icon task/plan/changelog/handoff docs,
  `generated/proposals/inbox/media-style-guide-note.md`, the icon-set workflow
  contract, and the prior skill-condition decision
- Changed: added the media-style status gate decision note, added
  `documents/contracts/REVIEW_HANDOFF_WRITER_ROOT_COOP_SPEC.md`, indexed both
  docs, marked the fallback task landed, and updated changelog/handoff records
- Handoff: media-style proposal generation remains blocked until the inbox note
  status is active. The handoff-writer spec is checklist-only; no skill,
  automation, API call, generated artifact, asset operation, folder-icon
  application, root rewrite, staging, or commit was performed.

## 2026-05-04 - Gallable proposal and scout checklist

- Role: Coordinator -> Scout -> Builder -> Reviewer -> Recorder, then
  Coordinator -> Builder -> Reviewer -> Recorder
- Scope: turn the Gallable inbox proposal into one generated proposal image,
  then continue into the approved directory-scout intake checklist task
- Read: root and icon workflow docs, icon task/plan/changelog/handoff docs, the
  Gallable inbox proposal and SVG, the media style note, the compatible
  filetypes reference, and the icon-set workflow contract
- Changed: added `generated/proposals/gallable-launcher-geometric-gallery/`
  with proposal/run/target/style docs, one prompt, one generated PNG, JSON
  metadata, and batch state; added
  `documents/contracts/DIRECTORY_SCOUT_PROPOSAL_INTAKE_CHECKLIST.md`; updated
  task, changelog, index, and handoff records
- Handoff: SVG was treated as reference-only because the current engine path is
  text-prompt based. Gallable output is ready for visual review; target-project
  writes, selection, reroll decisions, `.ico` build checks, and icon application
  remain separate tasks.

## 2026-05-04 - proposal inbox and icon-set workflow

- Role: Coordinator -> Builder -> Recorder
- Scope: set up an inbox for rough proposal ideas and define how directory or
  style-guide inputs can become generated icon sets
- Read: user style guide at `f:\media\icons\my_icons\style-guide.txt`, proposal
  output docs, apply-plan contract, current task board, and icon plan
- Changed: added `generated/proposals/inbox/README.md`, added
  `generated/proposals/inbox/media-style-guide-note.md`, added
  `documents/contracts/ICON_SET_GENERATION_WORKFLOW_CONTRACT.md`, and queued
  media-style proposal plus directory-scout checklist tasks
- Handoff: ideas can be dropped into `generated/proposals/inbox/`; future set
  runs can scout scoped directories, write descriptions, generate proposal
  images, and later hand off to apply-plan work. Folder-icon application remains
  separate.

## 2026-05-04 - lane env proposal retry

- Role: Builder -> Recorder
- Scope: let the icon lane use `vaultforge-icon\.env` for proposal generation
  while still delegating image generation to the shared engine
- Read: engine key contract, icon `.env` variable names without printing
  values, first proposal run log, and current proposal prompts
- Changed: added `run_icon_proposal.ps1`, reran the first proposal batch through
  the lane key, wrote three proposal images plus three metadata files, and
  marked the proposal task landed
- Handoff: use `run_icon_proposal.ps1` for future icon-lane proposal batches so
  `ICON_KEY` stays lane-local. Review/selection/application remain separate
  tasks.

## 2026-05-04 - first inspired-agent proposal attempt

- Role: Builder -> Recorder
- Scope: create the first inspired-agent proposal run under
  `generated/proposals/first-inspired-run/`, then dry-run and live-run the
  shared engine for three proposal images using the existing key mapping only
- Read: build-note agent roles and cycle notes, the SVG-Forge and Build Notes
  manual briefs, the inspired-agent proposal decision, engine CLI help, and
  current icon lane task/plan/handoff docs
- Changed: added `PROPOSAL.md`, `RUN_LOG.md`, three prompt files, and an
  `images/` output folder; updated task, changelog, plan, and handoff records
- Handoff: clean dry-run passed, key presence was confirmed without printing
  the key, and the live run was blocked by missing `api.responses.write` scope;
  no images or metadata were generated.

## 2026-05-04 - cleanup and proposal readiness

- Role: Coordinator -> Explorer -> Builder -> Recorder
- Scope: record Nath's clarifications, clean icon root doc sprawl, mark Part A
  as reference-only, and approve the proposal-document output home
- Read: icon task/plan/handoff docs, root workflow docs, Part A notes,
  documents moved under `documents/`, and inspired-agent proposal guidance
- Changed: moved contracts/reviews/decisions under `documents/`, added
  `documents/README.md`, added `generated/proposals/README.md`, added
  `documents/decisions/INSPIRED_AGENT_PROPOSALS_DECISION.md`, updated Part A
  notes with reference-only warnings, revised `$review-handoff-writer`
  conditions for root-doc cooperation, and queued the first proposal-doc run
- Handoff: proposal Markdown, supporting metadata, generated proposal images,
  and run metadata may be written under `generated/proposals/`; selected/applied
  outputs, asset operations, folder-icon application, new cloud auth/secret
  printing, and final taste decisions remain gated.

## 2026-05-04 - skill-condition decision

- Role: Builder -> Recorder
- Scope: decide the two remaining docs-only skill-condition tasks without
  creating skills, scripts, artifacts, images, APIs, asset moves/deletes, or
  folder icons
- Read: root/icon routing docs, icon task/plan/changelog/handoff docs,
  build-note skill references, no-write transcript check, and recent smoke
  recording
- Changed: added `documents/decisions/ICON_SKILL_CONDITIONS_DECISION.md`, marked both skill
  condition tasks landed, and revised parked activation gates in `PLAN.md`
- Handoff: both candidates remain parked. `$review-handoff-writer` needs
  cross-lane reuse, missed-field pain, or Nath request before promotion.
  `$smoke-test-recorder` needs at least two more repeated checks across
  different cases, including one wrapper or no-write check.

## 2026-05-04 - SVG-Forge real-sample live smoke

- Role: Builder -> Recorder
- Scope: run the explicitly approved SVG-Forge sample/output smoke without API
  calls, AI image generation, folder-icon application, or asset move/delete
- Read: root/icon dirty worktree status, icon task/changelog/handoff docs,
  `documents/decisions/SVG_FORGE_REAL_SAMPLES_DECISION.md`, `svg-forge` docs, sample listings, and
  `tools\make_samples.py`
- Changed: generated `samples\icon-star.png`, `samples\logo-blocks.jpg`,
  `samples\glyph-bolt.webp`, generated `output\real-sample-smoke\*.svg` plus
  `svg-forge.log`, marked the live smoke task landed, and recorded command
  evidence in lane/subtool docs
- Handoff: both approved commands exited 0. SVG/log files are inspectable in
  `svg-forge\output\real-sample-smoke`; do not clean them up unless a later
  task explicitly approves removal.

## 2026-05-04 - local write scope policy

- Role: Builder -> Recorder
- Scope: update the icon-lane no-write policy so scoped local file/folder
  writes are allowed before the next agent workflow step
- Read: root multi-agent workflow, icon system/plan/task/changelog/handoff docs,
  current dirty worktree status, and recent make/apply icon contracts
- Changed: recorded that local writes are approved only when task-scoped and
  lane/write-scope local, while preserving hard gates for secrets/cloud auth,
  paid/API work, generated artifacts, asset move/delete, folder-icon
  application, ownership changes, and taste decisions
- Handoff: continue with the agent workflow using scoped local writes where the
  task explicitly allows them; generated artifacts and hard-gate actions still
  need separate approval.

## 2026-05-04 - SVG-Forge real samples decision

- Role: Builder -> Recorder
- Scope: decide whether real SVG-Forge sample rasters should be generated for
  conversion smoke tests after reviewing write scope and cleanup expectations
- Read: root and icon coordination docs, SVG-Forge README/changelog,
  `samples` docs, `tools\make_samples.py`, and current local sample/output
  listings
- Changed: added `documents/decisions/SVG_FORGE_REAL_SAMPLES_DECISION.md`, marked
  `icon-svg-forge-real-samples-decision` landed, and queued the exact future
  live smoke validation as `#live-required`
- Handoff: no real sample generation happened. Future validation should use the
  documented two-command run and dedicated `output\real-sample-smoke` folder,
  leaving cleanup/removal as a separate explicit task.

## 2026-05-04 - apply-icon apply-plan contract

- Role: Coordinator -> Builder -> Reviewer -> Recorder
- Scope: draft the approved `$apply-icon` apply-plan format before any
  `apply_icon.py` or `$apply-icon` implementation
- Read: icon task/plan/handoff docs, `$make-icon` contract/output-path docs,
  and build-note references for `apply_icon.py plan`, dry-run, apply, and
  apply-plan artifacts
- Changed: added `documents/contracts/APPLY_ICON_APPLY_PLAN_CONTRACT.md`, marked
  `icon-apply-tool-contract` landed, and updated the parked `$apply-icon`
  conditions in plan, changelog, and handoff
- Handoff: the apply-plan format is planning-only; do not implement
  `apply_icon.py`, create generated apply-plan artifacts, apply folder icons,
  move/delete assets, generate images, or call APIs without a later approved
  task.

## 2026-05-04 - make-icon output path review

- Role: Coordinator -> Builder -> Reviewer -> Recorder
- Scope: review planned `$make-icon` output path assumptions without creating
  folders, artifacts, scripts, images, or API calls
- Read: root workflow/routing docs, icon system/plan/task/handoff docs, and the
  `$make-icon` contract, interface, review, and dry-run transcript docs
- Changed: added `documents/reviews/MAKE_ICON_OUTPUT_PATH_REVIEW.md`, recorded that
  `vaultforge-icon/generated/briefs/` and
  `vaultforge-icon/generated/metadata/` stay as planned no-write preview
  defaults, and marked the review task landed
- Handoff: continue with the approved `$apply-icon` apply-plan contract if no
  newer Nath direction appears; keep all writes, scripts, live generation,
  asset operations, and folder-icon application parked. The `#live-required`
  workflow-rule edits were a prior recorded rotation, not a new output-path
  decision.

## 2026-05-04 - live-required soft gate rule

- Role: Coordinator -> Builder -> Reviewer -> Recorder
- Scope: retune approval rules so dry-run/build work can continue toward the
  icon-generator goal without treating every future live run as a hard stop
- Read: root workflow docs, icon system/plan/task/handoff docs, and current
  approved task list
- Changed: reserved `#nath` for hard gates, added `#live-required` for missing
  live validation, removed hard-gate tags from approved non-hard-gate tasks, and
  kept `#approved` as the clearance stamp
- Handoff: continue with output-path review; if a live run is needed later,
  create a `#live-required` task that names the exact live run, then keep moving
  through safe dry-run/build work unless the main icon-generator goal changes

## 2026-05-04 - workflow continuation adjustment

- Role: Coordinator -> Builder -> Reviewer -> Recorder
- Scope: adjust the workflow so review findings and future approval needs do
  not stop every run after one rotation
- Read: root multi-agent workflow, icon system/plan/task/handoff docs, and
  current workflow-memory notes
- Changed: added root and icon-lane continuation rules, recorded soft-gate vs
  hard-gate behavior, and marked the adjustment landed
- Handoff: continue with the already approved output-path review task; later
  retuned by the live-required rule so future live validation is only a hard
  stop when it cannot be deferred or changes the main icon-generator goal

## 2026-05-03 - make-icon dry-run transcript check

- Role: Coordinator -> Builder -> Reviewer -> Recorder
- Scope: define the no-write `$make-icon` dry-run transcript acceptance check
  and preserve `#approved` as the approval stamp
- Read: `documents/contracts/MAKE_ICON_INTERFACE_PLAN.md`, `documents/reviews/MAKE_ICON_INTERFACE_REVIEW.md`,
  `TASKS.md`, `SYSTEM.md`, `PLAN.md`, changelog, and handoff
- Changed: added `documents/contracts/MAKE_ICON_DRY_RUN_TRANSCRIPT_CHECK.md`, marked the transcript
  check landed, recorded the `#approved` stamp rule, fixed approval-tag spacing,
  and queued output path review
- Handoff: review output path assumptions next; implementation, generated
  artifacts, API calls, asset operations, and folder icon application remain
  parked

## 2026-05-03 - make-icon interface review

- Role: Coordinator -> Builder -> Reviewer -> Recorder
- Scope: review the no-write `$make-icon` interface plan and add the `#nath`
  task-tag rule before proceeding
- Read: `documents/contracts/MAKE_ICON_INTERFACE_PLAN.md`, `TASKS.md`, `SYSTEM.md`, `PLAN.md`,
  changelog, and handoff
- Changed: added `documents/reviews/MAKE_ICON_INTERFACE_REVIEW.md`, clarified `$make-icon` as a
  workflow label rather than a runnable command, marked the review landed,
  tagged Nath-gated open tasks, and queued the dry-run transcript check
- Handoff: define the dry-run transcript acceptance check next; implementation,
  generation, asset operations, and folder icon application remain parked

## 2026-05-03 - make-icon interface plan

- Role: Coordinator -> Builder -> Reviewer -> Recorder
- Scope: complete the no-write `$make-icon` interface plan and record the new
  rotation scope limit
- Read: `documents/contracts/MAKE_ICON_CONTRACT.md`, `documents/reviews/MAKE_ICON_BRIEF_REVIEW.md`, `TASKS.md`,
  `PLAN.md`, `SYSTEM.md`, changelog, and handoff
- Changed: added `documents/contracts/MAKE_ICON_INTERFACE_PLAN.md`, updated `$make-icon`
  activation gates, recorded the two-small-related-docs task rotation limit,
  marked the interface-plan task landed, and queued interface review
- Handoff: review the interface plan before implementation; no script,
  generation, asset operation, or folder icon application is approved

## 2026-05-03 - make-icon brief review

- Role: Coordinator -> Builder -> Reviewer -> Recorder
- Scope: compare the two manual `$make-icon` briefs and decide whether the
  metadata/output shape is stable enough to plan a no-write interface
- Read: `documents/contracts/MAKE_ICON_CONTRACT.md`, both manual brief notes, current task board,
  changelog, plan, and handoff
- Changed: added `documents/reviews/MAKE_ICON_BRIEF_REVIEW.md`, marked the two-brief review
  landed, and queued a no-write interface-plan task
- Handoff: no-write interface planning is allowed next; `make_icon.py` remains
  parked until dry-run/output/ownership gates and Nath approval are satisfied

## 2026-05-03 - second manual make-icon brief

- Role: Coordinator -> Builder -> Reviewer -> Recorder
- Scope: write a second Markdown-only `$make-icon` brief for a different
  existing lane folder
- Read: `documents/contracts/MAKE_ICON_CONTRACT.md`, current task board, handoff, and
  `build-notes` file list
- Changed: added `NOTE/Make Icon Brief - Build Notes.md`, marked the second
  manual brief task landed, and queued a two-brief contract review
- Handoff: compare the SVG-Forge and Build Notes briefs before considering any
  tool-interface planning; no script implementation is approved

## 2026-05-03 - manual make-icon brief and cycle rule

- Role: Coordinator -> Builder -> Reviewer -> Recorder
- Scope: resume the manual `$make-icon` brief task and include the clarified
  cycle rule
- Read: icon lane docs, `documents/contracts/MAKE_ICON_CONTRACT.md`, task board, and handoff
- Changed: added `NOTE/Make Icon Brief - SVG-Forge.md`, clarified one-cycle vs
  7-cycle estimation in lane docs, marked the manual brief task landed, and
  queued a second manual brief test
- Handoff: one manual brief is not enough to build `make_icon.py`; run one more
  manual brief before reviewing whether the contract is stable

## 2026-05-03 - make-icon no-paid-call contract

- Role: Coordinator -> Builder -> Reviewer -> Recorder
- Scope: draft only the `$make-icon` contract and decide whether `make_icon.py`
  should remain parked
- Read: icon lane docs, build-note tool/skill notes, current task board, and
  handoff
- Changed: added `documents/contracts/MAKE_ICON_CONTRACT.md`, marked `icon-make-tool-contract`
  landed, and queued one manual docs-only brief test
- Handoff: `make_icon.py` remains parked; prove the contract with manual briefs
  before considering any script

## 2026-05-03 - newest-first recording rule

- Role: Coordinator -> Builder -> Reviewer -> Recorder docs pass
- Scope: add the icon-lane rule that new `SIGN_UP.md` dated entries and
  `CHANGELOG.md` entries go above older entries
- Read: root workflow/routing docs, icon lane docs, current `SIGN_UP.md`, and
  current `CHANGELOG.md`
- Changed: updated `SYSTEM.md`, reordered existing dated `SIGN_UP.md` entries,
  reordered current changelog bullets, and added this landed task
- Handoff: next entries should be placed above older dated entries, keeping the
  multi-agent handoff near the top as the current resume block

## 2026-05-03 - bounded SVG-Forge setup-doc pass

- Role: Coordinator -> Builder -> Reviewer -> Builder -> Inspiration Scout ->
  Coordinator/Recorder -> Final Review
- Scope: complete a compact bounded workflow pass using one concrete
  deliverable: clarify SVG-Forge setup docs after the dry-run fixture work
- Read: root workflow/routing docs, icon lane docs, SVG-Forge docs, current
  tasks, changelog, and handoff
- Changed: removed the stale setup-helper expectation, documented the current
  working directory assumption, clarified generated sample files as a write
  step, and kept the dry-run-only fixture path as the no-write smoke check
- Handoff: next active task is the docs-only no-paid-call `$make-icon` contract;
  apply-icon and formal skills remain parked behind their written conditions.
  Later cycle-rule clarification records this as a compact pass, not a true
  seven-full-rotation run.

## 2026-05-03 - build-notes assessment and SVG-Forge fixture

- Role: Coordinator -> Reviewer -> Recorder -> Builder
- Scope: assess `build-notes`, adopt only useful process rules, park formal
  skills/tools, then fix the SVG-Forge dry-run sample path
- Read: root workflow/routing docs, icon lane docs, all `build-notes`, and
  SVG-Forge docs/sample notes
- Changed: updated `PLAN.md`, `SYSTEM.md`, `TASKS.md`, `CHANGELOG.md`,
  `SIGN_UP.md`, `svg-forge/README.md`, `svg-forge/CHANGELOG.md`, and added
  `svg-forge/samples/dry-run-only/`
- Handoff: next run should be a bounded 7-cycle test only after selecting one
  concrete icon-lane deliverable

## 2026-05-03 - SVG-Forge dry-run check

- Role: Reviewer -> Recorder second cycle
- Scope: verify the documented SVG-Forge dry-run path without live generation,
  asset moves, deletion, or output writes
- Read: `svg-forge/README.md`, `svg-forge/CHANGELOG.md`, and
  `svg-forge/samples/README.md`
- Changed: recorded the blocker in `TASKS.md`, `CHANGELOG.md`, and this handoff
- Handoff: command was safe but blocked by missing raster samples; do not run
  `tools/make_samples.py` unless a future task approves creating sample files

## 2026-05-03 - lane promotion test build

- Role: Coordinator -> Builder -> Reviewer -> Recorder workflow test
- Scope: promote `vaultforge-icon` into a lightweight active lane without live
  generation, paid API calls, deletion, asset moves, or SVG-Forge rewrite
- Read: root startup/routing/task docs, multi-agent workflow, icon notes, and
  SVG-Forge README/changelog
- Changed: added the icon section doc spine and queued SVG-Forge dry-run
  validation as the first small follow-up
- Handoff: SVG-Forge dry-run was attempted and recorded below; next work should
  clarify sample setup or add a no-write sample availability check
