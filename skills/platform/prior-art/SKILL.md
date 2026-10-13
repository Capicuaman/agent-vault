---
name: prior-art
description: Always find the existing popular solution before writing custom code or proposing complex setups. Use whenever the user asks how to do something technical — automation, scripting, syncing, deploying, monitoring, parsing, converting, or any task where a battle-tested tool likely already exists. Biases hard toward "what do most people use?" over clever custom solutions. Invoked by "what do most people use", "is there a tool for this", "stand on the work of the dead", "prior art", or whenever a task smells like a solved problem.
---

# Prior Art

**Motto:** *Stand on the work of the dead. Someone already solved this. Find them.*

## Core Behavior

Before writing a single line of custom code or proposing a multi-step setup, always ask:

> "Has this been solved? What do 90% of people actually use?"

If yes — recommend that. If no — then and only then propose a custom solution.

## Search Order

1. **Known ecosystem tools** — recall popular packages, CLIs, daemons for the domain
2. **Web search** — if uncertain, search `"best tool for X site:reddit.com"` or `"X awesome list github"` to find what practitioners actually use
3. **Package registries** — npm, PyPI, Homebrew, apt — check download counts / stars as a popularity signal
4. **Only if nothing exists** — propose a minimal custom solution

## Response Format

When answering any technical question:

```
## What most people use
[Tool name] — [one sentence on what it is and why it's the standard]

## Install
[single command]

## Use
[minimal example — the 90% case only]

## Why not [alternative]?
[only if the user is likely to ask — one line]
```

Do NOT:
- Lead with custom scripts when a tool exists
- List 5 options when one is clearly dominant
- Explain edge cases before the happy path
- Add "gotchas" sections before the user has even tried the tool
- Propose systemd units, Docker containers, or CI pipelines when a cron job will do

## Popularity Signals to Trust

- GitHub stars > 1k on a focused tool = battle-tested
- In a distro's default repos (apt, brew core) = very widely used
- An "awesome-X" list exists for the domain = ecosystem is mature, pick the top entry
- Stack Overflow accepted answer uses it = 90% solution
- The tool has been around > 5 years = the API won't change on you

## Anti-Patterns to Reject

| Smell | What to do instead |
|---|---|
| "Let me write a Python script to..." | Check PyPI first |
| "You could set up a webhook server..." | Is there a managed service or CLI flag for this? |
| "Here's a systemd unit file..." | Does a cron job work? |
| "Option A, B, C, D, E all work..." | Pick one. The most popular one. |
| "It depends on your use case..." | What does the 90% use case need? Answer that. |

## Escalation Rule

Only escalate complexity when:
1. The user explicitly asks for more control
2. The simple tool provably cannot handle their scale or constraint
3. The popular solution is abandoned / unmaintained

State the escalation explicitly: *"The standard tool doesn't cover X, so here's the minimal custom addition."*

## Philosophy

Newton said "standing on the shoulders of giants." The giants are dead. Their code is not. Every cron job, rsync flag, and Homebrew formula represents accumulated human effort. Treat it as the default. Custom code is the cost of last resort.

The goal is always: **fewer moving parts, more proven parts.**
