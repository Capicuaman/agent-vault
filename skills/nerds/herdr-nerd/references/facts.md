# Herdr facts snapshot

**Sources & capture dates:**
- https://herdr.dev/ — 2026-08-24 (vanity metrics may be stale)
- https://herdr.dev/docs/ — 2026-10-06
- https://herdr.dev/compare/ — 2026-10-06
- https://herdr.dev/blog/ — 2026-10-06
- https://herdr.dev/agent-guide.md — 2026-10-06 (authoritative — written for agents)
- Local: `03_RESOURCES/Software_Engineering/DEV/herdr/` (2026-10-02, grounded in a real session)

Snapshot. Treat `herdr --help`, `herdr --default-config`, and https://herdr.dev/docs/ as ground truth when they disagree.

## Identity
- **Tagline:** "The runtime coding agents run on."
- **One-liner:** terminal workspace manager for AI coding agents — a runtime, not an app.
- **Backer:** Y Combinator (Aug 2026) · **$6M seed from Bessemer Venture Partners** (Sep 2026).
- **License:** Apache 2.0.
- **Platforms:** macOS, Linux, Windows (WSL recommended; native via PowerShell or `install.cmd`).
- **i18n:** English, 日本語, 简体中文.
- **Community:** Discord link on site · `@herdrdev` on social · GitHub.
- **Homepage vanity (snapshot drift):** 31,600 → 42,441 stars between Aug and Oct 2026; 762+ community plugins; 20 agent CLIs detected out of the box.

## Versions
- **Latest stable:** 0.9.3 (as of 2026-10-06 docs).
- **Preview channel:** 0.9.2, 0.9.1, 0.9.0 preview builds.
- **Prior stable line:** 0.8.x (0.8.2 was homepage snapshot in August).
- **Historical:** 0.5.11 through 0.7.5 documented; local repo reference was v0.7.4.
- **Channel default:** direct installs are **stable**; preview is opt-in. Package-manager installs update through that package manager.
- **Check version:** `herdr --version`

## Install
```sh
# Linux / macOS
curl -fsSL https://herdr.dev/install.sh | sh

# Windows PowerShell
powershell -ExecutionPolicy Bypass -c "irm https://herdr.dev/install.ps1 | iex"

# Windows cmd (endpoint-protection fallback)
curl.exe -fsSLo install.cmd https://herdr.dev/install.cmd && install.cmd && del install.cmd
```
Also: **Homebrew, mise, Nix**, manual downloads. Full matrix: https://herdr.dev/docs/install/

## Architecture — the one paragraph
Herdr is a **runtime + clients**, not an app. A background **server** owns real PTYs; every UI — the TUI, the CLI, plain SSH, whatever ships next — is a **client that attaches**. The TUI is the first client, not the last. Clients can crash, detach, or get killed without the agents noticing. Default socket: `~/.config/herdr/herdr.sock`.

## Concept model (teach in this order)
1. **Session** — a persistent background server namespace. `herdr` attaches the default; `herdr session attach <name>` for isolated namespaces. Most people need only the default.
2. **Workspace** — the project-level container. One per repo/task. Owns tabs and panes. Sidebar rolls agent states up per workspace.
3. **Tab** — a layout inside a workspace (e.g. `agents`, `logs`, `server`).
4. **Pane** — a real terminal. Splittable right or down. Survives client detach.
5. **Agent** — a process Herdr recognizes inside a pane. **States: `working`, `blocked`, `done`, `idle`, `unknown`.** (Note: 5 states — `unknown` is real.)
6. **Modes** — three input modes:
   - **terminal mode** — keys go to the focused pane.
   - **prefix mode** — press `ctrl+b`, release, press one action key, send one command to Herdr.
   - **navigate mode** — persistent navigation surface.

## Nested-launch guard
If `HERDR_ENV=1` is set, you are **already inside a Herdr pane**. Herdr blocks nested launches by design — never run `herdr` from inside another herdr pane.

## Agent awareness
- Detects ~20 agent CLIs out of the box: Claude Code, Codex, Cursor, opencode, Grok, Copilot, Hermes, pi, and more. Full list: https://herdr.dev/docs/agents/
- State comes from screen detection by default; **integrations** add lifecycle state and/or native session restore.
- `herdr integration install claude` — adds Claude native session restore (state still from screen).
- `herdr integration status` — see which integrations are active.
- `herdr agent list` — what Herdr currently sees in panes.
- `herdr agent explain --json` — why the detector classified a pane the way it did.

## Agent-native API
- CLI and local socket API are the same surface agents drive.
- Verbs: **read · send · wait · split · attach**.
- Agents can split panes, start sibling agents, prompt each other, and wait until a peer is genuinely `blocked` instead of firing keystrokes and hoping.
- Herdr ships an **official agent skill** at `https://raw.githubusercontent.com/herdrdev/herdr/master/skills/herdr/SKILL.md` — teaches an agent to control Herdr from inside a pane.
- Install for Claude-ecosystem agents: `npx skills add herdrdev/herdr --skill herdr -g`
- For other agents: paste the GitHub skill into their custom instructions.

## Default keybinds (prefix `ctrl+b`)
- Split right: `prefix v`
- Split down: `prefix minus` (literally the `-` key)
- New tab: `prefix c`
- Next / prev tab: `prefix n` / `prefix p`
- Workspace nav: `prefix w`
- New workspace: `prefix SHIFT+n`
- Detach: `prefix q`
- **Show every active binding live: `prefix ?`**

## Mouse-first (don't forget)
"No keybindings are required to use Herdr." Click panes/tabs/workspaces, drag split borders, right-click menus, drag-select to copy, double-click a token to copy, ctrl-click opens links (shift-ctrl on Linux, shift-cmd on macOS fallback).

