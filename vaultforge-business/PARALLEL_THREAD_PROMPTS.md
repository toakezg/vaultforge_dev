# Parallel Thread Prompts

These are narrow follow-on tasks that can be run in separate
`vaultforge-business` threads without changing shared engine routing.

## 1. Prompt Bank Cleanup

Goal: improve business prompt-bank organization without touching shared engine
behavior.

Suggested prompt:

```text
From E:\tools\vaultforge\ root, do a vaultforge-business prompt-bank cleanup pass only.

Scope:
- vaultforge-business prompt banks, docs, and organization notes
- no engine runtime changes
- no art wrapper changes
- no output routing changes

Tasks:
1. Inventory current business prompt bank files and naming patterns.
2. Identify duplicates, near-duplicates, and unclear category boundaries.
3. Propose and implement a small cleanup that preserves current behavior.
4. Update only the docs that help future prompt-bank maintenance.
5. Do not change preset/style/mod behavior unless required for correctness.

Deliver:
- exact files changed
- exact findings
- any deferred cleanup items
```

## 2. Safer Pack Definitions

Goal: reduce future shell-fragility by designing a more structured pack format,
without replacing the current runner yet unless the change is tiny and proven.

Suggested prompt:

```text
From E:\tools\vaultforge\ root, do a design-and-smoke pass for safer business pack definitions.

Scope:
- vaultforge-business only
- keep current run-client-pack.ps1 working
- do not change engine routing

Tasks:
1. Inspect current pack file usage and placeholder expansion.
2. Propose a structured alternative format with less quoting risk.
3. If trivial and safe, add support for the new format alongside the old one.
4. Preserve current text-pack behavior by default.
5. Add one safe dry-run example if useful.

Deliver:
- recommendation
- any minimal implementation
- dry-run commands
- compatibility notes
```

## 3. Business Metadata Contract

Goal: tighten naming and metadata rules for client deliverables without changing
generation behavior.

Suggested prompt:

```text
From E:\tools\vaultforge\ root, do a vaultforge-business metadata contract pass only.

Scope:
- vaultforge-business docs/scripts where metadata naming is defined
- no engine behavior changes
- no art changes

Tasks:
1. Inspect current metadata fields, folder naming, and job/tag/client naming patterns.
2. Identify inconsistencies or weak spots for downstream sorting and review.
3. Propose and implement only tiny safe improvements.
4. Document what should remain lane-owned versus what could become shared later.

Deliver:
- exact findings
- exact files changed
- remaining follow-up items
```

## 4. Gallery and Review Surface

Goal: improve downstream review of business outputs without touching the shared
generation core.

Suggested prompt:

```text
From E:\tools\vaultforge\ root, do a vaultforge-business review-surface pass only.

Scope:
- vaultforge-business generated output review helpers, docs, and scripts
- no engine runtime changes

Tasks:
1. Inspect what review helpers already exist for generated business outputs.
2. Identify the smallest useful improvement for browsing, contact sheets, or summary pages.
3. Implement only a narrow helper if it is low-risk.
4. Keep output roots and generation commands unchanged.

Deliver:
- exact commands run
- exact files changed
- what remains for a fuller gallery pass
```

## 5. Dry-Run Contract Hardening

Goal: make business dry-run safer and more predictable without changing live
generation behavior.

Suggested prompt:

```text
From E:\tools\vaultforge\ root, do a vaultforge-business dry-run contract pass only.

Scope:
- vaultforge-business only
- no engine feature work
- no art wrapper changes

Tasks:
1. Identify every file/directory/metadata write that still happens during DryRun.
2. Decide which writes are acceptable and which should be suppressed.
3. Implement only the smallest safe improvement.
4. Re-run dry-run checks and document any remaining side effects.

Deliver:
- exact dry-run commands
- before/after behavior
- any blocked items
```

## Coordination note

Keep separate threads away from these shared-runtime files unless the task
explicitly requires them:

- `vaultforge-business\run_business.ps1`
- `vaultforge-business\run-client-pack.ps1`
- `vaultforge-engine\src\generate.py`
- `vaultforge-engine\run_engine.bat`

That keeps thread overlap low while shared-core hardening settles.
