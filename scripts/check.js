// Basic checks for every game (no dependencies needed):
//  1. The inline <script> parses without syntax errors.
//  2. No browser storage is used (the games keep all state in memory).
//  3. Every getElementById("...") / $("...") id used in the script exists in the HTML.
// Run with: npm test
const fs = require("fs");
const path = require("path");
const vm = require("vm");

const dir = path.join(__dirname, "..", "games");
const files = fs.readdirSync(dir).filter((f) => f.endsWith(".html"));
let failed = 0;

for (const file of files) {
  const html = fs.readFileSync(path.join(dir, file), "utf8");
  const problems = [];

  const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map((m) => m[1]);
  if (!scripts.length) problems.push("no inline <script> found");
  scripts.forEach((code, i) => {
    try { new vm.Script(code, { filename: `${file} <script ${i + 1}>` }); }
    catch (e) { problems.push(`syntax error: ${e.message}`); }
  });

  if (/localStorage|sessionStorage|indexedDB/.test(html)) problems.push("uses browser storage");

  const ids = new Set([...html.matchAll(/[\s'`]id="([^"$]+)"/g)].map((m) => m[1]));
  const used = new Set([...scripts.join("\n").matchAll(/(?:\$|getElementById)\("([^"]+)"\)/g)].map((m) => m[1]));
  for (const id of used) if (!ids.has(id)) problems.push(`script uses id "${id}" that is not in the static HTML (may be created at runtime; verify)`);

  if (problems.length) { failed++; console.log(`✗ ${file}`); problems.forEach((p) => console.log(`    - ${p}`)); }
  else console.log(`✓ ${file}`);
}

console.log(failed ? `\n${failed} file(s) need attention.` : `\nAll ${files.length} games passed.`);
process.exit(failed ? 1 : 0);
