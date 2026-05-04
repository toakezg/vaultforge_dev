# Icon Codex Start

You are working in the VaultForge icon lane.

Before changing icon workflow docs, SVG conversion behavior, or icon handoff
notes:

1. Read `..\CODEX_START.md`.
2. Read `..\CURRENT_STATE.md`.
3. Read `..\THREAD_MAP.md`.
4. Read `SYSTEM.md`.
5. Read `PLAN.md`.
6. Read `TASKS.md`.
7. Read `CHANGELOG.md`.
8. Read `SIGN_UP.md`.
9. If touching SVG-Forge, also read:
   - `svg-forge\README.md`
   - `svg-forge\CHANGELOG.md`

Current rule:

- This lane owns icon workflow coordination and icon-specific tooling notes.
- `svg-forge` is the first existing subtool in this lane.
- Local file/folder writes are approved only when the task explicitly scopes
  them and every written path stays inside the lane/write scope.
- Do not move, delete, regenerate, or rewrite existing icon assets without an
  explicit icon-lane task.
- Do not create generated artifacts or generated output folders unless the task
  explicitly approves those outputs by path.
- Use dry-run checks before live generation, conversion, paid API calls, or
  asset cleanup.
