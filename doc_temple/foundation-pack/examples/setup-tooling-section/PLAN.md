# Plan

## Section Thread Model

- `project-init` is a promoted worker section under root coordination.
- section threads should read root startup docs before section docs.
- this section should own repeatable setup and bootstrap behavior.

## Current Direction

- keep setup steps clear and repeatable
- reduce hidden environment assumptions
- make first-run tooling easy to follow

## Watchpoints

- setup docs can rot faster than runtime code if no one tests the flow
- hidden dependencies create operator confusion
- bootstrap convenience can become unsafe if scripts are changed casually

## Forward Look

- simplify setup as the project stabilizes
- keep troubleshooting close to the setup flow
- separate one-time bootstrap from ongoing tooling where useful
