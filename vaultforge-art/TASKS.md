# Art Tasks

## Art Open Tasks

```tasks
not done
tag includes art
```

## Active Pool

- [ ] 🔽 Decide whether and when the sibling art runtime should migrate under root #art #architecture 🆔 art-runtime-migration-decision ⛔ art-bridge-inventory 2026-04-13
- [ ] 🔼 Inventory art bridge assumptions before changing shared engine behavior #art #engine #compatibility 🆔 art-bridge-inventory 2026-04-13
- [ ] 🔼 Record new art threads in `SIGN_UP.md` and art coordination changes in `CHANGELOG.md` #art #docs 🆔 art-thread-signup-review 🔁 every week when done 2026-04-13

## Landed Work

- [x] Add the root art coordination base without moving the sibling art runtime #art #threading 2026-04-13

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
