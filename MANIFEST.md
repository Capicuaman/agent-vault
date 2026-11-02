# Vault Manifest

Index of all vault content. The skills section between the markers is generated —
run `./scripts/vault-manifest.sh --write` after adding or removing a skill, and
`--check` before pushing. Everything outside the markers is hand-written.

<!-- BEGIN SKILLS -->
## Skills (52 total)

### bilan/ (9 skills)
| Skill | Trigger |
|-------|---------|
| `bilan-base` | Core company knowledge for bilan (health and wellness brand). |
| `bilan-blog-ops` | Blog content operations, creation workflows, and publishing standards for bilan. |
| `bilan-design` | Design system, CSS architecture, and visual consistency for bilan. |
| `bilan-label-system` | Manage bilan packaging labels end-to-end: front/back panel structure, typography decisions,… |
| `bilan-marketing` | Marketing-specific workflows, personas, campaign history, and content conventions for bilan. |
| `bilan-mx-nerd` | Deep-nerd mode for bilan.mx (https://bilan.mx) — the deployed public marketing site for the… |
| `bilan-sales` | Sales-specific workflows, pricing tiers, objection handling, CRM stages, and competitive battle… |
| `bilan-seo-conversion` | Periodic SEO + conversion rate audit for bilan.mx. |
| `bilan-webdev` | Core web development architecture and progressive enhancement guide for the bilan Astro site. |

### general/ (19 skills)
| Skill | Trigger |
|-------|---------|
| `assumption-space-sync` | Synchronize project files when new facts invalidate old assumptions. |
| `book-to-skill` | Convert books, papers, long documents, or prior reading notes into compact reusable agent skills. |
| `daily-journal` | Interactive daily journaling for the 05_JOURNAL folder. |
| `elicitation` | Extract accurate information from people who have incentive to shape their answers, using… |
| `emil-design-eng` | This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation… |
| `git-care` | Safely review, stage, commit, and push notes or project updates without losing work, staging… |
| `git-history-hygiene` | Keep Git history readable by planning commit boundaries, spotting mixed changes early, using… |
| `grill-me` | Interrogate the user one question at a time — to test whether they actually understand… |
| `impeccable` | Use when the user wants to design, redesign, shape, critique, audit, polish, clarify, distill,… |
| `learning-hq` | Scan the textDump repo for all learning materials and maintain the central Learning HQ HTML… |
| `meta-prompt-coach` | Coaches the user in meta-prompt engineering — recognizing when meta thinking applies,… |
| `metaphors-gamification` | Apply Lakoff & Johnson's "Metaphors We Live By" conceptual metaphor theory to analyze workflows… |
| `one-page-executive-brief` | Creates a decision-ready one-page executive brief from longer project docs, research memos,… |
| `prompt-skill-agent-triage` | Decide whether a new workflow should stay a one-off prompt, graduate into a reusable pi skill,… |
| `pygmalion-steward` | Steward of the agent entity corpus. |
| `session-exec-report` | Write a decision-ready executive report on the current pi session (or a specified slice of it)… |
| `tab-triage` | Triage a OneTab URL dump — clean tracking params, classify each link as Keep/Inbox/Discard,… |
| `tech-onboarding-orchestrator` | One-swoop onboarding for a new technology, GitHub repo, library, tool, framework, paper, or… |
| `technology-teaching` | Read technology files across the `textDump/` repo, extract the strongest explanation strategies… |

### genies/ (6 skills)
| Skill | Trigger |
|-------|---------|
| `genie-doctrine` | Shared doctrine for the genies family — the boundary taxonomy that explains why bugs are hard,… |
| `genie-drill` | Turn software-engineering lessons into durable skill through deliberate practice — the five-step… |
| `genie-error` | Capture, fingerprint, triage, and write up errors into the error-notes library at… |
| `genie-read` | Mine software change artifacts — changelogs, release notes, pull requests, diffs, issue threads,… |
| `genie-review` | Review a pending diff, pull request, or design for the bug classes that are hard to find —… |
| `genie-write` | Write change artifacts that teach — commit messages, pull request bodies, changelog entries,… |

### knowledge/ (1 skills)
| Skill | Trigger |
|-------|---------|
| `bonanno-game-theory` | Knowledge base from "Game Theory: An open access textbook with 165 solved exercises" by Giacomo… |

### nerds/ (5 skills)
| Skill | Trigger |
|-------|---------|
| `herdr-nerd` | Deep-nerd mode for Herdr (https://herdr.dev) — the terminal-native agent runtime (server +… |
| `homeassistant-nerd` | Home Assistant architecture, YAML/config review, automation debugging, integration planning,… |
| `laya-nerd` | Deep-nerd mode for laya (https://github.com/NandhaKishorM/laya) — a multilingual… |
| `nerd-forge-nerd` | Deep-nerd mode for the nerd-forge pattern itself and the entire *-nerd / *-forge corpus on this… |
| `rea-nerd` | Deep-nerd mode for REA / Reverse Engineer Anything (https://github.com/morluto/rea) — an… |

### forges/ (6 skills)
| Skill | Trigger |
|-------|---------|
| `forge-scout` | Detector skill that watches your work for forge-ripe opportunities and flags them before you… |
| `instruction-skill-forge` | Turn a raw user instruction, prompt, rule, example, or repeated behavior into the right meta… |
| `nerd-forge` | Create a new *-nerd skill: a grounded, enthusiastic expert persona for a specific technology,… |
| `prompt-pattern-forge` | Forge that extracts and documents a reusable prompt pattern from a prompt the user just made. |
| `workflow-drill-forge` | Turn any workflow, tool, repo note, or process into gamified drills that teach understanding… |
| `worktree-drill-forge` | Create practical, gamified drills for Git worktrees and Herdr worktree workflows. |

### platform/ (6 skills)
| Skill | Trigger |
|-------|---------|
| `anki-admin` | REQUIRED whenever the user asks about Anki on this machine: reviewing, studying, retention,… |
| `graphify` | Use for any question about a codebase, its architecture, file relationships, or project content… |
| `herdr` | Control Herdr, a terminal multiplexer for coding agents. |
| `here-now` | here.now lets agents publish websites and store private files in cloud Drives. |
| `pi-agent-helper` | Helps with recurring questions about pi, pi-agent, pi-coding-agent, and related customization… |
| `prior-art` | Always find the existing popular solution before writing custom code or proposing complex setups. |
<!-- END SKILLS -->

## Prompts (15 files)

| File | Purpose | Source |
|------|---------|--------|
| `here.md` | "I'm on this machine physically" context | textDump/.pi/prompts |
| `homelab-expert.md` | Homelab expert mode prompt | textDump/.pi/prompts |
| `remote.md` | "I'm SSH'd in remotely" context | textDump/.pi/prompts |
| `teach-tech.md` | Technology teaching trigger | textDump/.pi/prompts |
| `technology-teaching.md` | Tech teaching mode (v2) | textDump/.pi/prompts |
| `find-skill.md` | Skill discovery prompt | ~/.pi/agent/prompts |
| `home-assistant.md` | Home Assistant context | ~/.pi/agent/prompts |
| `pi-compare.md` | Compare pi to other agents | ~/.pi/agent/prompts |
| `pi-debug.md` | Debug pi configuration | ~/.pi/agent/prompts |
| `pi-docs.md` | pi docs lookup | ~/.pi/agent/prompts |
| `pi-explain.md` | pi feature explanation | ~/.pi/agent/prompts |
| `pi-scaffold-extension.md` | Scaffold pi extension | ~/.pi/agent/prompts |
| `pi-scaffold-skill.md` | Scaffold pi skill | ~/.pi/agent/prompts |
| `synology-curator.md` | Synology NAS curation | ~/.pi/agent/prompts |
| `synology.md` | Synology context | ~/.pi/agent/prompts |

---

## Registries (3 files)

| File | Purpose |
|------|---------|
| `_tech-nerd-pattern.md` | Canonical *-nerd skill pattern template |
| `_forge-pattern.md` | Canonical *-forge skill pattern template |
| `_meta-consultant-spawn.md` | Meta-consultant spawn pattern |

---

## Configs (1 file)

| File | Purpose |
|------|---------|
| `herdr-config-reference.toml` | Reference herdr config (from this machine) |

---

## System Prompts (1 file)

| File | Purpose |
|------|---------|
| `bilan-hero-poc.md` | Context for bilan hero section POC (was AI_Agents SYSTEM.md) |
