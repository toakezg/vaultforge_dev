import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { createServer, get } from "node:http";
import { extname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { spawn } from "node:child_process";

const root = fileURLToPath(new URL("..", import.meta.url));
const artifacts = join(root, "tests", "artifacts");
const edge = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe";
const profile = join(artifacts, "edge-profile");
const port = 9339;
const rootPath = resolve(root);

mkdirSync(profile, { recursive: true });

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

function fetchJson(target) {
  return new Promise((resolveFetch, reject) => {
    get(target, (response) => {
      let body = "";
      response.setEncoding("utf8");
      response.on("data", (chunk) => {
        body += chunk;
      });
      response.on("end", () => {
        try {
          resolveFetch(JSON.parse(body));
        } catch (error) {
          reject(error);
        }
      });
    }).on("error", reject);
  });
}

function wait(ms) {
  return new Promise((resolveWait) => setTimeout(resolveWait, ms));
}

function contentType(filePath) {
  return {
    ".css": "text/css",
    ".html": "text/html",
    ".js": "text/javascript",
    ".svg": "image/svg+xml"
  }[extname(filePath)] || "application/octet-stream";
}

function serveInterface() {
  const server = createServer((request, response) => {
    const requestUrl = new URL(request.url || "/", "http://127.0.0.1");
    const requested = requestUrl.pathname === "/" ? "index.html" : decodeURIComponent(requestUrl.pathname.slice(1));
    const filePath = resolve(rootPath, requested);

    if (filePath !== rootPath && !filePath.startsWith(`${rootPath}\\`)) {
      response.writeHead(403);
      response.end("Forbidden");
      return;
    }

    try {
      const body = readFileSync(filePath);
      response.writeHead(200, { "Content-Type": contentType(filePath) });
      response.end(body);
    } catch {
      response.writeHead(404);
      response.end("Not found");
    }
  });

  return new Promise((resolveServer, reject) => {
    server.on("error", reject);
    server.listen(0, "127.0.0.1", () => {
      const address = server.address();
      resolveServer({ server, url: `http://127.0.0.1:${address.port}/index.html` });
    });
  });
}

async function waitForTarget() {
  const started = Date.now();
  while (Date.now() - started < 10000) {
    try {
      const targets = await fetchJson(`http://127.0.0.1:${port}/json/list`);
      const page = targets.find((target) => target.type === "page");
      if (page?.webSocketDebuggerUrl) {
        return page.webSocketDebuggerUrl;
      }
    } catch {
      await wait(150);
    }
  }
  throw new Error("Edge CDP target did not start");
}

function createClient(wsUrl) {
  const ws = new WebSocket(wsUrl);
  let id = 0;
  const pending = new Map();

  ws.addEventListener("message", (event) => {
    const message = JSON.parse(event.data);
    if (!message.id || !pending.has(message.id)) {
      return;
    }
    const { resolve: resolvePending, reject } = pending.get(message.id);
    pending.delete(message.id);
    if (message.error) {
      reject(new Error(`${message.error.message}: ${message.error.data || ""}`));
    } else {
      resolvePending(message.result || {});
    }
  });

  return new Promise((resolveClient, reject) => {
    ws.addEventListener("open", () => {
      resolveClient({
        send(method, params = {}) {
          const currentId = ++id;
          ws.send(JSON.stringify({ id: currentId, method, params }));
          return new Promise((resolveSend, rejectSend) => {
            pending.set(currentId, { resolve: resolveSend, reject: rejectSend });
          });
        },
        close() {
          ws.close();
        }
      });
    });
    ws.addEventListener("error", reject);
  });
}

async function evaluate(client, expression) {
  const result = await client.send("Runtime.evaluate", {
    expression,
    awaitPromise: true,
    returnByValue: true
  });
  if (result.exceptionDetails) {
    throw new Error(result.exceptionDetails.exception?.description || result.exceptionDetails.text || "Runtime evaluation failed");
  }
  return result.result?.value;
}

async function key(client, key, modifiers = 0) {
  const code = key === "Enter" ? "Enter" : `Key${key.toUpperCase()}`;
  const windowsVirtualKeyCode = key === "Enter" ? 13 : key.toUpperCase().charCodeAt(0);
  await client.send("Input.dispatchKeyEvent", {
    type: "keyDown",
    key,
    code,
    windowsVirtualKeyCode,
    modifiers
  });
  await client.send("Input.dispatchKeyEvent", {
    type: "keyUp",
    key,
    code,
    windowsVirtualKeyCode,
    modifiers
  });
}

async function screenshot(client, name) {
  const image = await client.send("Page.captureScreenshot", { format: "png" });
  writeFileSync(join(artifacts, name), Buffer.from(image.data, "base64"));
}

const appServer = await serveInterface();
const child = spawn(edge, [
  "--headless=new",
  "--disable-gpu",
  "--allow-file-access-from-files",
  "--remote-allow-origins=*",
  `--remote-debugging-port=${port}`,
  `--user-data-dir=${profile}`,
  "--window-size=1280,900",
  appServer.url
], { stdio: "ignore" });

let client;
try {
  client = await createClient(await waitForTarget());
  await client.send("Page.enable");
  await client.send("Runtime.enable");
  await client.send("Emulation.setDeviceMetricsOverride", {
    width: 1280,
    height: 900,
    deviceScaleFactor: 1,
    mobile: false
  });
  await evaluate(client, "localStorage.removeItem('vaultforge.operator.v1'); location.reload();");
  await wait(700);

  assert(await evaluate(client, "document.body.classList.contains('splashing')"), "splash should lock scroll before entry");
  await key(client, "Enter");
  await wait(150);
  assert(await evaluate(client, "document.querySelector('#splash').classList.contains('hidden')"), "Enter should hide splash");
  assert(await evaluate(client, "!document.body.classList.contains('splashing')"), "splash scroll lock should clear");

  await evaluate(client, "document.querySelector('[data-mode=\"technical\"]').click();");
  assert(await evaluate(client, "document.querySelector('#modeSummary').textContent === 'Technical'"), "technical mode should activate");

  await evaluate(client, "const select = document.querySelector('#themeSelect'); select.value = 'ember'; select.dispatchEvent(new Event('change'));");
  assert(await evaluate(client, "document.documentElement.dataset.theme === 'ember'"), "theme should change");

  await evaluate(client, "document.querySelector('#settingsButton').click(); document.querySelector('#densityToggle').click();");
  assert(await evaluate(client, "document.body.classList.contains('dense')"), "density toggle should apply");
  await evaluate(client, "document.querySelector('#settingsDialog').close();");

  await evaluate(client, "document.querySelector('input[value=\"business\"]').click(); document.querySelector('input[value=\"coding\"]').click();");
  assert(await evaluate(client, "document.querySelector('#laneSummary').textContent === 'engine + coding'"), "lane summary should update");

  await evaluate(client, "document.querySelector('[data-template=\"build\"]').click();");
  assert(await evaluate(client, "document.querySelector('#promptInput').value.includes('Target lane:')"), "template should append to input");
  assert(await evaluate(client, "document.querySelector('#promptPreview').textContent.includes('Mode: technical')"), "preview should reflect mode");
  await evaluate(client, "document.querySelector('#cycleCount').value = '3'; document.querySelector('#cycleCount').dispatchEvent(new Event('input'));");
  await evaluate(client, "document.querySelector('#timeboxMinutes').value = '45'; document.querySelector('#timeboxMinutes').dispatchEvent(new Event('input'));");
  await evaluate(client, "const gate = document.querySelector('#hardGateMode'); gate.value = 'stop'; gate.dispatchEvent(new Event('change'));");
  await evaluate(client, "document.querySelector('#evidenceFiles').value = 'app.js, docs'; document.querySelector('#evidenceFiles').dispatchEvent(new Event('input'));");
  await evaluate(client, "document.querySelector('#evidenceVerification').value = 'npm.cmd test'; document.querySelector('#evidenceVerification').dispatchEvent(new Event('input'));");
  await evaluate(client, "document.querySelector('#evidenceNext').value = 'review scoped interface slice'; document.querySelector('#evidenceNext').dispatchEvent(new Event('input'));");
  assert(await evaluate(client, "document.querySelector('#promptPreview').textContent.includes('Cycles: 3')"), "preview should include cycle plan");
  assert(await evaluate(client, "document.querySelector('#commandDraft').textContent.includes('--cycles 3')"), "command draft should include cycles");
  assert(await evaluate(client, "!document.querySelector('#commandDraft').textContent.includes('--execute')"), "command draft should not execute");
  assert(await evaluate(client, "document.querySelector('#handoffDraft').textContent.includes('npm.cmd test')"), "handoff draft should include evidence");
  assert(await evaluate(client, "document.querySelectorAll('#galleryGrid .gallery-card').length >= 5"), "gallery should render planning and evidence cards");

  await key(client, "Enter", 2);
  await wait(150);
  assert(await evaluate(client, "document.querySelector('#runQueue li span').textContent.includes('engine + coding')"), "Ctrl+Enter should add a run draft");

  await evaluate(client, "location.reload();");
  await wait(900);
  assert(await evaluate(client, "document.documentElement.dataset.theme === 'ember'"), "theme should persist");
  assert(await evaluate(client, "document.body.classList.contains('dense')"), "density should persist");
  assert(await evaluate(client, "document.querySelector('#promptInput').value.includes('Target lane:')"), "prompt should persist");
  assert(await evaluate(client, "document.querySelector('#cycleCount').value === '3'"), "run plan should persist");
  assert(await evaluate(client, "document.querySelector('#evidenceFiles').value.includes('app.js')"), "evidence files should persist");
  await key(client, "Enter");
  await wait(150);
  await evaluate(client, "window.scrollTo(0, 0);");

  await screenshot(client, "operator-smoke-desktop.png");
  await client.send("Emulation.setDeviceMetricsOverride", {
    width: 390,
    height: 900,
    deviceScaleFactor: 1,
    mobile: true
  });
  await wait(250);
  await evaluate(client, "window.scrollTo(0, 0);");
  assert(await evaluate(client, "document.documentElement.scrollWidth <= window.innerWidth + 1"), "mobile layout should not overflow horizontally");
  await screenshot(client, "operator-smoke-mobile.png");

  console.log("interface browser smoke ok");
} finally {
  client?.close();
  child.kill();
  appServer.server.close();
}
