# REA nerd — facts snapshot

**Snapshot date:** 2026-10-09  
**Canonical repo:** https://github.com/morluto/rea  
**Website:** https://rea.tools/  
**npm package:** https://www.npmjs.com/package/rea-agents  
**Local onboarding packet:** `03_RESOURCES/AI/rea/rea-onboarding.md`  
**Local source snapshot:** `03_RESOURCES/AI/rea/source-snapshots/2026-10-09/`

Treat this as a dated snapshot. For “latest” questions, refresh GitHub/npm/docs before answering.

## Identity

REA — **Reverse Engineer Anything** — is a TypeScript/npm CLI and MCP server that lets agents inspect software artifacts and return evidence-backed reverse-engineering findings. It connects agents to static and runtime workflows for native binaries, JavaScript/Electron apps, websites, .NET assemblies, Android APKs, firmware, network captures, crashes, process behavior, and related targets. REA is not itself “the decompiler”; it orchestrates engines and workflows such as Ghidra/Hopper/IDA, browser capture, static JS analysis, and Evidence contracts so the agent can ask focused questions and show what supports each conclusion.

## Key facts

| Thing | Value |
|---|---|
| Canonical name | REA: Reverse Engineer Anything |
| Repo | `morluto/rea` |
| Repo URL | https://github.com/morluto/rea |
| Website | https://rea.tools/ |
| npm package | `rea-agents` |
| npm version at snapshot | `6.3.0` |
| CLI binaries | `rea`, `rea-agents` |
| License | MIT |
| Main language | TypeScript |
| Node requirement | `^22.19.0 || ^24.11.0 || >=26.0.0` |
| Setup command | `npx rea-agents setup` |
| Explicit latest setup | `npx rea-agents@latest setup` |
| Global install | `npm install --global rea-agents` |
| GitHub stars at snapshot | 47,552 |
| Forks at snapshot | 7,766 |
| Open issues at snapshot | 97 |
| Default branch | `main` |
| Local packet | `03_RESOURCES/AI/rea/rea-onboarding.md` |

## Install modes

| Mode | Command | What it means |
|---|---|---|
| Guided setup | `npx rea-agents setup` | Downloads/runs npm-selected package, then REA shows its own plan before changing agent config or installing optional tools. |
| Explicit latest setup | `npx rea-agents@latest setup` | Same idea, but requests npm latest explicitly. |
| One-off CLI | `npx -y rea-agents@latest <command>` | Runs without global install; useful for isolated static analysis. |
| Global CLI | `npm install --global rea-agents` | Makes `rea` shell-visible. |
| Curl wrapper | `curl -fsSL https://raw.githubusercontent.com/morluto/rea/main/install.sh | bash` | Installs the global npm package, prints version/runtime/npm/destination, then starts setup when interactive. |
| Skill-only | `npx skills add morluto/rea --skill reverse-engineer-anything` | Installs agent instructions only, not MCP registration or engines. |

Important setup boundary from docs: npm approval to download the package is not the same as approving REA’s own setup changes. REA shows a setup plan and asks before modifying agent config or installing Hopper.

## Architecture / mental model

REA has four practical layers:

1. **Target** — artifact or system being inspected: binary, `.app`, ASAR, Electron directory, website, HAR, APK, firmware, process run, crash record, etc.
2. **Provider/workflow** — how REA inspects the target: static JavaScript analysis, browser/CDP capture, native provider through Ghidra/Hopper/IDA, process capture, and so on.
3. **Evidence contract** — results retain artifact identity, observations, source locations, inferences, warnings, unknowns, and limitations.
4. **Agent/CLI surface** — agent calls MCP tools or user runs CLI commands; the agent uses evidence to explain, ask follow-ups, or implement a similar feature.

## What REA can analyze

From the README snapshot, targets include:

| Target | Examples of returned information | Notes |
|---|---|---|
| Native binaries | pseudocode, assembly, strings, symbols, calls, xrefs | Requires Hopper, Ghidra, or IDA. |
| JavaScript / Electron | modules, imports, source maps, routes, IPC, native add-ons | Node/npm; static path can be low-risk first test. |
| Websites | page structure, scripts, network observations, screenshots | Chrome-family browser. |
| Saved network captures | requests, responses, exposed payloads, source locations | HAR; mitmdump for native mitmproxy captures on Linux. |
| .NET assemblies | metadata, CIL, native dependencies, build comparisons | Static only. |
| Android APKs | manifest, classes, decompiled methods, references | Headless JADX + full JDK. |
| Firmware | regions, extraction results, native-analysis handoffs | Binwalk/Unblob on Linux. |
| Process behavior | terminal output, interactions, exit/filesystem observations | Linux/macOS native PTY. |

## Prior-art position

REA complements standard reverse-engineering tools. It is not a replacement for Ghidra, Hopper, IDA, DevTools, mitmproxy, or static analyzers. It is an agent-facing orchestration layer that makes those workflows accessible through CLI/MCP and returns evidence a model can cite.

## Source priority for future answers

1. Local packet: `03_RESOURCES/AI/rea/rea-onboarding.md`
2. Local snapshot: `03_RESOURCES/AI/rea/source-snapshots/2026-10-09/`
3. Repo/docs: https://github.com/morluto/rea and https://rea.tools/
4. npm metadata: https://www.npmjs.com/package/rea-agents
5. Installed CLI after explicit user approval: `rea --help`, `rea <command> --help`, `rea doctor --json`

## Known caveats

- REA changes quickly; repository `main`, docs, npm latest, and active MCP server can disagree.
- Agent setup may edit config files and requires explicit review/approval.
- Native analysis requires external engines and host support; provider failures do not invalidate unrelated static workflows.
- Runtime capture can execute or interact with selected targets using the user’s permissions.
- This project-local nerd cites textDump paths; promote global only after making references self-contained.
