const storageKey = "vaultforge.operator.v1";

const defaultKeybinds = {
  run: "Ctrl+Enter",
  prompt: "Ctrl+K",
  settings: "Ctrl+,",
  workshop: "Ctrl+1",
  lanes: "Ctrl+2",
  tools: "Ctrl+3",
  templates: "Ctrl+4",
  preview: "Ctrl+5"
};

const templates = {
  build: "Build a scoped VaultForge interface slice.\n\nTarget lane:\nSuccess check:\nStop condition:\nEvidence to record:",
  tighten: "Tighten the operator interface for clarity, density, and keyboard use. Keep changes interface-local and verify responsive behavior.",
  test: "Run interface-local checks, verify the browser view, and record any gaps as follow-up tasks.",
  handoff: "## Multi-Agent Handoff\n\n- Task:\n- Current role:\n- Last verified state:\n- Files touched:\n- Verification run:\n- Blocker or decision:\n- Resume prompt:",
  review: "Review the current interface slice for scope drift, layout breaks, missing tests, and operator workflow gaps.",
  workflow: "Use Workflow B with switch-safe hard gates. Route work through THREAD_MAP.md, keep writes inside the interface lane, and end with evidence.",
  docs: "Update interface docs with setup, how to use, verification, and next safe work.",
  plan: "Run plan:\n- Cycle budget:\n- Lane scope:\n- Hard gate mode:\n- Verification:\n- Safe next action:",
  evidence: "Evidence packet:\n- Files touched:\n- Verification run:\n- Blocker or decision:\n- Resume prompt:"
};

const state = loadState();
const splash = document.querySelector("#splash");
const appShell = document.querySelector("#appShell");
const enterApp = document.querySelector("#enterApp");
const navToggle = document.querySelector("#navToggle");
const quickAccess = document.querySelector("#quickAccess");
const modeButtons = document.querySelectorAll("[data-mode]");
const modeSummary = document.querySelector("#modeSummary");
const activeViewLabel = document.querySelector("#activeViewLabel");
const themeSelect = document.querySelector("#themeSelect");
const laneGrid = document.querySelector("#laneGrid");
const laneSummary = document.querySelector("#laneSummary");
const selectCore = document.querySelector("#selectCore");
const promptInput = document.querySelector("#promptInput");
const promptPreview = document.querySelector("#promptPreview");
const commandDraft = document.querySelector("#commandDraft");
const handoffDraft = document.querySelector("#handoffDraft");
const copyPrompt = document.querySelector("#copyPrompt");
const copyCommand = document.querySelector("#copyCommand");
const copyHandoff = document.querySelector("#copyHandoff");
const clearPrompt = document.querySelector("#clearPrompt");
const runButton = document.querySelector("#runButton");
const runQueue = document.querySelector("#runQueue");
const cycleCount = document.querySelector("#cycleCount");
const timeboxMinutes = document.querySelector("#timeboxMinutes");
const hardGateMode = document.querySelector("#hardGateMode");
const commitMode = document.querySelector("#commitMode");
const evidenceFiles = document.querySelector("#evidenceFiles");
const evidenceVerification = document.querySelector("#evidenceVerification");
const evidenceBlocker = document.querySelector("#evidenceBlocker");
const evidenceNext = document.querySelector("#evidenceNext");
const galleryGrid = document.querySelector("#galleryGrid");
const settingsButton = document.querySelector("#settingsButton");
const settingsDialog = document.querySelector("#settingsDialog");
const densityToggle = document.querySelector("#densityToggle");
const keybindList = document.querySelector("#keybindList");

let captureAction = null;

