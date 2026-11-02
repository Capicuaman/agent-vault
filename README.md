# 🏛️ Agent Vault

**Central repository for all agent skills, prompts, configs, and context files.**  
Shared across all Herdr instances via GitHub. Single source of truth.

## What's In Here

| Directory | Contents | Count |
|-----------|----------|-------|
| `skills/bilan/` | Brand-specific skills for bilan | 9 |
| `skills/general/` | Universal workflow & methodology skills | 19 |
| `skills/genies/` | Software-engineering mastery skills (genies family) | 6 |
| `skills/knowledge/` | Knowledge packs generated from books/documents (book-to-skill) | 1 |
| `skills/nerds/` | Expert persona (*-nerd) skills | 5 |
| `skills/forges/` | Production (*-forge) skills | 6 |
| `skills/platform/` | Tool/platform integration skills (pi, herdr, graphify, orca, anki) | 6 |
| `prompts/` | Reusable prompt templates | 15 |
| `registries/` | Pattern registries (_tech-nerd-pattern, _forge-pattern) | 4 |
| `configs/` | Reference configs (herdr, pi) | 1 |
| `system-prompts/` | Project-level SYSTEM.md files (agent context) | 1 |
| `scripts/` | Install, sync, link & audit automation | 7 |

**Total: 52 skills**

---

## Entity Governance

The whole corpus is governed by `general/pygmalion-steward`: it receives requests
for new entities, decides whether one is needed and how many, routes production,
and audits the portfolio for duplicates, staleness and upstream drift.

- Organization chart: `skills/general/pygmalion-steward/references/org-chart.md`
- Formal terms: `skills/general/pygmalion-steward/references/glossary.md`
- Health audit: `python3 scripts/vault-audit.py`
- Drift sweep: `python3 scripts/vault-audit.py --drift --run-probes`

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

# Pull AND reinstall every changed skill
PI_SKILLS_DIR=~/.agents/skills ./scripts/vault-sync.sh --install

# After editing a skill locally, push changes back
./scripts/vault-push.sh "update herdr-nerd with new session attach docs"

# Check that installed copies match the vault (Talos)
python3 scripts/vault-audit.py --installed
```

### The three ways a skill can exist

| Situation | Move |
|---|---|
| You want to **author** something new | Create `skills/<category>/<name>/SKILL.md`, then `./scripts/vault-manifest.sh --write` |
| You **already have** a skill installed (authored here) | `./scripts/vault-import.sh <name> --category <cat>` — promotes it, refreshes the live copy, and prints the registry lines |
| It is **owned upstream** (Orca, distro, skills.sh) | Do **not** vendor it. Add a row to `registries/_externals.md` |

Full decision record and runbook: [`docs/local-skill-integration.md`](docs/local-skill-integration.md).

After any adoption, run the two guards:

```bash
./scripts/vault-manifest.sh --check        # catalogs match reality
python3 scripts/vault-audit.py --short     # no zombie/ghost/orphan/hollow
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
| `book-to-skill` | Convert books and documents into structured agent skills |
| `meta-prompt-coach` | Coach and improve prompts as reusable artifacts |
| `pygmalion-steward` | Entity intake, decomposition, org chart, audit and drift |
| `grill-me` | Interrogate: one question at a time, to test or extract |

### `skills/genies/` — Software-Engineering Mastery

Skills that **go meta into the artifacts software leaves behind** — bug fixes,
changelogs, pull requests and diffs, issue threads, postmortems, design docs,
tests, and git history. They teach from change, not from the happy path.

| Skill | Purpose |
|-------|---------|
| `genie-doctrine` | Shared lens: boundary taxonomy, easy vs hard, the five-step drill |
| `genie-read` | Mine other people's changes (changelogs, PRs, issues, postmortems, git) |
| `genie-error` | Capture, fingerprint, and write up your own errors |
| `genie-write` | Write commit messages, PR bodies, bugfix notes, changelogs, postmortems |
| `genie-review` | Apply the boundary lens to a pending diff or design |
| `genie-drill` | Turn lessons into skill: drills, casebooks, Anki cards |

The six install together — the five operational genies reference
`../genie-doctrine/references/`.

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

### `skills/knowledge/` — Knowledge Packs
Book- and document-derived reference corpora. Producer: `book-to-skill` (general/).
These answer questions from a grounded source; they do not run procedures.

| Skill | Purpose |
|-------|---------|
| `bonanno-game-theory` | Bonanno's game theory: strategic/dynamic games, Nash, beliefs, PBE |

### `skills/platform/` — Platform Skills
Tool and platform integrations for the agent stack.

| Skill | Purpose |
|-------|---------|
| `anki-admin` | Anki collection admin, FSRS, card quality, drills (script + SOP) |
| `graphify` | Knowledge graph building and querying |
| `herdr` | Control Herdr panes, tabs, workspaces |
| `here-now` | Publish sites and store files in here.now |
| `pi-agent-helper` | pi, pi-agent, pi-coding-agent configuration |
| `prior-art` | Find existing popular solutions before building |

### External skills (not vendored)

Some installed skills are owned and versioned upstream. Copying them here would
fork them and drift. They are listed in the Registry of Record for the `external`
Family, `registries/_externals.md` (currently Orca's version-matched stubs, the
skills.sh finder, and the two Omarchy package skills). Talos reports these as
`external`, not `unmanaged`.

---

## Adding a New Skill

**Authored here** — `skills/<category>/<name>/SKILL.md`, then:

```bash
./scripts/vault-manifest.sh --write
python3 scripts/vault-audit.py --short
./scripts/vault-push.sh "add <skill-name>"
```

**Already installed on this machine** — do not copy by hand:

```bash
./scripts/vault-import.sh <skill-name> --category <category>   # gates + copy + refresh live
./scripts/vault-manifest.sh --write                             # catalogs
python3 scripts/vault-audit.py --installed                      # now managed, not unmanaged
./scripts/vault-push.sh "import <skill-name> into <category>"
```

**Owned upstream** — add a row to `registries/_externals.md`, never to `skills/`.
`vault-import.sh` refuses externally-declared names and symlinked skills, so the
fork-by-accident path is closed.

Other instances pick any of the above up with `./scripts/vault-sync.sh --install`.

---

## Pi Config Locations (where skills get installed)

| Location | Scope | Used by |
|----------|-------|---------|
| `~/.pi/agent/skills/` | Global, all projects | pi (coding agent) |
| `~/.agents/skills/` | Global, all projects | agents/ conventions |
| `<project>/.pi/skills/` | Project-scoped | pi when cwd is that project |
| `<project>/.agents/skills/` | Project-scoped | agents/ conventions |

The install script targets `~/.pi/agent/skills/` by default (global scope, available everywhere).
