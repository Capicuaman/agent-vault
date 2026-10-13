# Example: Turning A Raw Instruction Into A Skill

## Raw User Instruction

> I would also like to go meta and create a skill that given the input, produce drills that can be gamified to understand workflows, start with herdr, notify the herdr-nerd if you need him.

## Intake

```yaml
raw_instruction: create a skill that turns input workflows into gamified drills, starting with Herdr
trigger_phrases:
  - produce drills
  - gamified workflow training
  - create CLI/browser labs
  - start with herdr
desired_behavior: extract workflow model, create drills, add gamification, consult herdr-nerd when needed
repeatability: repeated
scope: repo-wide workflow teaching
risk: low to medium depending on live-lab commands
examples_given:
  - Herdr/worktree quest
existing_skill_overlap:
  - metaphors-gamification
  - technology-teaching
  - prompt-skill-agent-triage
recommended_echelon: E1d drill/game skill
```

## Decision

Create a new skill, because no existing skill owned the full transformation from arbitrary workflow → drill ladder → CLI/browser/live-lab spec.

Do not make it an agent, because it does not need unattended runtime.

Do not keep it as a prompt, because it should be reused across workflows and sessions.

## Artifact Created

```text
.agents/skills/workflow-drill-forge/SKILL.md
.agents/skills/workflow-drill-forge/examples/herdr-worktree-drill-pack.md
```

## Why Not Patch `metaphors-gamification`?

`metaphors-gamification` chooses coherent metaphors and mechanics. The new instruction needed a broader workflow-teaching engine: safety maps, drills, traps, labs, and boss scenarios. That is adjacent, not identical.

## Why Mention `herdr-nerd`?

Herdr claims can drift quickly. If a Herdr drill depends on current behavior, the skill should check `.pi/skills/herdr-nerd/` or a Herdr specialist before finalizing.