function loadState() {
  try {
    return {
      mode: "natural",
      theme: "dark",
      dense: false,
      lanes: ["engine", "business"],
      prompt: "",
      plan: { cycles: "1", timebox: "30", gate: "switch-safe", commit: "review" },
      evidence: { files: "", verification: "npm.cmd test", blocker: "no hard gate", next: "" },
      keybinds: { ...defaultKeybinds },
      ...JSON.parse(localStorage.getItem(storageKey) || "{}")
    };
  } catch {
    return {
      mode: "natural",
      theme: "dark",
      dense: false,
      lanes: ["engine", "business"],
      prompt: "",
      plan: { cycles: "1", timebox: "30", gate: "switch-safe", commit: "review" },
      evidence: { files: "", verification: "npm.cmd test", blocker: "no hard gate", next: "" },
      keybinds: { ...defaultKeybinds }
    };
  }
}

function saveState() {
  localStorage.setItem(storageKey, JSON.stringify(state));
}

function hideSplash() {
  splash.classList.add("hidden");
  document.body.classList.remove("splashing");
  appShell.removeAttribute("aria-hidden");
}

function setMode(mode) {
  state.mode = mode;
  modeButtons.forEach((button) => button.classList.toggle("active", button.dataset.mode === mode));
  modeSummary.textContent = mode === "technical" ? "Technical" : "Natural";
  updatePreview();
  saveState();
}

function setTheme(theme) {
  state.theme = theme;
  document.documentElement.dataset.theme = theme;
  themeSelect.value = theme;
  saveState();
}

function updateLanes() {
  state.lanes = Array.from(laneGrid.querySelectorAll("input:checked")).map((input) => input.value);
  laneSummary.textContent = state.lanes.length ? state.lanes.join(" + ") : "none";
  updatePreview();
  saveState();
}

function currentPlan() {
  return {
    cycles: cycleCount.value || "1",
    timebox: timeboxMinutes.value || "30",
    gate: hardGateMode.value,
    commit: commitMode.value
  };
}

function currentEvidence() {
  return {
    files: evidenceFiles.value.trim(),
    verification: evidenceVerification.value.trim(),
    blocker: evidenceBlocker.value.trim(),
    next: evidenceNext.value.trim()
  };
}

function shortPrompt() {
  const firstLine = promptInput.value.trim().split("\n").find(Boolean);
  if (!firstLine) return "<task brief>";
  return firstLine.replaceAll('"', "'").slice(0, 96);
}

function buildCommandDraft() {
  const plan = currentPlan();
  const laneFlags = state.lanes.map((lane) => `--lane ${lane}`).join(" ");
  const lanes = laneFlags || "--lane interface";
  return `..\\run_workflow_b.bat --cycles ${plan.cycles} --timebox-minutes ${plan.timebox} --hard-gate-mode ${plan.gate} --commit-mode ${plan.commit} ${lanes} --task "${shortPrompt()}"`;
}

function buildHandoffDraft() {
  const evidence = currentEvidence();
  return [
    "## Multi-Agent Handoff",
    "",
    `- Task: ${shortPrompt()}`,
    "- Current role: interface builder.",
    `- Last verified state: ${promptInput.value.trim() ? "draft prompt and planning surface are ready for review" : "draft prompt still needs operator text"}.`,
    `- Files touched: ${evidence.files || "not recorded yet"}.`,
    `- Verification run: ${evidence.verification || "not recorded yet"}.`,
    `- Blocker or decision: ${evidence.blocker || "not recorded yet"}.`,
    `- Resume prompt: ${evidence.next || "review the interface-local draft and keep real execution gated"}.`
  ].join("\n");
}

function updatePlanState() {
  state.plan = currentPlan();
  updatePreview();
  saveState();
}

function updateEvidenceState() {
  state.evidence = currentEvidence();
  updatePreview();
  saveState();
}

function setView(view) {
  document.querySelectorAll(".nav-item").forEach((item) => {
    item.classList.toggle("active", item.dataset.view === view);
  });
  activeViewLabel.textContent = view[0].toUpperCase() + view.slice(1);
  const panel = document.querySelector(`[data-panel="${view}"]`);
  if (panel) {
    panel.scrollIntoView({ behavior: "smooth", block: "start" });
  }
}

