# Tasks

## Coding Open Tasks

```tasks
not done
tag includes coding
```

## Active Pool

- [ ] ⏫ Record new coding threads in `SIGN_UP.md` and coding behavior changes in
  `CHANGELOG.md` #coding #docs 🆔 coding-thread-signup-review 🔁 every week when done 2026-04-16
- [ ] ⏫ Build CLI mode parsing, preset prompt loading, and prompt compilation flow
  #coding #cli 🆔 coding-cli-prompt-flow ⛔ coding-config-loader 2026-04-16
- [ ] 🔼 Build project context loading with include/exclude and max-file guards
  #coding #implementation 🆔 coding-context-builder ⛔ coding-config-loader 2026-04-16
- [ ] ⏫ Add a run-manifest writer for per-run metadata, context manifests, and
  stable saved artifacts #coding #reports 🆔 coding-run-manifest-writer ⛔ coding-config-loader 2026-04-16
- [ ] ⏫ Add a structured event writer that emits neutral factual events for
  downstream systems without doing XP interpretation #coding #api 🆔 coding-event-writer ⛔ coding-run-manifest-writer 2026-04-16
- [ ] 🔺 Wire the Responses API call, per-run artifact saving, event emission,
  and clean terminal summary output #coding #api 🆔 coding-responses-run-output ⛔ coding-cli-prompt-flow 2026-04-16
- [ ] ⏫ Add usage tracking JSON files plus append-only `usage_log.jsonl`,
  `run_log.jsonl`, and `usage_summary.md` #coding #reports 🆔 coding-usage-reports ⛔ coding-responses-run-output 2026-04-16

## Next

- [ ] 🔼 Add batch launchers, `.env.example`, and smoke-testable CLI examples
  #coding #cli 🆔 coding-launcher-env-pass ⛔ coding-responses-run-output 2026-04-16
- [ ] 🔼 Add tests for config loading, context building, usage tracking, and
  event writing #coding #tests 🆔 coding-mvp-tests ⛔ coding-usage-reports 2026-04-16
- [ ] 🔽 Decide when to add approval-gated write mode, patch application, and
  richer downstream event shaping after the MVP is stable #coding #planning 🆔 coding-phase2-writes-events ⛔ coding-usage-reports 2026-04-16

## Landed Work

- [x] Build config loading, environment defaults, and local path resolution for
  runs, reports, and events before CLI wiring #coding #api 🆔 coding-config-loader 2026-04-17
- [x] Implement the first local usage tracking pass with per-run JSON artifacts,
  append-only lifecycle events, and a rebuilt section usage summary
  #coding #reports 2026-04-17
- [x] Scaffold the local Python project layout for the VaultForge Code bridge
  under `src\vf_code_bridge`, `assets\`, and `tests\`, including
  `VERIFICATION.md` #coding #implementation 2026-04-17
- [x] Promote `vaultforge-coding` into the VaultForge Code section and add the
  first section doc set #coding #docs 2026-04-16
- [x] Capture the v2 Codex/OpenAI bridge implementation spec in
  `vaultforge_code_codex_api_bridge_spec_v_2.md` #coding #planning 2026-04-16

## Working Rules

- keep actionable bridge work here
- keep direction and tradeoffs in `PLAN.md`
- add notable section changes to `CHANGELOG.md`
- tag every task with at least one section tag and one task-type tag
- keep the automatic coding `tasks` query above manual task sections
- prefer local-first bridge behavior over remote-service sprawl
