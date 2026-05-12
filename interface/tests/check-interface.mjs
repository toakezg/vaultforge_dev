import { readFileSync, existsSync } from "node:fs";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

const root = fileURLToPath(new URL("..", import.meta.url));

function read(name) {
  return readFileSync(join(root, name), "utf8");
}

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

const requiredFiles = [
  "index.html",
  "assets/vaultforge-intro.svg",
  "styles.css",
  "app.js",
  "docs/README.md",
  "docs/CHANGELOG.md",
  "docs/HOW_TO_USE.md",
  "docs/EXTENDING.md"
];

for (const file of requiredFiles) {
  assert(existsSync(join(root, file)), `missing ${file}`);
}

const html = read("index.html");
const css = read("styles.css");
const js = read("app.js");

for (const id of [
  "splash",
  "quickAccess",
  "laneGrid",
  "promptInput",
  "promptPreview",
  "commandDraft",
  "handoffDraft",
  "cycleCount",
  "timeboxMinutes",
  "hardGateMode",
  "commitMode",
  "evidenceFiles",
  "evidenceVerification",
  "evidenceBlocker",
  "evidenceNext",
  "galleryGrid",
  "settingsDialog",
  "keybindList"
]) {
  assert(html.includes(`id="${id}"`), `missing #${id}`);
}

for (const view of ["workshop", "lanes", "tools", "templates", "preview"]) {
  assert(html.includes(`data-view="${view}"`), `missing ${view} nav`);
}

for (const lane of ["engine", "business", "coding", "xp4l", "art", "icon"]) {
  assert(html.includes(`value="${lane}"`), `missing ${lane} lane`);
}

for (const variable of ["--bg", "--panel", "--accent", "--accent-2", "--good"]) {
  assert(css.includes(variable), `missing CSS variable ${variable}`);
}

assert(css.includes("@media (max-width: 720px)"), "missing mobile breakpoint");
assert(css.includes("[data-tooltip]"), "missing tooltip styling");
assert(css.includes("body.splashing"), "missing splash scroll lock");
assert(html.includes("assets/vaultforge-intro.svg"), "missing intro image asset");
assert(html.includes('aria-hidden="true"'), "missing initial app aria hide");
assert(js.includes("defaultKeybinds"), "missing keybind registry");
assert(js.includes("window.VaultForgeOperator"), "missing extension surface");
assert(js.includes("localStorage"), "missing persistent settings");
assert(js.includes("Ctrl+Enter"), "missing run keybind");
assert(js.includes("buildCommandDraft"), "missing command draft builder");
assert(js.includes("buildHandoffDraft"), "missing handoff draft builder");
assert(js.includes("renderGallery"), "missing preview gallery renderer");
assert(js.includes('event.key === "Enter"'), "missing Enter intro shortcut");
assert(js.includes("technical"), "missing technical mode");
assert(js.includes("natural"), "missing natural mode");
assert(js.includes("draft only, no local command is run"), "missing no-exec preview copy");
assert(js.includes("Evidence packet"), "missing evidence packet template");
assert(!js.includes("--execute"), "command drafts should not add execute flag");
assert(!html.includes("http://") && !html.includes("https://"), "interface should not depend on remote assets");

console.log("interface contract ok");
