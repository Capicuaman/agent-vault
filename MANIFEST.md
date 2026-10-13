# Vault Manifest

Auto-maintained index of all vault content. Last updated manually — run `./scripts/vault-manifest.sh` to regenerate (TODO: build that script).

## Skills (40 total)

### bilan/ (9 skills)
| Skill | Trigger | Source |
|-------|---------|--------|
| `bilan-base` | Core company knowledge, brand voice | textDump/.pi/skills |
| `bilan-marketing` | Campaigns, personas, content | textDump/.pi/skills |
| `bilan-sales` | Pricing, CRM, objection handling | textDump/.pi/skills |
| `bilan-label-system` | Packaging labels, Inkscape/SVG | textDump/.agents/skills |
| `bilan-blog-ops` | Blog creation and publishing | ~/.pi/agent/skills |
| `bilan-design` | Design system, Tailwind, tokens | ~/.pi/agent/skills |
| `bilan-mx-nerd` | Live bilan.mx site deep-nerd | ~/.pi/agent/skills |
| `bilan-seo-conversion` | SEO + CRO audits | ~/.pi/agent/skills |
| `bilan-webdev` | Astro site architecture and dev | ~/.pi/agent/skills |

### general/ (15 skills)
| Skill | Trigger | Source |
|-------|---------|--------|
| `assumption-space-sync` | Propagate new facts across docs | textDump/.agents/skills |
| `daily-journal` | Interactive daily journaling | textDump/.agents/skills |
| `elicitation` | Indirect questioning, high-stakes conversations | textDump/.pi/skills |
| `emil-design-eng` | UI polish philosophy (Emil Kowalski) | textDump/.agents/skills |
| `git-care` | Safe commit/push workflows | textDump/.pi/skills |
| `git-history-hygiene` | Clean git history, commit planning | textDump/.pi/skills |
| `impeccable` | Frontend UI design and redesign | textDump/.pi/skills |
| `learning-hq` | Learning HQ dashboard maintenance | textDump/.pi/skills |
| `metaphors-gamification` | Conceptual metaphors for gamification | textDump/.agents/skills |
| `one-page-executive-brief` | Compress docs into one-pagers | textDump/.agents/skills |
| `prompt-skill-agent-triage` | Decide: prompt vs. skill vs. agent | textDump/.agents/skills |
| `session-exec-report` | Executive reports on pi sessions | textDump/.pi/skills |
| `tab-triage` | OneTab URL dump processing | textDump/.agents/skills |
| `technology-teaching` | Best teaching artifact for any tech | textDump/.agents/skills |
| `tech-onboarding-orchestrator` | One-swoop tech onboarding | textDump/.agents/skills |

### nerds/ (5 skills)
| Skill | Trigger | Source |
|-------|---------|--------|
| `herdr-nerd` | Herdr terminal multiplexer expert | textDump/.pi/skills |
| `homeassistant-nerd` | Home Assistant architecture | ~/.pi/agent/skills |
| `laya-nerd` | Laya decision engine expert | textDump/.pi/skills |
| `nerd-forge-nerd` | Meta-expert on the *-nerd pattern | ~/.pi/agent/skills |
| `rea-nerd` | REA reverse-engineering expert | textDump/.pi/skills |

### forges/ (6 skills)
| Skill | Trigger | Source |
|-------|---------|--------|
| `forge-scout` | Detect forge-ripe opportunities | ~/.pi/agent/skills |
| `instruction-skill-forge` | Turn instructions into skills | textDump/.agents/skills |
| `nerd-forge` | Create new *-nerd persona skills | ~/.pi/agent/skills |
| `prompt-pattern-forge` | Extract reusable prompt patterns | ~/.pi/agent/skills |
| `workflow-drill-forge` | Gamified workflow drills | textDump/.agents/skills |
| `worktree-drill-forge` | Git/Herdr worktree drills | textDump/.pi/skills |

### platform/ (5 skills)
| Skill | Trigger | Source |
|-------|---------|--------|
| `graphify` | Knowledge graph building + querying | ~/.pi/agent/skills |
| `herdr` | Control Herdr panes/tabs/workspaces | ~/.pi/agent/skills |
| `here-now` | Publish sites, store files in cloud | ~/.agents/skills |
| `pi-agent-helper` | pi configuration and customization | ~/.pi/agent/skills |
| `prior-art` | Find existing solutions first | ~/.pi/agent/skills |

---

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
