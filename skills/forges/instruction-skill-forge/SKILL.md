---
name: instruction-skill-forge
description: "Turn a raw user instruction, prompt, rule, example, or repeated behavior into the right meta artifact: one-off prompt, reusable skill, existing-skill patch, nerd skill, workflow drill, or autonomous agent proposal. Use when the user wants to go meta on instructions, promote or demote prompts/skills/agents, convert examples into skill instructions, or ask what echelon an instruction belongs in."
---

# Instruction Skill Forge

Use this skill when the user gives an instruction and wants to decide what it should become in the prompt → skill → agent ecosystem.

This is the **transformation companion** to `prompt-skill-agent-triage`.

- `prompt-skill-agent-triage` decides the echelon.
- `instruction-skill-forge` turns the instruction into the artifact for that echelon.

## Core Purpose

Given a raw instruction, produce one of these outputs:

| Echelon | Artifact | When it fits |
|---|---|---|
| E-1 | Session note / preference | Too personal, temporary, or vague for reuse |
| E0 | One-off prompt | Useful now, not yet proven repeatable |
| E1a | Patch existing skill | Belongs inside an existing workflow or skill |
| E1b | New repo-local skill | Reusable, repeatable, multi-step, cross-session behavior |
| E1c | `*-nerd` skill | Specialist persona for one tool/technology/domain |
| E1d | Drill/game skill | Teaches a workflow through labs, drills, boss scenarios |
| E2 | Agent proposal | Needs unattended execution, runtime, monitoring, logs |

The skill must support movement **up or down**:

- **Promote**: prompt → skill → agent.
- **Demote**: skill idea → prompt if not stable enough.
- **Merge**: new instruction → patch existing skill instead of creating duplicate skills.
- **Split**: bloated skill → smaller specialist skills.

## When To Use

Activate when the user says things like:

- "turn this instruction into a skill"
- "is this a prompt, skill, or agent?"
- "go meta on this instruction"
- "make this reusable"
- "convert this example into a skill"
- "should this be added to an existing skill?"
- "promote this prompt"
- "demote this skill idea"
- "make a nerd skill for this"
- "create a meta-skill"

## Related Skills To Consult

Use these when relevant:

- `prompt-skill-agent-triage` — for prompt/skill/agent echelon decision.
- `skill-maker` — for general skill creation patterns.
- `workflow-drill-forge` — if the instruction is about drills, labs, quests, practice, or gamified learning.
- `metaphors-gamification` — if the skill includes XP, ranks, missions, levels, or game design.
- `~/.pi/agent/skills/nerd-forge/SKILL.md` — if the result should be a `*-nerd` specialist.
- Existing local skills in `.agents/skills/` and `.pi/skills/` — to avoid duplicates.

## Required Discovery

Before creating a new skill, search for overlap.

Check:

- `.agents/skills/*/SKILL.md`
- `.pi/skills/*/SKILL.md`
- `.claude/skills/*/SKILL.md` or `.claude/skills/*/skill.md` when relevant
- related docs in `03_RESOURCES/`
- task logs if the instruction came from repeated work

If an existing skill already owns the behavior, patch that skill instead of creating a duplicate.

## Input Intake

Parse the instruction into this schema:

```yaml
raw_instruction: <exact or summarized input>
trigger_phrases:
  - <phrases that should activate it>
desired_behavior: <what the agent should do>
repeatability: <one-off | repeated | frequent | autonomous>
scope: <single file | repo-wide | project/domain | external runtime>
risk: <low | medium | high>
examples_given:
  - <examples or counterexamples>
existing_skill_overlap:
  - <candidate existing skills>
recommended_echelon: <E-1 | E0 | E1a | E1b | E1c | E1d | E2>
```

If critical facts are missing, ask at most one short clarifying question. If the likely answer is obvious from context, proceed and state the assumption.

## Decision Rules

### Demote To E-1 Session Note

Use when:

- instruction is personal style only
- applies only to the current conversation
- conflicts with higher-priority repo rules
- not stable enough to encode

Output: short note or suggestion, not a skill.

### Keep As E0 Prompt

Use when:

