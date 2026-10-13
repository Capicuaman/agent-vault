---
name: prompt-skill-agent-triage
description: Decide whether a new workflow should stay a one-off prompt, graduate into a reusable pi skill, or become an autonomous agent. Use whenever you need to place a task into the prompt → skill → agent echelons.
---

# Prompt · Skill · Agent Triage

Use this skill to keep the PARA garden disciplined about **when to write a quick prompt, when to formalize a skill, and when to invest in an agent** (cron/runtime, watchdog, reporting).

The decision follows the existing escalation rules from `01_PROJECTS/BILAN/OPERATIONS/PROMPT_APPENDIX.md` (≥5 proven runs → skill, ≥10 autonomous runs → agent) plus pi's skill specification at `~/.npm-global/lib/node_modules/@mariozechner/pi-coding-agent/docs/skills.md`.

## When to activate this skill
- The user says "do we need a prompt, skill, or agent for this?"
- A workflow is being run repeatedly across sessions and needs governance.
- A request touches multiple files/systems and you are “thinking in echelons and in systems.”
- Before promoting anything into `.agents/skills/`, `.pi/skills/`, or cron.

## Required intake (fill before deciding)
Collect the following facts (paste into the session or `triage-intake` template if present):

1. **Use case name / link** — source doc, repo path, or ticket.
2. **Owner(s)** — who currently runs it, who approves outputs.
3. **Frequency** — times per week/month, or total runs so far.
4. **Inputs** — data sources, files, API keys, env requirements.
5. **Outputs** — files, folders, reports, broadcasts.
6. **Risk level** — regulatory, financial, reputational, or low.
7. **Automation pressure** — Why automate? speed, error rate, coverage?
8. **Rollback / logging needs** — Where would evidence live? (`tasks/todo.md`, dashboards, etc.)

> Tip: if answers to 2–8 are unknown, keep it a prompt until the workflow stabilizes.

## Echelons at a glance

| Echelon | Form | When it fits | Obligations |
|---|---|---|---|
| **E0** | One-off / appendix prompt | <5 successful runs, still exploratory, single operator, high context switching | Document in `PROMPT_APPENDIX` (T0–T1). No repo automation. Note learnings. |
| **E1** | pi skill (`.agents/skills/` or `.pi/skills/`) | Stable inputs/outputs, cross-file steps, multi-operator handoffs, needs repeatable instructions | Follow Agent Skills spec, include scripts/templates, update task log when created. |
| **E2** | Agent (cron, watcher, workflow automation) | ≥10 unattended runs, clear success signals, logging + alerting in place, failure modes understood | Needs runbook, health checks, journal automation post-push, explicit owner for runtime + fixes. |

## Decision tree

### Step 1 — Frequency & stability gate
- **< 3 runs** or still tuning prompt wording → Stay at **E0 (prompt)**. Record in appendix with status `T0` or `T1`.
- **≥ 5 human-run successes** with repeatable structure → Eligible for **E1 (skill)**. Continue to Step 2.
- **≥ 10 runs where humans already copy/paste the same checklist** → Consider E2, but only after Steps 2–3 confirm readiness.

### Step 2 — System surface & coordination
Ask:
- Does this touch multiple directories, data sources, or roles?
- Does it require helper scripts, templates, or metadata tracking?
- Would mis-execution create repo drift (out-of-sync docs, stale dashboards)?

If **yes** to any → prefer **skill** so the workflow lives near its scripts/templates.
If **no** (single file, single user) → stay prompt until scale changes.

### Step 3 — Autonomy readiness (agent filter)
Only graduate to an agent when **all** conditions hold:
1. **Inputs deterministic** — APIs, files, credentials stable and versioned.
2. **Outputs verifiable** — there is a deterministic diff or checksum to review.
3. **Alerting path** — someone is paged or notified when the agent fails.
4. **Rollback** — `git reset` plan or data backup exists.
5. **Journal/log integration** — runs append to `tasks/todo.md`, `05_JOURNAL`, or a dashboard automatically (per repo conventions).
6. **Runtime owner** — name the human who watches the cron/workflow.

Missing any item → remain at skill level even if the task is frequent.

### Step 4 — Risk & blast radius check
- **High stakes (legal, finance, compliance)** → require peer review even for skills; agents must include manual approval gates.
- **Medium stakes** → skill okay if reviewers follow the runbook; agents must write to a staging area first.
- **Low stakes / internal experiments** → prompts fine; only promote when repetition actually hurts productivity.

## Output format (copy into the session)
After running the checks, output a short report:

```
## Prompt/Skill/Agent Triage
- Use case: <name + path>
- Runs so far: <number> (evidence link)
- Frequency: <daily/weekly/ad-hoc>
- Risk: <low/med/high>
- Recommended echelon: <E0 prompt | E1 skill | E2 agent>
- Next action: <add to appendix / draft SKILL / schedule cron>
- Owner(s): <names>
- Logging target: <tasks/todo.md | dashboard path>
```

If promoting:
- **Prompt → Skill:** cite the future skill path (e.g., `.agents/skills/<name>/`), list required assets (scripts, templates), and link to pi skills doc for structure.
- **Instruction → Artifact:** use `instruction-skill-forge` when the user wants the raw instruction transformed into a prompt block, existing-skill patch, new skill, nerd skill, drill/game skill, or agent proposal.
- **Skill → Agent:** document desired runtime (cron tab, n8n workflow, systemd unit), monitoring hooks, and the post-run journal command (`/usr/bin/python3 ... journal_agent.py --force --live` after git pushes).

## Follow-up actions

| Outcome | Action | Where to log |
|---|---|---|
| Stay Prompt | Update or add entry in `PROMPT_APPENDIX` tracker with tier (T0/T1) | `01_PROJECTS/BILAN/OPERATIONS/PROMPT_APPENDIX.md` |
| Promote to Skill | Create directory under `.agents/skills/` or `.pi/skills/`, draft SKILL.md per pi spec, log plan + review in `tasks/todo.md` | Repo + task log |
| Promote to Agent | Draft runbook + automation script, set up cron/n8n, document monitoring + rollback, run journal automation after first push | Repo, automation dir, `tasks/todo.md`, `05_JOURNAL` |

## References
- `01_PROJECTS/BILAN/OPERATIONS/PROMPT_APPENDIX.md` — Tier rules, prompt tracker, escalation policy.
- `~/.npm-global/lib/node_modules/@mariozechner/pi-coding-agent/docs/skills.md` — Skill specification, naming, discovery.
- `tasks/todo.md` — Required place to log plan + review for every new skill/agent project.
- `.agents/skills/instruction-skill-forge/SKILL.md` — Companion skill for turning the triage decision into the actual prompt/skill/agent artifact.

## Example usage
> "We keep rewriting the same WhatsApp follow-up." → Intake reveals 8 runs/week, two reps, same calculator each time → Recommend **E1 Skill**. Path: `.agents/skills/bilan-follow-up`. Actions: draft SKILL.md, attach calculator script, log plan+review, add tracker entry.

> "Need hourly AR reminders without human touch." → Already T2 skill logging 15 unattended runs, data in Notion, n8n ready → Recommend **E2 Agent**. Actions: document cron job, set alerting, append to task log + journal after deployment.
