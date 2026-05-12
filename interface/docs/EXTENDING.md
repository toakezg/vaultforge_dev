# Extending

This first interface slice is intentionally small, but it has simple extension
points for later mods or plugin-style additions.

## Safe Extension Points

- Add prompt snippets in `app.js` under the `templates` object.
- Add default shortcuts in `defaultKeybinds`.
- Add theme tokens in `styles.css` with a new `[data-theme="name"]` block.
- Add lane checkboxes in `index.html` and include matching prompt copy in
  `app.js`. Also update the `laneIds` map so command drafts use the
  controller's full Workflow B lane names.
- Add draft-only planning fields by extending `currentPlan()`,
  `buildCommandDraft()`, and the matching form controls in `index.html`.
- Add evidence or handoff fields by extending `currentEvidence()`,
  `buildHandoffDraft()`, and the matching form controls in `index.html`.
- Add preview/gallery cards by extending `renderGallery()` without wiring those
  cards to live VaultForge command execution.
- Add terminal-style draft log entries through `addTerminalEntry()` for local
  operator actions. Keep it honest: log draft/copy/queue activity unless a
  future approved task wires a real process feed.
- Extend the usage ticker through `estimateDraftTokens()` until a real Workflow
  B usage feed exists.
- Adjust the local app launcher in `scripts/launch-interface.mjs` or
  `run-interface.bat` when the interface needs a different static-serving path.

Runtime helpers are exposed on `window.VaultForgeOperator` for light local
experiments:

```js
window.VaultForgeOperator.appendTemplate("review");
window.VaultForgeOperator.setTheme("ember");
window.VaultForgeOperator.setMode("technical");
```

Keep extensions interface-local until a routed Workflow B task approves changes
to engine, business, icon, XP4L, art, or coding behavior.

Do not enable the disabled local execution gate or add `--execute` to command
drafts without a separate approved task.
