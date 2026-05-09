# Tasks

## Engine Open Tasks

```tasks
not done
tag includes engine
```

## Now

- [x] 🔺 Start the dedicated engine thread for the step 7 handoff after reading root overhead docs and this section's docs #engine #threading #nath 2026-04-13
- [x] ⏫ Record new engine threads in `SIGN_UP.md` and engine behavior changes in `CHANGELOG.md` #engine #docs 2026-04-13
- [ ] ⏫ Keep `SIGN_UP.md` and `CHANGELOG.md` current for engine threads and behavior changes #engine #docs 🆔 engine-doc-hygiene 🔁 every week when done
- [x] Create engine skeleton docs #engine #docs
- [x] Record first extraction plan #engine #planning
- [x] Decide exact Python package layout for copied engine code #engine #architecture
- [x] Decide whether the first engine entrypoint should preserve the `generate.py` filename #engine #architecture
- [x] Copy the shared engine into `src\generate.py` #engine #implementation
- [x] Copy and adapt `tests\test_generate.py` #engine #tests
- [x] Add `run_engine.bat` #engine #cli
- [x] Verify unit tests and dry-run behavior #engine #validation
- [x] Add project-root override for delegated lane compatibility #engine #compatibility
- [x] Update `vaultforge-art\run_art.bat` to delegate to the engine while preserving art-root defaults #engine #compatibility
- [x] Record compatibility findings in `COMPATIBILITY.md` #engine #docs

## Next

- [x] Update business wrapper default with a tiny retarget-only change to call `vaultforge-engine\src\generate.py` directly #engine #compatibility
- [x] Rename the engine entrypoint and update wrappers/tests/docs to the neutral `generate.py` path #engine #docs
- [x] 🔽 Decide whether to install the engine editable into its own `.venv` or keep launcher-based execution for now #engine #planning
- [x] Compare direct engine dry-run output against the current business dry-run before retargeting business #engine #validation
- [ ] ⏫ Decide whether `@file.conf` smoke configs should include `--dry-run` variants for safer testing #engine #validation 🆔 engine-conf-dry-run-variants
- [ ] 🔼 Review whether engine sidecar JSON should stay additive or become a shared manifest contract before gallery hooks land #engine #metadata 🆔 engine-manifest-contract-review ⛔ engine-business-metadata-flags
- [x] ⏫ Define the shared tweak/edit/reference contract before landing native input-image or reference-image flags #engine #api 🆔 engine-edit-reference-contract 2026-05-09

## Later

- [ ] 🔽 Split registries into dedicated preset/style/mod files if the single-file module becomes hard to maintain #engine #architecture 🆔 engine-split-registries
- [x] ⏫ Add business-native metadata flags #engine #metadata 🆔 engine-business-metadata-flags
- [ ] 🔽 Consider a future no-write preview mode for business dry-runs once config-safe testing is settled #engine #dry-run 🆔 engine-no-write-preview ⛔ engine-conf-dry-run-variants
- [x] 🔼 Add image edit plumbing for `--input-image` #engine #api 🆔 engine-input-image-plumbing ⛔ engine-edit-reference-contract 2026-05-09
- [x] 🔼 Add reference image plumbing #engine #api 🆔 engine-reference-image-plumbing ⛔ engine-edit-reference-contract 2026-05-09
- [ ] 🔽 Add gallery/contact-sheet generation hooks #engine #gallery 🆔 engine-gallery-hooks ⛔ engine-manifest-contract-review

## Working Rules

- Tag every task with at least one section tag and one task-type tag, for example `#engine #docs` or `#engine #tests`.
- Set priority by engine-local importance using Tasks markers: 🔺 highest, ⏫ high, 🔼 medium, 🔽 low, ⏬ lowest. Leave no marker only for unranked inbox or backlog tasks.
- Give active and next tasks a short stable `🆔` id so dependency chains can stay readable.
- Use `🔁` only for genuine recurring work, preferably with `when done` for review or maintenance loops.
- Use `⛔ task-id` for `before this` dependencies. Treat `after this` as the reverse link: give the current task a `🆔`, then point the follow-up task at it with `⛔`.
- Hold `due`, `scheduled`, `start`, and `created` until a later planning pass.
- Keep the automatic engine `tasks` query above manual task sections so open engine work self-populates.