- first or second time running it
- user is still discovering the workflow
- input/output shape is unstable
- it does not need tools or repo context

Output: reusable prompt block with placeholders.

### Patch Existing Skill E1a

Use when:

- existing skill already covers 70%+ of the behavior
- new instruction is a rule, trigger, example, checklist, or edge case
- new skill would duplicate scope

Output: patch plan and edit target.

### Create New Skill E1b

Use when:

- repeated behavior has stable steps
- it uses repo context or tools
- it should survive across sessions
- it has clear activation triggers
- it is not just a specialist persona

Output: new `SKILL.md` with frontmatter, activation triggers, workflow, output format, examples, and safety notes.

### Create Nerd Skill E1c

Use when:

- instruction is about becoming an expert on one technology/tool/domain
- strong factual grounding matters
- the skill needs `references/` with facts, commands, patterns, or snapshots

Output: defer to `nerd-forge` pattern: `.pi/skills/<thing>-nerd/`.

### Create Drill/Game Skill E1d

Use when:

- instruction asks to teach or understand a workflow through practice
- examples, drills, quests, labs, boss fights, or terminal/browser games are central

Output: defer to or patch `workflow-drill-forge` unless a narrower domain-specific drill skill is needed.

### Propose Agent E2

Use when:

- task should run unattended
- runtime, logging, alerting, and recovery matter
- repeated executions already work manually

Output: agent proposal/runbook, not immediate automation unless explicitly approved.

## Artifact Templates

### E0 Prompt Template

```markdown
# Prompt: <name>

Use when: <trigger>

Input:
- <required input>

Task:
<instruction>

Output:
- <format>

Quality checks:
- <check>
```

### E1 Skill Template

```markdown
---
name: <skill-name>
description: <trigger-rich description>
---

# <Skill Title>

## Purpose

<what this skill does>

## When To Use

- <trigger phrase>
- <workflow condition>

## Required Discovery

- <files or searches>

## Workflow

1. <step>
2. <step>
3. <step>

## Output Format

<format>

## Examples

### Example Input

<input>

### Example Output

<output>

## Safety / Boundaries

- <what not to do>
```

### E1 Existing Skill Patch Template

```markdown
Patch target: `<path/to/SKILL.md>`

Why patch instead of new skill:
- <reason>

Add/modify sections:
- <section>

New trigger language:
- <trigger>

New example:
- <example>
```

### E2 Agent Proposal Template

```markdown
# Agent Proposal: <name>

## Why Skill Is No Longer Enough

## Runtime

## Inputs

## Outputs

## Schedule / Trigger

## Logging

## Failure Modes

## Human Approval Gates

## Rollback
```

## Output Format

When asked to transform an instruction, respond with:

```markdown
## Instruction Transformation

- Raw instruction: <summary>
- Recommended echelon: <E0/E1a/E1b/E1c/E1d/E2>
- Reason: <why>
- Existing skill overlap: <skills checked>
- Action: <create prompt | patch skill | create skill | propose agent>
- Target path: <path if applicable>

## Artifact

<prompt, patch, skill skeleton, or proposal>

## Next Step

<one concrete next action>
```

## Example: Last Prompt Pattern

### Raw Instruction

> I would like to create a skill that will help me turn the given instruction into a skill in the meta, up or down.

### Analysis

- This is not just a one-off prompt.
- It is a repeated meta-workflow: converting raw instructions into prompts, skills, skill patches, nerd skills, drill skills, or agent proposals.
- It overlaps with `prompt-skill-agent-triage`, but that skill mostly decides echelon; it does not produce the artifact.
- Therefore create a companion E1b skill.

### Output

Create `.agents/skills/instruction-skill-forge/SKILL.md` with:

- trigger-rich frontmatter
- input intake schema
- up/down echelon decision rules
- templates for E0/E1/E2 outputs
- examples showing how raw instructions become skills or patches

## Quality Checklist

Before finalizing:

- Did I search for existing overlapping skills?
- Did I choose patch over duplicate when appropriate?
- Did I support both promotion and demotion?
- Did I include activation triggers?
- Did I include output templates?
- Did I include at least one example from the user's actual instruction style?
- Did I avoid creating an autonomous agent without explicit approval?