function promptModeHeader() {
  if (state.mode === "technical") {
    return "Mode: technical\nInclude paths, commands, verification, and gate handling.";
  }

  return "Mode: natural\nUse plain operator language and keep choices easy to review.";
}

function updatePreview() {
  const laneText = state.lanes.length ? state.lanes.join(", ") : "unselected";
  const plan = currentPlan();
  const evidence = currentEvidence();
  const body = promptInput.value.trim() || "No prompt drafted yet.";
  const command = buildCommandDraft();
  promptPreview.textContent = `${promptModeHeader()}\nLanes: ${laneText}\nCycles: ${plan.cycles}\nTimebox minutes: ${plan.timebox}\nHard gate mode: ${plan.gate}\nCommit mode: ${plan.commit}\nExecution: draft only, no local command is run from this interface.\n\n${body}`;
  commandDraft.textContent = command;
  handoffDraft.textContent = buildHandoffDraft();
  state.prompt = promptInput.value;
  state.plan = plan;
  state.evidence = evidence;
  renderGallery(command, evidence);
  saveState();
}

function appendTemplate(name) {
  const current = promptInput.value.trim();
  const next = templates[name] || "";
  promptInput.value = current ? `${current}\n\n${next}` : next;
  promptInput.focus();
  updatePreview();
}

function startRun() {
  const item = document.createElement("li");
  const stamp = new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
  item.innerHTML = `<span>${state.lanes.join(" + ") || "unrouted"} draft</span><b>${stamp}</b>`;
  runQueue.prepend(item);
}

function renderGallery(command, evidence) {
  galleryGrid.innerHTML = "";
  const laneText = state.lanes.length ? state.lanes.join(" + ") : "unrouted";
  const cards = [
    ["Run plan", `${currentPlan().cycles} cycle, ${currentPlan().timebox} minute draft for ${laneText}`],
    ["Prompt preview", promptInput.value.trim() ? "Prompt body ready for review" : "Waiting for operator prompt text"],
    ["Command draft", command],
    ["Evidence", evidence.files || evidence.verification || evidence.blocker || evidence.next ? `${evidence.verification || "verification pending"}; ${evidence.blocker || "decision pending"}` : "Record files touched, tests run, blocker, and next prompt"],
    ["Handoff draft", "Copy-ready Workflow B handoff text is prepared below"]
  ];

  for (const [title, detail] of cards) {
    const card = document.createElement("article");
    card.className = "gallery-card";
    card.innerHTML = `<strong>${title}</strong><span>${detail}</span>`;
    galleryGrid.append(card);
  }
}

function normalizeKey(event) {
  const parts = [];
  if (event.ctrlKey) parts.push("Ctrl");
  if (event.altKey) parts.push("Alt");
  if (event.shiftKey) parts.push("Shift");
  if (event.metaKey) parts.push("Meta");

  const key = event.key.length === 1 ? event.key.toUpperCase() : event.key;
  if (!["Control", "Alt", "Shift", "Meta"].includes(key)) {
    parts.push(key);
  }

  return parts.join("+");
}

function handleAction(action) {
  const viewActions = ["workshop", "lanes", "tools", "templates", "preview"];
  if (action === "run") startRun();
  if (action === "prompt") promptInput.focus();
  if (action === "settings") openSettings();
  if (viewActions.includes(action)) setView(action);
}

function onKeydown(event) {
  if (!splash.classList.contains("hidden") && event.key === "Enter") {
    event.preventDefault();
    hideSplash();
    return;
  }

  const combo = normalizeKey(event);

  if (captureAction) {
    event.preventDefault();
    state.keybinds[captureAction] = combo;
    captureAction = null;
    renderKeybinds();
    saveState();
    return;
  }

  const action = Object.entries(state.keybinds).find(([, value]) => value === combo)?.[0];
  if (action) {
    event.preventDefault();
    handleAction(action);
  }
}

