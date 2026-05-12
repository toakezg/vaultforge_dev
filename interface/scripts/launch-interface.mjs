import { createServer } from "node:http";
import { readFileSync } from "node:fs";
import { extname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { spawn } from "node:child_process";

const root = fileURLToPath(new URL("..", import.meta.url));
const rootPath = resolve(root);
const requestedPort = Number.parseInt(process.env.VAULTFORGE_INTERFACE_PORT || process.argv[2] || "4173", 10);
const port = Number.isFinite(requestedPort) ? requestedPort : 4173;
const shouldOpen = !process.argv.includes("--no-open");

function contentType(filePath) {
  return {
    ".css": "text/css; charset=utf-8",
    ".html": "text/html; charset=utf-8",
    ".js": "text/javascript; charset=utf-8",
    ".svg": "image/svg+xml; charset=utf-8"
  }[extname(filePath)] || "application/octet-stream";
}

function openBrowser(url) {
  if (!shouldOpen) return;
  const command = process.platform === "win32" ? "cmd" : process.platform === "darwin" ? "open" : "xdg-open";
  const args = process.platform === "win32" ? ["/c", "start", "", url] : [url];
  const child = spawn(command, args, { detached: true, stdio: "ignore" });
  child.unref();
}

const server = createServer((request, response) => {
  const requestUrl = new URL(request.url || "/", "http://127.0.0.1");
  const requested = requestUrl.pathname === "/" ? "index.html" : decodeURIComponent(requestUrl.pathname.slice(1));
  const filePath = resolve(rootPath, requested);

  if (filePath !== rootPath && !filePath.startsWith(`${rootPath}\\`) && !filePath.startsWith(`${rootPath}/`)) {
    response.writeHead(403);
    response.end("Forbidden");
    return;
  }

  try {
    const body = readFileSync(filePath);
    response.writeHead(200, {
      "Content-Type": contentType(filePath),
      "Cache-Control": "no-store"
    });
    response.end(body);
  } catch {
    response.writeHead(404);
    response.end("Not found");
  }
});

server.listen(port, "127.0.0.1", () => {
  const address = server.address();
  const url = `http://127.0.0.1:${address.port}/`;
  console.log(`VaultForge Operator Interface: ${url}`);
  console.log("Press Ctrl+C to stop the local interface server.");
  openBrowser(url);
});

server.on("error", (error) => {
  console.error(`Unable to launch VaultForge Operator Interface on 127.0.0.1:${port}`);
  console.error(error.message);
  process.exitCode = 1;
});