## Configuration
- **Linux/macOS:** `~/.config/herdr/config.toml`
- **Windows:** `%APPDATA%\herdr\config.toml`
- Works without a config file.
- Print default: `herdr --default-config`
- Reload live: `herdr server reload-config` (or global menu → reload config)
- Sections: `[keys]`, `[theme]`, `[ui]`, `[terminal]`, `[update]`
- Full reference: https://herdr.dev/docs/configuration/

## Logs & diagnostics
- Default session logs: `~/.config/herdr/` (Linux/mac) · `%APPDATA%\herdr\` (Windows)
- Named-session logs: under `sessions/<name>/` inside the above
- Status: `herdr status`, `herdr status server`, `herdr status client`

## Remote / "connecting machines" (Herdr 0.9 flagship)
- SSH into the machine and run `herdr` there (works like tmux).
- Or attach as thin local client: `herdr --remote user@host`.
- **Herdr 0.9 unified local + saved SSH machines in one TUI client**, with a combined agent list and independent reconnects.
- Flag: `--remote-keybindings local|server` (default `local`).
- Trade-offs: https://herdr.dev/docs/how-to-work/
- **Herdr Cloud** teased in the Sep 2026 blog post — hosted runtime direction.

## Plugins
- **Topic:** add `herdr-plugin` to a public GitHub repo.
- **Manifest:** `herdr-plugin.toml` at the repo root.
- **Install:** `herdr plugin install <...>`
- No submission queue, no review — index auto-refreshes.
- Marketplace at https://herdr.dev/plugins/ (launching with tagged repos).
- "Listings aren't reviewed by Herdr, so install at your own discretion."

## Session state — what survives
- **Detach** → everything.
- **Server restart** → persistent state restores (session restore).
- **Pane history replay** → yes.
- **Native agent resume** → via integrations (e.g. Claude).
- **Live binary handoff** → `herdr update --handoff` replaces the server during update while keeping pane processes alive (shipped May 2026).
- Full map: https://herdr.dev/docs/session-state/

## Core subcommands (quick index — see `commands.md` for examples)
- `herdr` · `herdr status [server|client]`
- `herdr server {start,stop,reload-config}`
- `herdr session {list,attach,stop,delete}`
- `herdr agent {list,explain --json}`
- `herdr integration {install,status}`
- `herdr plugin install`
- `herdr update [--handoff]`
- `herdr --remote user@host` · `--remote-keybindings local|server`
- `herdr --session <name>` · `--no-session` · `--default-config` · `--version`

## Docs structure (map for lookups)
- Install → https://herdr.dev/docs/install/
- Quick start → mouse-first path
- Concepts → https://herdr.dev/docs/concepts/
- Keyboard → https://herdr.dev/docs/keyboard/ (prefix explanations + safe chord picks)
- Agents → https://herdr.dev/docs/agents/
- Integrations → https://herdr.dev/docs/integrations/
- Connecting machines → local + SSH in one TUI
- Session state → https://herdr.dev/docs/session-state/
- Configuration → https://herdr.dev/docs/configuration/
- API → CLI + socket for scripts and agents
- Plugins → authoring + manifest + hooks
- Marketplace → publishing via GitHub topic
- How-to-work (remote trade-offs) → https://herdr.dev/docs/how-to-work/

## Roadmap teasers
- **Herdr Cloud** — hosted runtime, direction announced in "Connecting the machines" (Sep 7, 2026).
- **Marketplace launch** — tagged `herdr-plugin` repos auto-listed.
- **More clients** — "TUI · CLI · plain SSH, more coming" per the compare page.

## Known drifts between docs and reality

Findings from running `herdr-nerd-training/` on long-lived installations (2026-10-06):

### Env var injection drift
The agent-guide claims every managed pane gets `HERDR_ENV`, `HERDR_WORKSPACE_ID`, `HERDR_TAB_ID`, `HERDR_PANE_ID`. **Reality on older running servers:**
- Only `HERDR_ENV`, `HERDR_PANE_ID` are injected.
- `HERDR_SESSION` and `HERDR_SOCKET_PATH` are *also* injected (undocumented in the agent-guide).
- `HERDR_WORKSPACE_ID` and `HERDR_TAB_ID` are empty.
- Older servers also use pane ID form `p_N` instead of the new `w1:p1`.

When advising, ask the user what their env shows rather than assuming the agent-guide's shape.

### Protocol mismatch is the common failure mode
`herdr --version` reports the **CLI binary** version. The **server** keeps running across CLI updates until explicitly restarted or handoff-swapped. Over time, a mismatch builds. Diagnostic:
```sh
herdr api snapshot 2>&1 | head -3
# protocol_mismatch error → server is behind CLI
```

All `api`/`workspace`/`tab`/`pane`/`agent` CLI commands fail with `protocol_mismatch` when this happens. Session/pane keybinds inside the TUI still work (the TUI client speaks the server's protocol). Fix is a server restart (optionally via `herdr update --handoff`, which may not survive a major protocol jump).

### Workaround for learning without disruption
If a user's server is protocol-mismatched but they can't restart yet (long-running agent panes), suggest a **named workaround session**:
```sh
herdr --session fresh
```
The new session comes up on the current CLI's protocol; the old `one` session keeps running on its old protocol. All API drills work in `fresh` without touching live work.

### Rule for the nerd
When a user reports "the drill output doesn't match the doc," first instinct = **check server protocol**, not blame the doc. Then update the drill doc to reflect reality for both old-server and current-server cases.
