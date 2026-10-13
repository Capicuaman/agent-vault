# REA nerd — commands cheatsheet

**Snapshot date:** 2026-10-09  
**Grounding:** `03_RESOURCES/AI/rea/source-snapshots/2026-10-09/docs/installation.md`, `docs/cli.md`, README, npm metadata.

Do not run setup, install packages, or analyze targets without the user’s approval. REA can modify agent configuration and runtime captures can execute selected targets.

## Daily-entry commands

### Guided setup

```bash
npx rea-agents setup
```

REA shows its own setup plan and asks before changing agent configuration or installing optional tooling.

### Explicit latest setup

```bash
npx rea-agents@latest setup
```

Use this when you intentionally want npm latest instead of a project-local package version.

### One-off static JavaScript/Electron analysis

```bash
npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/app --json
```

This is the preferred first experiment because it can inspect an extracted JS/Electron app directory or ASAR without a native reverse-engineering engine.

### Install the shell-visible CLI

```bash
npm install --global rea-agents
rea --help
```

### Update an npm-installed CLI

```bash
rea update
```

Then run the setup command printed by the update to refresh agent registrations.

## Setup / registration inspection

### Dry-run or scoped setup patterns

```bash
npx rea-agents@latest setup --help
npx rea-agents@latest setup --dry-run --json
```

Use setup output as a review artifact before applying changes.

### Skill-only install

```bash
npx skills add morluto/rea --skill reverse-engineer-anything
```

This installs instructions only; it does not register REA’s MCP server or install analysis engines.

### Doctor / readiness

```bash
rea doctor --json
rea doctor --provider ghidra --json
rea doctor --client codex --json
```

Substitute the provider/client. Doctor checks files/prerequisites; it does not necessarily prove live MCP tools are connected in the current agent session.

## CLI inspection commands

### Generic analysis

```bash
rea analyze /absolute/path/to/target --json
```

For extracted directories and ASAR files, `rea analyze PATH` can select the JavaScript workflow when no provider/snapshot is supplied.

### Native analysis with provider

```bash
rea analyze /absolute/path/to/program --provider ghidra --json
rea analyze /absolute/path/to/program --provider hopper --json
rea analyze /absolute/path/to/program --provider ida --json
```

### Native focused queries

```bash
rea search /absolute/path/to/program "search" --provider ghidra --json
rea function /absolute/path/to/program main --provider ghidra --json
rea decompile /absolute/path/to/program 0x1000 --provider ghidra --json
rea instructions /absolute/path/to/program 0x1000 --provider ghidra --json
rea xrefs /absolute/path/to/program 0x1000 --provider ghidra --json
rea trace /absolute/path/to/program "search" --provider ghidra --json
```

## Provider selection

### List provider capabilities

```bash
rea providers --json
rea capabilities --json
```

### Set standing provider preference

```bash
export REA_ANALYSIS_PROVIDER=ghidra
rea analyze /absolute/path/to/program --json
```

An explicit `--provider` overrides `REA_ANALYSIS_PROVIDER`.

## Snapshots and Evidence

### Save and reuse analysis snapshots

```bash
rea analyze /absolute/path/to/program --provider ghidra --snapshot /absolute/path/to/analysis/program.json
rea analyze /absolute/path/to/program --provider ghidra --snapshot /absolute/path/to/analysis/program.json
```

The second command can reuse exact cached results when target bytes, operation, parameters, provider, and settings match.

### Import/export/compare Evidence bundles

```bash
rea evidence-import /absolute/path/to/evidence/bundle.json
rea evidence-export /absolute/path/to/evidence/bundle.json /absolute/path/to/evidence/canonical.json
rea compare /absolute/path/to/evidence/left.json /absolute/path/to/evidence/right.json
```

### Preserve failure status through formatters

```bash
set -o pipefail
rea inspect-artifact ./app.asar --json | jq . > inspection.json
```

## Historical-source comparison

```bash
rea import-reference-source /absolute/path/to/source
```

Optional secret-pattern exclusion:

```bash
export REA_REFERENCE_SECRET_PATTERNS_JSON='["**/.env", "**/secrets/**"]'
rea import-reference-source /absolute/path/to/source
```

## Agent-client setup values from docs snapshot

| Client | `--client` value |
|---|---|
| Claude Code | `claude_code` |
| Claude Desktop | `claude_desktop` |
| Codex | `codex` |
| Cursor | `cursor` |
| Gemini CLI | `gemini_cli` |
| Windsurf | `windsurf` |
| Devin | `devin` |
| OpenCode | `opencode` |
| Antigravity | `antigravity` |
| GitHub Copilot CLI | `copilot_cli` |
| Command Code | `commandcode` |
| VS Code | `vscode` |
| Grok Build | `grok_build` |
| OMP | `omp` |

## Nerd patterns

### Pattern 1 — Low-risk first contact

```bash
# 1. Read setup plan first.
npx rea-agents@latest setup --dry-run --json

# 2. If you only need static JS inspection, skip MCP setup and run a one-off command.
npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/app --json > rea-js-analysis.json
```

Why: avoids changing agent configuration before proving value.

### Pattern 2 — Evidence-first reconstruction

Ask the agent:

```text
Use REA to inspect <target>. Show the evidence for how <feature> works, list unknowns, and only then propose an implementation plan.
```

Why: forces REA’s evidence contract to shape the answer rather than letting the agent hallucinate internals.

### Pattern 3 — Provider-specific native pass

```bash
rea providers --json
rea doctor --provider ghidra --json
rea analyze /absolute/path/to/program --provider ghidra --snapshot /absolute/path/to/analysis/program.json --json
```

Why: provider health and snapshots make repeated native queries less chaotic.

### Pattern 4 — TextDump adoption path

```text
1. Review 03_RESOURCES/AI/rea/rea-onboarding.md.
2. Ask rea-nerd for a setup dry-run plan.
3. Choose one client and one target type.
4. Run no install/setup until the plan is reviewed.
5. Record results under 03_RESOURCES/AI/rea/ or 01_PROJECTS/AI_Agents/WORKING/rea-evaluation/ if it becomes active work.
```

## Ground truth reminder

When installed, `rea --help` and `rea <command> --help` are the final authority for CLI flags in that installed version. Refresh source docs before answering “latest” questions.
