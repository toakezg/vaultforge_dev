# VaultForge Operator Interface

This folder contains the local operator UI for VaultForge.

The first slice is a dependency-free static app. It is intentionally separate
from engine, business, icon, XP4L, and art runtime behavior.

## Setup

Open `index.html` directly in a browser, or run a local static server from this
folder:

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
draft-only run-planning controls, command preview, gallery cards, settings,
tooltip styling, keybind registry, responsive breakpoint, and local docs are
present. The smoke test also opens the page in local Microsoft Edge headless,
clears the intro screen with `Enter`, toggles mode/theme/density, changes lanes,
appends a template, updates the run plan, verifies that the command draft omits
`--execute`, starts a draft with `Ctrl+Enter`, checks localStorage persistence,
checks mobile overflow, and saves screenshots.

Headless render artifacts from the latest builder pass are kept under:

```text
tests/artifacts/
```

## Extension Notes

For small mod/plugin-style changes, see `docs/EXTENDING.md`.
