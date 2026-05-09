# Engine Changelog

## 2026-05-09

- Added native local image references with `--input-image` and `--reference-image`, including dry-run visibility and sidecar metadata.
- Added Markdown batch prompt image extraction for standard Markdown embeds, Obsidian wiki embeds, and simple HTML image tags.
- Updated batch hashing so changed reference images trigger reruns instead of being treated as unchanged prompt text.

## 2026-04-16

- Added the engine task-property rule: active and next tasks now carry stable `🆔` ids, recurring loops should use `🔁`, and dependencies should use `⛔`.
- Backfilled ids and dependency links into the current open engine task pool, including shared ids needed by business follow-up work.
- Reviewed the open engine task board against the engine verification, compatibility, and architecture notes.
- Promoted config-safe `@file.conf` review, added missing metadata/edit-contract planning tasks, and tightened the gallery plus image-input dependency chain.

## 2026-04-15

- Decided to keep engine execution launcher/direct-script based for now instead of requiring an editable `.venv` install while the shared engine is still a small prototype.
- Updated `run_engine.bat` to prefer a local `.venv\Scripts\python.exe` when present and otherwise fall back to the Windows `py` launcher.

## 2026-04-14

- Added the engine open-task query block so `TASKS.md` self-populates not-done engine tasks.

## 2026-04-13

- Added engine-native `--client`, `--job`, `--tag`, and `--variants` flags for low-risk business handoff metadata, output naming, multi-variant generation, dry-run previews, and optional sidecar run manifests.
- Added the engine-local task priority rule and marked current open engine tasks with Obsidian Tasks priority markers.
- Hard-set the engine task tag rule and tagged existing engine task lines with section and task-type tags.
- Added the engine section to the root/section thread model.
- Updated engine startup docs so dedicated engine threads read root overhead context before changing shared generator behavior.
- Added `SIGN_UP.md` as the engine thread sign-in and handoff trace.

## 2026-04-12

- Verified `vaultforge-engine\src\generate.py` as the shared engine prototype.
- Preserved dry-run behavior and current CLI conventions through the first business retarget.
