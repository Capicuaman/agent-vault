# 🏛️ Agent Vault

**Central repository for all agent skills, prompts, configs, and context files.**  
Shared across all Herdr instances via GitHub. Single source of truth.

## What's In Here

| Directory | Contents | Count |
|-----------|----------|-------|
| `skills/bilan/` | Brand-specific skills for bilan | 9 |
| `skills/general/` | Universal workflow & methodology skills | 15 |
| `skills/nerds/` | Expert persona (*-nerd) skills | 5 |
| `skills/forges/` | Production (*-forge) skills | 6 |
| `skills/platform/` | Tool/platform integration skills (pi, herdr, graphify) | 5 |
| `prompts/` | Reusable prompt templates | 15 |
| `registries/` | Pattern registries (_tech-nerd-pattern, _forge-pattern) | 3 |
| `configs/` | Reference configs (herdr, pi) | 1 |
| `system-prompts/` | Project-level SYSTEM.md files (agent context) | 1 |
| `scripts/` | Install & sync automation | 3 |

**Total: 40 skills**

---

## Quick Setup on a New Instance

```bash
# Clone the vault
git clone git@github.com:Capicuaman/agent-vault.git ~/Documents/agent-vault

# Install skills into pi config (interactive — pick categories)
cd ~/Documents/agent-vault && ./scripts/vault-install.sh

# Or install everything at once
./scripts/vault-install.sh all
```

---

## Sync Workflow

```bash
# Pull latest from GitHub (run on any instance to get updates)
./scripts/vault-sync.sh

# After editing a skill locally, push changes back
./scripts/vault-push.sh "update herdr-nerd with new session attach docs"
```

---

## Skill Categories

### `skills/bilan/` — Brand Skills
Project-specific to the bilan electrolyte brand. Load these when working on bilan marketing, web, sales, or product content.

| Skill | Purpose |
|-------|---------|
| `bilan-base` | Core company knowledge, brand voice, terminology |
| `bilan-marketing` | Campaigns, personas, content workflows |
| `bilan-sales` | Pricing, objection handling, CRM |
| `bilan-label-system` | Packaging label management end-to-end |
| `bilan-blog-ops` | Blog content creation and publishing |
| `bilan-design` | Design system, CSS architecture |
| `bilan-mx-nerd` | Deep-nerd for the live bilan.mx deployed site |
| `bilan-seo-conversion` | SEO + CRO audits |
| `bilan-webdev` | Astro site architecture and dev workflows |

### `skills/general/` — Universal Skills
Load anywhere, any project.

| Skill | Purpose |
|-------|---------|
| `assumption-space-sync` | Propagate new facts across docs when assumptions change |
| `daily-journal` | Interactive daily journaling for 05_JOURNAL |
| `elicitation` | Extract accurate info via indirect questioning |
| `emil-design-eng` | UI polish and component design philosophy |
| `git-care` | Safe review/stage/commit/push workflows |
| `git-history-hygiene` | Clean git history, commit boundaries |
| `impeccable` | Frontend UI design, review, and redesign |
| `learning-hq` | Scan and maintain the Learning HQ dashboard |
| `metaphors-gamification` | Apply conceptual metaphors to gamification design |
| `one-page-executive-brief` | Compress docs into decision-ready one-pagers |
| `prompt-skill-agent-triage` | Decide: prompt vs. skill vs. agent |
| `session-exec-report` | Write executive reports on pi sessions |
| `tab-triage` | Process OneTab URL dumps |
| `technology-teaching` | Turn docs/repos into the best teaching artifact |
| `tech-onboarding-orchestrator` | One-swoop onboarding for any new technology |

### `skills/nerds/` — Expert Persona Skills
Deep-nerd modes for specific tools and platforms.

| Skill | Purpose |
|-------|---------|
| `herdr-nerd` | Expert on Herdr terminal multiplexer |
| `homeassistant-nerd` | Home Assistant architecture and automation |
| `laya-nerd` | Laya decision engine deep-nerd |
| `nerd-forge-nerd` | Meta-expert on the *-nerd skill pattern itself |
| `rea-nerd` | REA (Reverse Engineer Anything) deep-nerd |

### `skills/forges/` — Production Skills
Generate, build, or transform artifacts at scale.

| Skill | Purpose |
|-------|---------|
| `forge-scout` | Detect forge-ripe opportunities in your work |
| `instruction-skill-forge` | Turn raw instructions into structured skills |
| `nerd-forge` | Create new *-nerd expert persona skills |
| `prompt-pattern-forge` | Extract reusable prompt patterns |
| `workflow-drill-forge` | Turn workflows into gamified drills |
| `worktree-drill-forge` | Git worktree + Herdr worktree drills |

### `skills/platform/` — Platform Skills
Tool and platform integrations for the agent stack.

| Skill | Purpose |
|-------|---------|
| `graphify` | Knowledge graph building and querying |
| `herdr` | Control Herdr panes, tabs, workspaces |
| `here-now` | Publish sites and store files in here.now |
| `pi-agent-helper` | pi, pi-agent, pi-coding-agent configuration |
| `prior-art` | Find existing popular solutions before building |

---

## Adding a New Skill

1. Create `skills/<category>/<skill-name>/SKILL.md`
2. Update `MANIFEST.md` (or run `./scripts/vault-manifest.sh` to auto-regenerate)
3. Run `./scripts/vault-push.sh "add <skill-name>"`
4. On other instances: `./scripts/vault-sync.sh` + `./scripts/vault-install.sh <skill-name>`

---

## Pi Config Locations (where skills get installed)

| Location | Scope | Used by |
|----------|-------|---------|
| `~/.pi/agent/skills/` | Global, all projects | pi (coding agent) |
| `~/.agents/skills/` | Global, all projects | agents/ conventions |
| `<project>/.pi/skills/` | Project-scoped | pi when cwd is that project |
| `<project>/.agents/skills/` | Project-scoped | agents/ conventions |

The install script targets `~/.pi/agent/skills/` by default (global scope, available everywhere).
