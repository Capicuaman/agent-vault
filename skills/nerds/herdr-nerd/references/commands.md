# Herdr command cheatsheet (nerd-grade)

Grounded in https://herdr.dev/agent-guide.md, https://herdr.dev/docs/, and local reference at `03_RESOURCES/Software_Engineering/DEV/herdr/herdr-command-reference.md`. Prefer `herdr <cmd> --help` for authoritative, up-to-date flags.

## Daily entry
```sh
herdr                       # attach existing session, or launch TUI if none
herdr --session textdump    # named session per domain
herdr status                # workspaces, tabs, panes, agent states
herdr status server         # server-side runtime summary
herdr status client         # client-side state
```

## Nested-launch rule
If `echo $HERDR_ENV` prints `1`, you're already inside a Herdr pane. **Do not** run `herdr` again — nested launches are blocked by design.

## Server lifecycle
```sh
herdr server stop               # actually stop everything; detach only ends the client
herdr server reload-config      # apply ~/.config/herdr/config.toml edits live
```

## Sessions (named = isolated namespaces)
```sh
herdr session list
herdr session attach <name>
herdr session stop <name>
herdr session delete <name>
```
Most users only need the default. Reach for named sessions to isolate per-domain work (textdump, bilan, ricing, zapata, etc.).

## Agents
```sh
herdr agent list                      # what Herdr currently sees in panes
herdr agent explain --json            # why the detector classified a pane that way
```

## Integrations (add lifecycle state or native resume)
```sh
herdr integration status              # which integrations are active
herdr integration install claude      # Claude native session restore
```
State still comes from screen detection by default; integrations layer on top.

## Plugins
```sh
herdr plugin install <repo-or-manifest>
```
Discover at https://herdr.dev/plugins/ — any public GitHub repo with the `herdr-plugin` topic + a `herdr-plugin.toml` manifest. No review queue; install at your own discretion.

## Remote / "connecting machines" (0.9+)
```sh
ssh you@server                        # option 1: SSH in, run herdr locally on the box
herdr --remote you@server             # option 2: thin local client, remote server over SSH bridge
herdr --remote you@server --remote-keybindings server
```
In 0.9+, local and saved SSH machines appear in one TUI with a combined agent list.

## Update
```sh
herdr update                          # installer-managed update (stable by default)
herdr update --handoff                # live binary handoff — swap server, keep PTYs alive (May 2026)
```
Preview channel is opt-in. Package-manager installs update through that manager.

## Escape hatches
```sh
herdr --no-session                    # monolithic, no server/client split — loses persistence
herdr --default-config                # print full default config.toml to stdout
herdr --version                       # version check
```

## Default keybinds (prefix = `ctrl+b`)

| Action              | Keys                 |
|---------------------|----------------------|
| Split right         | `prefix v`           |
| Split down          | `prefix minus` (`-`) |
| New tab             | `prefix c`           |
| Next / prev tab     | `prefix n` / `p`     |
| Workspace picker    | `prefix w`           |
| New workspace       | `prefix SHIFT+n`     |
| Detach              | `prefix q`           |
| **Show all active bindings live** | `prefix ?` |

Mouse-first: every action above is also a click or right-click menu. No keybindings are required.

## Config

| OS            | Path                                          |
|---------------|-----------------------------------------------|
| Linux / macOS | `~/.config/herdr/config.toml`                 |
| Windows       | `%APPDATA%\herdr\config.toml`                 |

Sections: `[keys]`, `[theme]`, `[ui]`, `[terminal]`, `[update]`.

```sh
herdr --default-config > ~/.config/herdr/config.toml   # seed from defaults
herdr server reload-config                             # apply without restart
```

## Nerd patterns

### 1. Per-domain named sessions
```sh
herdr --session bilan        # all bilan work
herdr --session textdump     # knowledge garden ops
herdr session attach bilan   # jump back from anywhere
```

### 2. Install the official Herdr agent skill into yourself
Herdr ships a skill file at:
```
https://raw.githubusercontent.com/herdrdev/herdr/master/skills/herdr/SKILL.md
```
It teaches a coding agent to control Herdr from inside a pane (split, send, read, wait).

```sh
# For agents on the open skills CLI (claude, etc.)
npx skills add herdrdev/herdr --skill herdr -g
```
For other agents, paste the GitHub skill into their custom instructions.

### 3. Scripted drive via the socket
The CLI and the socket are the same surface agents drive. Anything the TUI does, a script can do:
```sh
herdr status --json | jq '.workspaces[] | select(.agents[]?.state == "blocked")'
herdr agent explain --json <pane-id>
```

### 4. State-aware context switching
Before pane-hunting, ask Herdr:
```sh
herdr status                 # look for `blocked`
herdr agent list             # one-line per agent across all workspaces
```
The sidebar rolls `working/blocked/done/idle/unknown` up to the workspace. Trust it.

### 5. Live config iteration
```sh
$EDITOR ~/.config/herdr/config.toml
herdr server reload-config
```
No restart, no PTY churn.

### 6. Worktree quest flow
See `03_RESOURCES/Software_Engineering/DEV/herdr/worktrees.md` and `worktree-quest-cli/` in-repo for the multi-worktree agent orchestration pattern.
