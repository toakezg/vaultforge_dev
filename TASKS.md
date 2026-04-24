# TASKS

## Todays Goal/Bonus
-*NEW*-  Todays Goal/Bonus. Achievable goal(s) that may be aimed for and reward both XP and Bonus-XP (XPLife) . To encourage reaching minor or Major milestones or even just some fun. Keep in mind these are not mandatory and priority tasks still take precedence.
```tasks
path includes TODAYS GOAL 
```

## Not Done System wide
```tasks
not done
sort by priority
```

## Active Pool

- [x] 🔺 Start the dedicated engine thread for the engine-specific step 7 handoff after it reads root `CODEX_START.md`, root `THREAD_MAP.md`, and engine section docs #engine #threading #nath 2026-04-13 ✅ 2026-04-13
- [ ] ⏫ Keep `THREAD_MAP.md` current as sections are promoted, parked, or moved #root #threading 🆔 root-thread-map-review 🔁 every week when done 2026-04-13
- [ ] 🔽 Decide whether parked folders such as `vaultforge-core`, `vaultforge-design`, `vaultforge-system`, and `vaultforge-init` should become promoted sections with full doc sets #root #planning 🆔 root-promote-parked-sections 2026-04-13
      #decided Yes these sections should be promoted with docs that reflect current vaultforge practices.
- [ ] 🔽 Decide when or whether the sibling art runtime should be migrated under root instead of only represented by the `vaultforge-art` coordination base #art #architecture 🆔 root-art-runtime-migration-decision ⛔ art-bridge-inventory 2026-04-13
- [ ] 🔼 Build Part B for XP4Life Icons: copy selected outputs into `selected/`, rename them cleanly, and create an icon index note #root #icons #xp4life 🆔 root-xp4life-part-b 2026-04-11
- [ ] 🔽 Decide whether XP4Life should earn a dedicated preset inside `vaultforge-art` instead of relying on the shared `icon` preset #root #icons #planning 🆔 root-xp4life-preset-decision 2026-04-11
- [ ] 🔽 Review whether the `_template/` version of the icon lane feels useful after a couple of real vault creates, or whether it should be reduced to a lighter stub #root #template #planning 🆔 root-template-lane-review 2026-04-11
- [ ] 🔽 Decide whether generated example PNGs should stay in `_template/` or move into a separate demo/example pack #root #template #icons 🆔 root-template-png-location 2026-04-11
- [ ] 🔼 Extend Part B once category naming, reward rules, and title rules settle from Part A output review #root #xp4life #planning 🆔 root-xp4life-part-b-extend ⛔ root-xp4life-part-b 2026-04-11
- [ ] 🔼 Prototype `VaultForge Icons` client job storage with `client.yaml`, references, generated, selected, delivery, and usage files #root #vaultforge-icons #clients 🆔 root-vaultforge-icons-client-storage 2026-04-11
- [ ] 🔽 Plan image-input and tweak/edit flags for VaultForge Icons after reviewing what belongs in `vaultforge-engine` versus lane wrappers #root #vaultforge-icons #api 🆔 root-vaultforge-icons-edit-flags 2026-04-11
- [ ] 🔽 Decide whether usage stats should start as CSV only or become JSON/YAML plus CSV exports #root #vaultforge-icons #stats 🆔 root-vaultforge-icons-stats-format ⛔ root-vaultforge-icons-client-storage 2026-04-11

## Landed Work

- [x] Activate `vaultforge-xp4l` as an active section in root coordination docs
  and thread routing #xp4l #docs 2026-04-16
- [x] Promote `vaultforge-coding` into the VaultForge Code section and add its first local doc set #coding #docs 2026-04-16
- [x] Add the root/section thread model, root `THREAD_MAP.md`, section sign-up pattern, and art coordination base #root #docs #threading #nath 2026-04-13
- [x] Update `vaultforge-business` to target `vaultforge-engine` after the copied engine passed dry-run checks, while preserving current business output routing #business #engine 2026-04-12
- [x] Rename the shared engine entrypoint to `vaultforge-engine\src\generate.py` and refresh root docs around the current engine split #engine #docs 2026-04-12
- [x] Compare business wrapper dry-run behavior against direct engine calls before changing business defaults #business #engine 2026-04-12
- [x] Add the art compatibility bridge so `vaultforge-art\run_art.bat` delegates to `vaultforge-engine` while preserving art-root defaults #engine #compatibility 2026-04-12
- [x] Prototype `vaultforge-engine` by copying reusable generator code and tests from the dirty sibling `vaultforge-art` worktree without breaking current wrappers #engine #architecture 2026-04-12
- [x] Add `vaultforge-engine` documentation skeleton and root architecture note for staged engine extraction #engine #architecture 2026-04-11
- [x] Validate one live XP4Life Icons Part A generation run from `_template/` and copy examples into workspace outputs for review #root #icons #validation 2026-04-11
- [x] Add a lightweight output review note with the first successful icon examples #root #icons #docs 2026-04-11
- [x] Rewrite `How to - Create XP4Life Icon set (obsidian).md` with a transferable Obsidian icon-set method and required plugin ID #root #icons #obsidian 2026-04-11
- [x] Capture the broader `VaultForge Icons` branch plan from phone notes, including client templates, usage stats, pricing, ads, and future image-input flags #root #vaultforge-icons #planning 2026-04-11
- [x] Distill `Icons - part A` into a clean local reference note and attack-plan note #root #icons #docs 2026-04-11
- [x] Create a quick-use note with runnable commands and recommended prompts for XP4Life Icons Part A #root #icons #docs 2026-04-11
- [x] Add a reusable prompt bank for quests, achievements, titles, and rewards under `ICON/XP4Life/part-a/prompts/` #root #icons #prompts 2026-04-11
- [x] Add `run-icons-part-a.bat` as a local launcher that delegates generation to `vaultforge-art` while keeping prompts and outputs in this vault #root #icons #cli 2026-04-11
- [x] Verify the Part A launcher in `--dry-run` mode across quests, achievements, titles, and rewards #root #icons #validation 2026-04-11
- [x] Mirror the operator-facing Part A assets into `_template/` and add a small seeded `Home.md` entry point #root #icons #template 2026-04-11
- [x] Establish the core workspace docs for future Codex threads: `README.md`, `SYSTEM.md`, `PLAN.md`, `TASKS.md`, `CHANGELOG.md`, and `CODEX_START.md` #root #docs #planning 2026-04-11

## Working Rules

- Keep actionable work here.
- Keep direction and tradeoffs in `PLAN.md`.
- Add new completed structural changes to `CHANGELOG.md`.
- If a workflow needs a short operator note, prefer a topic quick guide in `NOTE/`.
- Tag every task with at least one section tag and one task-type tag, for example `#root #threading` or `#engine #docs`.
- Set priority by section-local importance using Tasks markers: 🔺 highest, ⏫ high, 🔼 medium, 🔽 low, ⏬ lowest. Leave no marker only for unranked inbox or backlog tasks.
- Give active and next tasks a short stable `🆔` id so dependency chains can stay readable.
- Use `🔁` only for genuine recurring work, preferably with `when done` for review or maintenance loops.
- Use `⛔ task-id` for `before this` dependencies. Treat `after this` as the reverse link: give the current task a `🆔`, then point the follow-up task at it with `⛔`.
- Hold `due`, `scheduled`, `start`, and `created` until a later planning pass.
- Keep the automatic `tasks` query above the manual active pool so root can see not-done work without copying tasks by hand.
