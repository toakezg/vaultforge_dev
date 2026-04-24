# VaultForge Code Codex Start

You are working in the VaultForge Code section under `vaultforge-coding\`.

Before changing code bridge docs or implementation:

1. Read `..\CODEX_START.md`.
2. Read `..\SYSTEM.md`.
3. Read `..\THREAD_MAP.md`.
4. Read `README.md`.
5. Read `SYSTEM.md`.
6. Read `PLAN.md`.
7. Read `TASKS.md`.
8. Read `CHANGELOG.md`.
9. Read `SIGN_UP.md`.
10. Read `vaultforge_code_codex_api_bridge_spec_v_2.md`.

Current rule:

- keep the bridge local-first, Windows-friendly, and safe by default
- do not modify unrelated VaultForge sections when implementing the bridge
  unless an explicit integration task calls for it
- keep `vaultforge-code` on the execution/reporting side and do not push XP,
  quest, achievement, reward, or dashboard interpretation into this section
- treat `vaultforge-coding\` as the folder path and `VaultForge Code` as the
  section identity

At the end of a meaningful coding-section run:

- update `CHANGELOG.md`
- update root `CHANGELOG.md` if the change affects cross-lane coordination or
  a shared contract
