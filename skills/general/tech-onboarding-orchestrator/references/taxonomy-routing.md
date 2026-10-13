# Taxonomy Routing for Technology Onboarding

Use this reference to place technology-onboarding outputs inside the existing textDump garden without inventing parallel folders.

## Default routing rule

Route by **intent first**, then by **domain**.

1. If the technology is being actively evaluated for a project, route to the project.
2. If it is general reusable knowledge, route to `03_RESOURCES/`.
3. If it is unsorted or the user is still deciding, route to `00_INBOX/`.
4. If it becomes a reusable pi behavior, route to the skill corpus.
5. If it becomes unattended runtime, route to an agent/runbook location and log ownership.

## PARA destination table

| Intake type | Preferred destination | Notes |
|---|---|---|
| General AI tool / agent framework | `03_RESOURCES/AI/<slug>/` | Use for LLM tools, agent frameworks, RAG, prompt systems, graph tools. |
| pi / agent-harness workflow | `03_RESOURCES/AI/pi/<slug>/` or `.agents/skills/` | Knowledge docs under resources; executable workflows as skills. |
| Developer library / framework | `03_RESOURCES/Software_Engineering/DEV/<slug>/` | Use when the tech is mostly a programming dependency or architecture pattern. |
| Python package / automation | `03_RESOURCES/Software_Engineering/DEV/<slug>/` or `03_RESOURCES/Workflow_Automation/<slug>/` | Prefer workflow automation if the user will run it operationally. |
| Shell / terminal / CLI / TUI | `03_RESOURCES/Terminal_And_Shell/<slug>/` or `03_RESOURCES/TUI/<slug>/` | Use TUI when interface patterns matter more than shell configuration. |
| Knowledge-management method | `03_RESOURCES/Knowledge_Management/<slug>/` or `03_RESOURCES/Methods/<slug>/` | Use Methods for conceptual frameworks; Knowledge_Management for systems/tools. |
| Active AI project | `01_PROJECTS/AI_Agents/WORKING/<slug>/` | Only create with user approval; active project, not just learning. |
| bilan-specific adoption | relevant `01_PROJECTS/BILAN/<domain>/` folder | Respect bilan taxonomy and brand/science rules. |
| Unsorted external link | `00_INBOX/YYYY-MM-DD_<slug>-intake.md` | Use when unsure; add TODO for routing decision. |
| Durable onboarding packet | destination folder above + `<slug>-onboarding.md` | Use the packet template. |
| Project-local reusable skill | `.agents/skills/<skill-name>/` | Best for textDump/PARA-specific workflows. |
| Project-local `*-nerd` | `.pi/skills/<thing>-nerd/` | Best when references cite local textDump paths. Update project `_tech-nerd-pattern.md`. |
| Global `*-nerd` | `~/.pi/agent/skills/<thing>-nerd/` | Only if self-contained and useful outside this repo. Update global `_tech-nerd-pattern.md`. |
| Global generic skill | `~/.pi/agent/skills/<skill-name>/` | Use for repo-independent pi behaviors. |

## Chameleon role routing

State the role switch when it matters.

| Technology smell | Likely role |
|---|---|
| PARA organization, documentation, skill ecosystem, taxonomy | Knowledge Garden Orchestrator |
| TypeScript, Astro, Bun, Vite, frontend apps | Full-Stack Web Engineer |
| Python scripts, automation, analysis, APIs | Python Automation Engineer |
| Jekyll/Astro content publishing, frontmatter, SEO content ops | Static Site & Content Engineer |
| Homelab, Tailscale, shell, services, networking | Infra/DevOps Engineer |
| Remotion, video generation, ComfyUI/media pipelines | Media/Video Engineer |
| Unknown external tech | State an inferred temporary role and revise after reading the docs. |

## Skill scope routing

Use this to avoid creating duplicate skills.

| Need | Use / hand off to |
|---|---|
| Teach or explain the tech | `technology-teaching` |
| Create a specialist persona for one tech | `nerd-forge` after nerd-worthiness gate |
| Audit whether a nerd should exist | `nerd-forge-nerd` |
| Detect a repeatable artifact shape | `forge-scout` |
| Find standard ecosystem solution first | `prior-art` |
| Decide prompt vs skill vs agent | `prompt-skill-agent-triage` |
| Convert an instruction into a skill artifact | `instruction-skill-forge` |
| Explore a codebase architecture | `graphify` / `graphify_build` after approval to clone or on an existing local path |
| Build drills/labs/quests for practice | `workflow-drill-forge` |

## Naming conventions

- Use lowercase slugs: `rea`, `astro`, `graphify`, `tailwind`.
- Keep brand casing rules when inside bilan content: prose says `bilan`; paths may contain `BILAN`.
- Use wiki-links for durable conceptual links: `[[tech-onboarding]]`, `[[nerd-forge]]`, `[[PARA]]`.
- If an output is dated, prefix with ISO date: `2026-10-10_rea-intake.md`.

## Approval gates

Ask before:

- cloning an external repo into textDump;
- installing packages or running untrusted code;
- creating a permanent `*-nerd`, `*-forge`, or autonomous agent;
- moving files across PARA categories;
- opening GUI apps on the SSH host.
