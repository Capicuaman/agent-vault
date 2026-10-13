# Herdr vs. the field

Grounded in https://herdr.dev/compare/ (captured 2026-10-06). 9 tools in the matrix. One-liners at the bottom.

## The frame
Most tools Herdr gets compared to are **apps**: a window you open to manage coding agents, and a window the work depends on. Herdr is a **runtime**: a server holds real terminals on the machine, agents live in those, and every UI — Herdr's TUI included — is just a client that attaches. The row that sorts the field is "**what happens to the agents when the thing you're looking at goes away?**"

## The matrix

| Capability | **Herdr** | tmux · Zellij | cmux · Warp | Solo | Conductor · Emdash · Superset |
|---|---|---|---|---|---|
| Kind of thing | runtime + clients | terminal multiplexer | terminal app | process dashboard | manager app |
| Work survives its own UI closing | **yes — server owns the terminals** | yes, detach | session restore while app is open | while app is open | while app is open |
| Runs inside your existing terminal | **yes** | yes | replaces it | no, desktop app | no, desktop app |
| Semantic agent state | **blocked · working · done · idle** | — | attention cues | process status | workspace status |
| Detach, reattach, SSH in | **yes, any tty** | yes | partial | — | remote projects |
| Direct attach to one agent | **yes** | — | — | — | — |
| API agents drive themselves | **read · send · wait · split · attach** | terminal scripting | app APIs | MCP for processes | workflow APIs |
| Worktree + diff review flow | pairs with it | — | partial | — | **yes, their core** |
| Clients on the same runtime | **TUI · CLI · plain SSH, more coming** | its own client | the app only | the app only | the app only |

## One-liners

- **vs tmux** — tmux keeps terminals alive; so does Herdr. The difference is Herdr knows which terminals are agents, what state each one is in, and how to wait on them. tmux sees panes.
- **vs Zellij** — Zellij is a friendlier workspace for humans in terminals. Herdr is a runtime for agents in terminals: state, waits, direct attach, and an API.
- **vs cmux** — cmux is a Mac terminal app built around agents. Herdr isn't an app: it's the runtime underneath, in whatever terminal you already use, reachable over SSH.
- **vs Warp** — Warp wants to be your terminal and your platform. Herdr keeps your terminal and owns what runs inside it.
- **vs opencode web** — opencode's web mode serves one agent over HTTP. Herdr runs the whole herd: any agent CLI, many at once, from any tty.
- **vs Solo** — Solo is a dashboard that supervises your dev processes. Herdr holds interactive agent terminals open whether or not anything is watching them.
- **vs Conductor / Emdash / Superset** — Manager apps put worktrees, diffs, and review queues in a window. Herdr is the layer under that kind of window: quit their app and the agents stop; detach every Herdr client and they don't.

## Composition reminders
- "The columns are categories, not enemies." Herdr pairs happily with a worktree manager (Conductor/Emdash/Superset) and runs fine inside a fancy terminal (Warp/Ghostty/Kitty/iTerm/Alacritty).
- The nerd's job in a comparison question: **route the user to the right layer**, not evangelize. If they want worktree review UX, Herdr + a manager app. If they want persistent agent terminals, Herdr alone. If they just want a nicer terminal, Warp. If they want a process supervisor for a dev stack, Solo.
