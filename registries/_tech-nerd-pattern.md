---
name: tech-nerd-pattern
description: "Hidden registry/meta-doc for the tech-nerd pattern and current nerd corpus. Not an invocable skill; kept loadable only to satisfy pi root Markdown validation."
disable-model-invocation: true
---

# tech-nerd skill pattern

Meta-doc. Not a skill itself — a template for spinning up more `*-nerd` skills.

## Scopes

Skills live in one of two **scopes**. Each scope has its own registry file; a nerd belongs in exactly one.

- **global scope** — `~/.pi/agent/skills/`. Loaded in every pi session regardless of directory. Registry: **this file**.
- **project scope** — `<repo>/.pi/skills/`. Loaded only when pi starts inside that repo. Registry: `<repo>/.pi/skills/registries/_tech-nerd-pattern.md`.

**Sibling registry (project):** `~/Documents/textDump/.pi/skills/registries/_tech-nerd-pattern.md`.

## Idea

A `*-nerd` skill makes the assistant a **grounded, enthusiastic, slightly obsessive expert** on exactly one technology. Trigger it when the user asks anything about that tech. The nerd:

1. Cites real commands, flags, file paths, keybinds, version numbers.
2. Grounds every answer in a priority chain: local repo docs → captured site snapshot → live site (via `graphify_add`) → `<tool> --help`.
3. Corrects common misconceptions kindly.
4. Suggests next-step composition patterns, not replacements.
5. Flags snapshot staleness; refreshes via `graphify_add` when the question is about "latest".

## Shape of a `*-nerd` skill

```
.pi/skills/<thing>-nerd/
  SKILL.md
  references/
    facts.md        # one-paragraph canon + a facts table
    commands.md     # cheatsheet of real commands, grounded in docs
```

### SKILL.md frontmatter

```markdown
---
name: <thing>-nerd
description: Deep-nerd mode for <Thing> (<url>). Use when the user asks about <thing>, <alt names>, <core concepts>, <CLI/API>, or compares <thing> to <alternatives>. Also trigger on "<thing>-nerd" and "nerd mode on".
---
```

The description must list the real activation triggers — concepts, commands, "compared to X" questions, and the explicit `nerd mode on` phrase.

### SKILL.md body sections (reuse this skeleton)

1. **Posture** — grounded, nerd voice, correct misconceptions kindly, prefer composition.
2. **What <thing> actually is** — one-paragraph canon the nerd will not deviate from.
3. **Key facts table** — install, license, version, hierarchy, defaults, where to look.
4. **Core verbs / keybinds / API** — real, copy-pasteable.
5. **When the user asks something, do this** — numbered procedure: classify → source priority → answer with real command → suggest next step → say so if not in docs.
6. **Signature nerd moves** — the 3–6 patterns a power user would use.
7. **Anti-patterns to call out** — things to politely correct.
8. **When to hand off** — which other skills to combine with.
9. **Housekeeping** — snapshot date, how to refresh.

## Checklist for building a new nerd

1. `graphify_add` the project's homepage/docs so a `raw/*.md` snapshot exists.
2. Check `03_RESOURCES/` for any local reference material; prefer it over snapshots.
3. Write `references/facts.md` with the one-paragraph canon + a facts table + version/date stamp.
4. Write `references/commands.md` as a copy-pasteable cheatsheet.
5. Write `SKILL.md` using the skeleton above. Keep description trigger-rich.
6. Smoke test: ask a question in the technology's domain and make sure the skill description would match it.

## Forging new nerds

Use the **`nerd-forge`** skill. It encodes the full build procedure, YAML gotchas, and smoke-test checklist. This file is the summary; `nerd-forge` is the executable version.

- Global install: `~/.pi/agent/skills/nerd-forge/SKILL.md`
- Project install: `.pi/skills/nerd-forge/SKILL.md`

## Sibling meta-docs

- `~/.pi/agent/skills/registries/_forge-pattern.md` — canonical spec + registry for **forges** (makers that produce artifacts to a shape).
- `~/.pi/agent/skills/registries/_meta-consultant-spawn.md` — the first prompt pattern (climb-one-level).

## Role taxonomy

| Role | Produces | Terminal? | Example |
|---|---|---|---|
| **nerd** | expert answers on one tech | no | `bilan-mx-nerd` |
| **forge** | artifacts to a spec | no | `nerd-forge` |
| **forge-nerd** | audits of a forge's corpus | yes (one per forge) | `nerd-forge-nerd` |
| **scout** | opportunity cards | yes (one per domain) | `forge-scout` |

## Current nerds

- `nerd-forge` — **global** (`~/.pi/agent/skills/nerd-forge/`). Meta-skill that creates new `*-nerd` skills.
- `herdr-nerd` — **project** (`~/Documents/textDump/.pi/skills/herdr-nerd/`). https://herdr.dev. Scoped to textDump because its references cite textDump-local docs.
- `homeassistant-nerd` — **global** (`~/.pi/agent/skills/homeassistant-nerd/`). Home Assistant / Frigate / MQTT / HACS / dashboards / homelab deployment.
- `laya-nerd` — **project** (textDump). https://github.com/NandhaKishorM/laya (typed AI decision engine).
- `bilan-mx-nerd` — **global** (`~/.pi/agent/skills/bilan-mx-nerd/`). https://bilan.mx. Deployed public marketing site for the bilan electrolyte brand (not the Astro codebase — that's `bilan-webdev`).
- `nerd-forge-nerd` — **global** (`~/.pi/agent/skills/nerd-forge-nerd/`). Meta-expert on the nerd-forge pattern and the full `*-nerd` / `*-forge` corpus. Audits, splits, merges, syncs the registries, proposes template amendments. Terminal climb — do not forge a `nerd-forge-nerd-nerd`.

## Scouts (global)

- `forge-scout` — **global** (`~/.pi/agent/skills/forge-scout/`). Detects forge-ripe opportunities in your work and produces forge-candidate cards. Does not build — flags.

## Prompt patterns

Produced by `prompt-pattern-forge` (`~/.pi/agent/skills/prompt-pattern-forge/`). Canonical shape in that forge's `examples/`.

- **Meta-Consultant Spawn** (`~/.pi/agent/skills/registries/_meta-consultant-spawn.md`) — the climb-one-level prompt shape that produced `nerd-forge-nerd` on 2026-10-07.

## Candidate nerds (open the next one when the need shows up)

- `astro-nerd` — Astro framework (already used in bilan)
- `bun-nerd` — Bun runtime / package manager
- `nix-nerd` — Nix / NixOS / flakes
- `pi-nerd` — the pi coding agent itself (would complement `pi-agent-helper`)
- `graphify-nerd` — the graphify CLI (would complement the existing `graphify` skill)
- `tailwind-nerd` — Tailwind CSS v4
- `jekyll-nerd` — for the bilan Jekyll site under `01_PROJECTS/BILAN/BLOG/jekyll/`
- `remotion-nerd` — Remotion video generation
- `tailscale-nerd` — Tailscale / home-lab networking
