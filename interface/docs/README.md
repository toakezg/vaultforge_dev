# VaultForge Operator Interface

This folder contains the local operator UI for VaultForge.

The first slice is a dependency-free static app. It is intentionally separate
from engine, business, icon, XP4L, and art runtime behavior.

## Setup

Use the local launcher from this folder:

```powershell
.\run-interface.bat
```

It serves the static app on `127.0.0.1:4173` and opens the interface in the
default browser. To choose a different port, pass it as the first argument:

```powershell
.\run-interface.bat 4180
```

The same path is available through npm:

```powershell
npm.cmd start
```

Open `index.html` directly in a browser for a quick static check, or run a
manual local static server from this folder:

```powershell
py -m http.server 4173
```

Then open:

```text
http://127.0.0.1:4173
```

## Test

Run the interface-local contract and browser smoke checks:

```powershell
npm test
```

The tests verify that the expected screens, lane controls, prompt surfaces,
draft-only run-planning controls, command preview, evidence handoff draft,
gallery cards, locked local execution gate, operator terminal, draft usage
counters, settings, tooltip styling, keybind registry, responsive breakpoint,
and local docs are present. The smoke test also opens the page in local
Microsoft Edge headless, clears the intro screen with `Enter`, toggles
mode/theme/density, changes lanes, selects all lanes, appends a template,
updates the run plan, fills evidence fields, verifies that the command draft
uses Workflow B lane ids and omits `--execute`, checks that the execution gate
is disabled, queues a draft with `Ctrl+Enter`, checks localStorage persistence,
checks mobile overflow, and saves screenshots.

The launcher and interface do not run VaultForge lane commands. They only make
the operator app available locally and prepare draft prompts, command text, and
handoff evidence. The Workflow B command draft uses `..\run_workflow_b.bat` so
it can be copied into a terminal opened from `interface/`; it emits full
Workflow B lane ids such as `vaultforge-engine`; it still omits `--execute`.

The operator terminal is a local draft log, not a real process terminal. It
records interface actions such as lane staging, template appends, copy actions,
and queued draft entries. The token counter is an approximate draft-size ticker
for prompt/command/handoff text until a future Workflow B usage feed is wired.

Headless render artifacts from the latest builder pass are kept under:

```text
tests/artifacts/
```

## Extension Notes

For small mod/plugin-style changes, see `docs/EXTENDING.md`.
