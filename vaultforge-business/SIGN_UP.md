# Business Sign Up

New business threads should add a short entry here before or after their first meaningful change.

Use this shape:

```text
## YYYY-MM-DD - thread label

- Role:
- Scope:
- Read:
- Changed:
- Handoff:
```

## 2026-04-13 - section setup

- Role: documentation setup for dedicated business threads
- Scope: section docs, root handoff, and startup requirements
- Read: root `CODEX_START.md`, root `THREAD_MAP.md`, business docs, Nath notes
- Changed: business docs now point new threads through root overhead first
- Handoff: engine-specific step 7 work should move to a dedicated engine thread

## 2026-04-15 - real client prompt-bank expansion

- Role: add real client markdown prompt-bank inventory now that reusable packs exist
- Scope: prompt-bank client folders, inventory docs, and business task tracking
- Read: root `CODEX_START.md`, root `THREAD_MAP.md`, business docs, prompt templates, generated client runs
- Changed: added `empower-you-plan-management` and `jubal` markdown prompt-bank folders and updated the business inventory/changelog/task state
- Handoff: more reviewed client folders can be added in-business; native engine flags and direct edit APIs still belong in the engine lane

## 2026-04-16 - business task master review

- Role: review business task ordering, priorities, and dependency truthfulness
- Scope: business startup docs, plan/task alignment, and open integration sequencing
- Read: root `CODEX_START.md`, root `README.md`, root `SYSTEM.md`, root `PLAN.md`, root `TASKS.md`, root `THREAD_MAP.md`, root `CHANGELOG.md`, business docs, and engine task/plan/docs
- Changed: corrected the open business integration queue to reflect that engine-native `--client`, `--job`, `--tag`, and `--variants` already exist, kept `--tweak` wrapper-owned for now, and added a manifest-contract follow-up task
- Handoff: the next business implementation pass can start with `business-engine-native-metadata-adoption`; direct edit and reference-image wiring still wait on engine API work

## 2026-05-09 - workflow-b builder hard gate

- Role: builder for Workflow B cycle 1 business-lane approved local slices
- Scope: `vaultforge-business` section files only
- Read: prompt packet snapshots for root docs, workflow rules, and business docs; live shell reads were blocked before PowerShell started
- Changed: no implementation changes; recorded this hard-gate note only
- Handoff: retry `business-engine-native-metadata-adoption` after local shell access works; first checks should be `git status --short`, `Get-Content .\run_business.ps1`, and `Get-Content ..\vaultforge-engine\src\generate.py`
- Blocker: every shell command failed with `windows sandbox: CryptUnprotectData failed: 2148073483`, so implementation and verification would have been blind
- Decision: pause this builder slice until shell reads work; do not edit wrapper behavior from snapshots alone
- Resume prompt: `Continue Workflow B cycle 1 for vaultforge-business. Read SIGN_UP.md latest entry, then implement business-engine-native-metadata-adoption if git status and wrapper/engine reads are available.`
- Estimated tokens: about 9k used before pause; likely 20k-35k more to inspect, implement, test, and record the wrapper metadata pass

## 2026-05-09 - workflow-b business native metadata builder

- Role: builder for Workflow B cycle 1 business-lane approved local slices
- Scope: `vaultforge-business` section files only
- Read: prompt packet snapshots, live `git status --short`, `run_business.ps1`, `run_business_md_bank.ps1`, engine `generate.py` CLI/variant handling, business `TASKS.md`, `CHANGELOG.md`, and `SIGN_UP.md`
- Changed: `run_business.ps1` now passes native engine `--client`, `--job`, `--tag`, and `--variants`; direct and markdown wrappers default to sibling `..\vaultforge-engine`; business docs mention the native metadata bridge
- Handoff: `business-engine-native-metadata-adoption` and `business-wrapper-backcompat` are landed; next business slice is `business-manifest-contract-review`, especially deciding how to treat engine image-sidecar JSON files alongside wrapper-owned `run.json` and `gallery-entry.json`; a lower-priority follow-up now tracks the `run-client-pack.ps1 -WhatIf` log side effect
- Verification: parser checks for both PowerShell wrappers; direct wrapper `-WhatIf`; direct wrapper `-DryRun`; `run_business_smoke.bat`; markdown-bank `-WhatIf`; pack-runner `-WhatIf`; checked the unique dry-run client output folder was not created
- Blocker or decision: no hard gate hit; no live generation was run
- Resume prompt: `Continue Workflow B for vaultforge-business. Start with business-manifest-contract-review and inspect a dry-run/live-safe sample of engine sidecar metadata versus business run.json/gallery-entry.json before changing manifest ownership.`

## 2026-05-09 - workflow-b business native metadata reviewer

- Role: reviewer for Workflow B cycle 1 business-lane approved local slices
- Scope: `vaultforge-business` verification and review findings
- Read: run packet outputs, live `git status --short`, business wrapper diffs, `run_business.ps1`, `run_business_md_bank.ps1`, engine variant/output-path handling, `TASKS.md`, `CHANGELOG.md`, and `SIGN_UP.md`
- Findings: no blocking findings in the business native metadata bridge; the known `run-client-pack.ps1 -WhatIf` log side effect is already parked as `business-pack-whatif-log-side-effect`
- Verification: parser checks passed for both PowerShell wrappers; direct wrapper `-WhatIf` showed native `--client`, `--job`, `--tag`, and `--variants`; direct wrapper `-DryRun` reached engine context metadata and variant output paths; `run_business_smoke.bat` passed; markdown-bank `-WhatIf` passed; review output folders stayed absent; `git diff --check` reported only LF-to-CRLF warnings
- Blocker or decision: no hard gate hit; no live generation was run
- Resume prompt: `Continue Workflow B for vaultforge-business as recorder. Record the reviewer result, keep business-manifest-contract-review as the next slice, and do not run live generation unless Nath approves it.`

## 2026-05-09 - workflow-b business native metadata recorder closure

- Role: root recorder closing the Workflow B cycle 1 business slice
- Scope: affected section handoff note only
- Read: run packet outputs for business builder and reviewer, plus the live business handoff
- Changed: recorded that the reviewed native metadata bridge slice is closed for cycle 1
- Handoff: no hard gate remains for `business-engine-native-metadata-adoption` or `business-wrapper-backcompat`. The next business slice remains `business-manifest-contract-review`; the `run-client-pack.ps1 -WhatIf` log side effect stays parked as `business-pack-whatif-log-side-effect`. No live generation was run or approved in this recorder pass.
