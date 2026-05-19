# Art Tasks

## Art Open Tasks

```tasks
not done
tag includes art
```

## Active Pool

- [ ] 🔺 Keep the `run_art.bat` wrapper thin and aligned with the shared engine contract #art #cli 🆔 art-wrapper-maintain
- [ ] 🔼 Add art-specific prompt packs or presets only after a real recurring need appears #art #prompts 🆔 art-preset-expansion
- [ ] 🔼 Capture the first real art outputs and note what the lane still needs for steady use #art #validation 🆔 art-first-output-review ⛔ art-wrapper-maintain

## Landed Work

- [x] Promote `vaultforge-art` from coordination base into a live art lane with a wrapper, inbox, output, and v01 lane doc #art #docs

## Working Rules

- Keep art experiments lane-owned.
- Keep shared generator contracts in engine.
- Keep client workflow out of the art lane.
- Tag every task with at least one section tag and one task-type tag, for example `#art #docs` or `#art #architecture`.
- Set priority by art-local importance using Tasks markers: 🔺 highest, ⏫ high, 🔼 medium, 🔽 low, ⏬ lowest. Leave no marker only for unranked inbox or backlog tasks.
- Give active and next tasks a short stable `🆔` id so dependency chains can stay readable.
- Use `🔁` only for genuine recurring work, preferably with `when done` for review or maintenance loops.
- Use `⛔ task-id` for `before this` dependencies. Treat `after this` as the reverse link: give the current task a `🆔`, then point the follow-up task at it with `⛔`.
- Hold `due`, `scheduled`, `start`, and `created` until a later planning pass.
- Keep the automatic art `tasks` query above manual task sections so open art work self-populates.
- Use `inbox\` for batch prompt files and `output\` for generated images.