function renderKeybinds() {
  keybindList.innerHTML = "";
  Object.entries(state.keybinds).forEach(([action, combo]) => {
    const row = document.createElement("button");
    row.type = "button";
    row.className = "keybind-row";
    row.innerHTML = `<span>${action}</span><kbd>${captureAction === action ? "Press keys" : combo}</kbd>`;
    row.addEventListener("click", () => {
      captureAction = action;
      renderKeybinds();
    });
    keybindList.append(row);
  });
}

function openSettings() {
  renderKeybinds();
  if (typeof settingsDialog.showModal === "function") {
    settingsDialog.showModal();
  } else {
    settingsDialog.setAttribute("open", "");
  }
}

function syncFromState() {
  promptInput.value = state.prompt || "";
  state.plan = { cycles: "1", timebox: "30", gate: "switch-safe", commit: "review", ...(state.plan || {}) };
  state.evidence = { files: "", verification: "npm.cmd test", blocker: "no hard gate", next: "", ...(state.evidence || {}) };
  cycleCount.value = state.plan.cycles;
  timeboxMinutes.value = state.plan.timebox;
  hardGateMode.value = state.plan.gate;
  commitMode.value = state.plan.commit;
  evidenceFiles.value = state.evidence.files;
  evidenceVerification.value = state.evidence.verification;
  evidenceBlocker.value = state.evidence.blocker;
  evidenceNext.value = state.evidence.next;
  laneGrid.querySelectorAll("input").forEach((input) => {
    input.checked = state.lanes.includes(input.value);
  });
  setTheme(state.theme);
  setMode(state.mode);
  document.body.classList.toggle("dense", Boolean(state.dense));
  densityToggle.checked = Boolean(state.dense);
  updateLanes();
  updatePreview();
}

enterApp.addEventListener("click", hideSplash);
window.addEventListener("load", () => window.setTimeout(hideSplash, 900));
navToggle.addEventListener("click", () => quickAccess.classList.toggle("collapsed"));
settingsButton.addEventListener("click", openSettings);
document.addEventListener("keydown", onKeydown);

modeButtons.forEach((button) => {
  button.addEventListener("click", () => setMode(button.dataset.mode));
});

document.querySelectorAll(".nav-item").forEach((item) => {
  item.addEventListener("click", () => setView(item.dataset.view));
});

document.querySelectorAll("[data-template]").forEach((button) => {
  button.addEventListener("click", () => appendTemplate(button.dataset.template));
});

themeSelect.addEventListener("change", () => setTheme(themeSelect.value));
laneGrid.addEventListener("change", updateLanes);
cycleCount.addEventListener("input", updatePlanState);
timeboxMinutes.addEventListener("input", updatePlanState);
hardGateMode.addEventListener("change", updatePlanState);
commitMode.addEventListener("change", updatePlanState);
evidenceFiles.addEventListener("input", updateEvidenceState);
evidenceVerification.addEventListener("input", updateEvidenceState);
evidenceBlocker.addEventListener("input", updateEvidenceState);
evidenceNext.addEventListener("input", updateEvidenceState);
selectCore.addEventListener("click", () => {
  laneGrid.querySelectorAll("input").forEach((input) => {
    input.checked = ["engine", "business", "coding"].includes(input.value);
  });
  updateLanes();
});

promptInput.addEventListener("input", updatePreview);
clearPrompt.addEventListener("click", () => {
  promptInput.value = "";
  updatePreview();
});

copyPrompt.addEventListener("click", async () => {
  await navigator.clipboard?.writeText(promptPreview.textContent);
});

copyCommand.addEventListener("click", async () => {
  await navigator.clipboard?.writeText(commandDraft.textContent);
});

copyHandoff.addEventListener("click", async () => {
  await navigator.clipboard?.writeText(handoffDraft.textContent);
});

runButton.addEventListener("click", startRun);
densityToggle.addEventListener("change", () => {
  state.dense = densityToggle.checked;
  document.body.classList.toggle("dense", state.dense);
  saveState();
});

window.VaultForgeOperator = {
  appendTemplate,
  defaultKeybinds,
  setMode,
  setTheme,
  state,
  templates
};

syncFromState();
