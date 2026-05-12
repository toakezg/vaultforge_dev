# How To Use

1. Open the app and let the intro screen clear, or press `Enter`.
2. Use quick access on the left to jump between Workshop, Lanes, Tools,
   Templates, and Preview.
3. Choose one or more lanes in the lane panel.
4. Pick Natural or Technical mode from the top bar.
5. Use template buttons to assemble a prompt, or type directly in the input.
6. Set the local run plan: cycle count, timebox, hard-gate mode, and commit
   mode.
7. Fill the evidence fields for files touched, verification, blocker or
   decision, and next action when preparing a handoff.
8. Review the generated run draft, command draft, evidence handoff, and preview
   gallery.
9. Press `Start run` or `Ctrl+Enter` to add a local draft entry.
10. Open Settings to change theme, density, and keybinds.

Default keybinds:

```text
Ctrl+Enter  Start run
Ctrl+K      Focus prompt input
Ctrl+,      Open settings
Ctrl+1      Workshop
Ctrl+2      Lanes
Ctrl+3      Tools
Ctrl+4      Templates
Ctrl+5      Preview
```

This interface does not execute VaultForge lane commands. The command surface is
a draft-only planning aid and intentionally omits `--execute`.

Small mod and plugin-style additions are documented in `EXTENDING.md`.
