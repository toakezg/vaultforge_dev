# PLAN

## Role

This note keeps the active direction, implementation decisions, and watchpoints for the VaultForge workspace.

`TASKS.md` holds the actionable work pool.

## Current Direction

Date: 2026-04-27

- Keep this repo focused on reusable vault structure, launcher helpers, and note-first workflow setup.
- Run VaultForge through a root/section thread model: root coordinates, sections execute focused work.
- Keep `CURRENT_STATE.md` as the app-UI-independent recovery anchor when Codex project or thread visibility drifts.
- Use `THREAD_MAP.md` before cross-section edits so dedicated threads know where to operate.
- Promote active worker bases with section docs: `CODEX_START.md`, `SYSTEM.md`, `PLAN.md`, `TASKS.md`, `CHANGELOG.md`, and `SIGN_UP.md`.
- Use sibling tools when they already do the heavy lifting well.
- Continue the engine split now that `vaultforge-engine\src\generate.py` exists as the shared core prototype.
- Treat `vaultforge-art` as the art/playground lane and `vaultforge-business` as the client lane.
- Promote `vaultforge-coding` as the local-first VaultForge Code bridge
  section around the Codex/OpenAI API bridge spec.
- Activate `vaultforge-xp4l` as the XP4Life interpretation and progression
  section that consumes structured upstream events without taking over execution.
- Keep VaultForge Code on the execution/reporting side and leave deeper XP
  interpretation for a future sibling section instead of folding it into the
  bridge lane.
- Build XP4Life Icons Part A as a concrete, repeatable lane rather than leaving it as a loose idea.
- Keep the icon workflow editable from notes first, then runnable from a simple batch entry point.
- Route icon outputs into this vault so prompts, docs, and results stay reviewable together.
- Seed only the operator-facing icon assets into `_template/` so new vaults inherit the workflow without inheriting the implementation planning notes.
- Treat the successful XP4Life run as proof that a broader VaultForge Icons branch is worth planning, but keep client/logo workflow work staged and selective.

## XP4Life Icons Part A Implementation Shape

- Source of truth for the concept lives in `NOTE/Icons - part A.md`.
- Execution planning lives in `NOTE/Icons - part A - todo.md`.
- Quick operator guidance lives in `NOTE/Icons - part A - quick use guide.md`.
- Recommended prompts live in `ICON/XP4Life/part-a/prompts/`.
- The local launcher lives in `run-icons-part-a.bat`.
- The launcher may still delegate image generation directly to the old runtime/reference prototype at `F:\tools\image_generation\vaultforge-art\generate_art.py`.

## Watchpoints

- The Codex app sidebar can lose or regroup visible project/thread history; repo docs must remain strong enough to recover coordination without relying on that UI.
- Dedicated section threads can drift if they skip root `THREAD_MAP.md` or fail to update their section changelog.
- Root should not quietly become the worker space for tasks that belong in engine, business, or art.
- The coding bridge section can sprawl if it starts acting like the general
  implementation lane for unrelated VaultForge work.
- The coding bridge should emit factual events, not XP meaning, or it will blur
  into a future interpretation lane.
- XP4L can sprawl if it starts absorbing execution concerns before its event and
  output contracts are stable.
- `vaultforge-art` now has a root coordination base; the old runtime/reference prototype is `F:\tools\image_generation\vaultforge-art`, and the planned fresh lane is `F:\vaultforge\vaultforge-art`.
- The XP4Life launcher currently depends on a fixed sibling project path.
- The shared engine prototype is in this workspace, but the XP4Life launcher has not been retargeted to it yet.
- Prompt quality has one successful live Part A run, but Part B selection and packaging still need operator review.
- The current art project has a general `icon` preset, not a dedicated XP4Life preset yet.
- If XP4Life grows beyond Part A, prompt organization and naming rules will matter more than raw prompt volume.
- `_template/` now carries the optional icon lane, so future vault creation should be reviewed to make sure that remains helpful rather than noisy.
- Generated examples currently exist in `_template/` because the successful run was launched there; decide later whether template seed examples are helpful or should be moved into a separate demo pack.

## Forward Look

- The next dedicated engine thread should boot from root, then engine, then handle the engine-specific step 7 handoff from the business notes.
- Each active section should assign or naturally maintain one thread to keep `SIGN_UP.md`, `CHANGELOG.md`, and root handoff notes current.
- `vaultforge-engine/` now holds the first verified shared generator prototype.
- `vaultforge-business` now targets the shared engine directly while preserving business output routing.
- The next dedicated coding thread should scaffold the VaultForge Code bridge
  MVP inside `vaultforge-coding` without modifying unrelated sections.
- If VaultForge later promotes an XP interpretation section, it should consume
  coding events rather than push that logic back into `vaultforge-coding`.
- The next dedicated XP4L thread should lock the event contract and output
  contract before deeper progression heuristics harden.
- The next shared-core steps are safer dry-run semantics, wrapper parity checks, and only then native shared features such as variants, input images, tweaks, and galleries.
- If the first results are strong, Part B can add tighter naming rules, export selection, and curation notes.
- A dedicated XP4Life preset inside `vaultforge-art` may become worthwhile later.
- The next template decision is no longer whether to seed the lane, but whether the seeded version should be expanded, reduced, or split into optional packs later.
- A gallery note may become useful once this vault has real generated icon outputs to curate.
- VaultForge Icons can grow into a client/logo branch with YAML client intake, usage stats, price/ad reference docs, and image-reference editing, but those should be implemented after Part B selection/packaging.
