---
name: workflow-drill-forge
description: Turn any workflow, tool, repo note, or process into gamified drills that teach understanding through practice. Use when the user wants drills, labs, quests, boss scenarios, CLI/browser training loops, or game-like exercises for workflows. Starts with strong Herdr/worktree support and consults local herdr-nerd sources when available.
---

# Workflow Drill Forge

Use this skill to transform a workflow into **practice drills that can become a game**.

The goal is not decoration. The goal is to make the learner understand the workflow by repeatedly making the right decisions in realistic situations.

## Core Job

Given an input workflow, produce:

1. a clear workflow model
2. a drill ladder from easy to difficult
3. feedback for correct and incorrect choices
4. practical labs that can be played in CLI, browser, Markdown, or real-world mode
5. optional gamification mechanics: XP, ranks, streaks, boss fights, progress maps

## When To Use

Activate this skill when the user asks for:

- drills for a workflow
- gamified workflow training
- CLI labs
- browser labs with terminal elements
- quest design
- boss scenarios
- practice katas
- onboarding missions
- ways to understand a tool by doing
- converting docs into exercises
- Herdr, Git worktree, pi, vim, automation, or homelab workflow practice

## Specialist Hook: herdr-nerd

If the task is Herdr-specific and a `herdr-nerd` specialist/subagent is available in the current environment, consult it before finalizing drills.

In this repo, the concrete local specialist source is:

- `.pi/skills/herdr-nerd/SKILL.md`
- `.pi/skills/herdr-nerd/references/`

Read those files for Herdr claims before producing advanced Herdr drills, especially if the drill depends on Herdr 0.9+ behavior, remote machines, agent states, plugin behavior, socket/API usage, or worktree commands.

If no `herdr-nerd` specialist is available, continue without blocking and include this note in the final result:

```text
herdr-nerd specialist was not available in this session; drills were generated from repo context and known Herdr workflow notes.
```

Do not invent that the specialist was consulted if it was not.

## Required Discovery

Before writing drills, inspect source material when available.

Prioritize:

- workflow docs
- README files
- existing training apps
- command references
- task logs that show real work
- error reports or troubleshooting notes
- existing gamification notes

For Herdr, check these paths first when present:

- `03_RESOURCES/Software_Engineering/DEV/herdr/overview.md`
- `03_RESOURCES/Software_Engineering/DEV/herdr/worktrees.md`
- `03_RESOURCES/Software_Engineering/DEV/herdr/worktree-quest-cli/`
- `03_RESOURCES/Software_Engineering/DEV/herdr/worktree-quest-browser-labs/`
- `03_RESOURCES/AI/pi/herdr-mission-control-app/`
- `03_RESOURCES/AI/pi/metaphors-workflow-gamification.md`
- `.pi/skills/herdr-nerd/SKILL.md`
- `.pi/skills/herdr-nerd/references/`

## Drill Design Protocol

### Step 1: Extract The Workflow Model

Identify:

- actors: who or what acts
- artifacts: files, branches, sessions, panes, tickets, devices, etc.
- states: clean, dirty, blocked, done, merged, stale, active, idle
- transitions: actions that move between states
- commands: concrete CLI or UI operations
- decisions: points where the user must choose
- traps: common mistakes and misconceptions
- recovery moves: how to undo, pause, inspect, or safely proceed

Output this as a compact model before the drills.

### Step 2: Classify Commands By Safety

Every drill that includes commands must classify them:

| Class | Meaning | Examples |
|---|---|---|
| Read-only | Safe inspection | `git status`, `git worktree list`, `herdr session list` |
| Low-risk write | Creates local reversible state | `git add`, `git commit`, create a lab file |
| Mutating workflow action | Changes branch/session/project state | `git rebase`, `git merge`, `git worktree remove` |
| Destructive / dangerous | Can discard or overwrite work | `git reset --hard`, `git clean`, force push |

Never make destructive commands part of an automatic drill. If included for recognition, label them as traps.

### Step 3: Build A Drill Ladder

Use this progression unless the workflow demands something different:

1. **Recognition Drill** — identify the state or concept.
2. **Command Choice Drill** — choose the next correct command/action.
3. **Ordering Drill** — arrange steps in the right sequence.
4. **Trap Drill** — spot the dangerous or misleading option.
5. **Simulation Drill** — run through a fake terminal/browser scenario.
6. **Live Lab** — read-only or carefully confirmed practice on a real system.
7. **Boss Scenario** — combine multiple states, conflicts, and decisions.
8. **Reflection Check** — explain why the chosen path was safe.

### Step 4: Add Gamification Only After The Drills Work

Choose a metaphor that fits the workflow.

Good defaults:

- Herdr/worktrees: expedition, frontier, ranch, or field operations
- Git: time travel, checkpointing, shipping lanes, or expedition trail map
- Vim: martial arts / kata
- Homelab: control room / ship engineering
- Sales training: field reps / customer scenarios

For each gamified layer, define:

- XP or progress unit
- ranks or levels
- badges or achievements
- failure states
- feedback tone
- boss scenarios
- what behavior the mechanic reinforces
- what behavior it might accidentally hide

### Step 5: Produce A Build-Ready Output

Default output format:

```markdown
# [Workflow] Drill Pack

## Source Assumptions
- [what sources were used]

## Workflow Model
- Actors:
- Artifacts:
- States:
- Transitions:
- Traps:

## Safety Map
| Action | Safety class | Why |

## Drill Ladder
### Drill 1: [name]
Goal:
Scenario:
Prompt:
Choices or command:
Correct answer:
Feedback:
Trap explanation:
Gamification reward:

## Boss Scenario

## Live Lab Option

## Build Notes
- CLI version:
- Browser version:
- Markdown version:
```

## Output Modes

Pick the smallest useful mode:

- **Markdown drill pack**: best for fast design and review
- **CLI drill spec**: best when the workflow is command-heavy
- **Browser terminal lab blueprint**: best when visual state and simulated terminal both matter
- **Static HTML/JS lab**: best when user explicitly asks to build the game
- **Live lab checklist**: best for real infrastructure workflows

Do not build a full app unless the user asks for implementation or says to go ahead.

## Herdr Starter Pattern

For Herdr/worktree drills, include these core lessons:

1. Launch Herdr from the repo/folder where work lives.
2. A Herdr workspace is UI/session organization; a Git worktree is a separate checkout.
3. Use `ctrl+b then shift+g` to create a Herdr worktree lane.
4. Run one agent per task/branch/worktree.
5. Use Herdr agent states to decide what needs attention: blocked, done, working, idle.
6. Merge branches, not worktree directories.
7. Closing a Herdr workspace is not the same as deleting a Git worktree.
8. Cleanup is deliberate: inspect, merge or discard intentionally, remove worktree, then delete branch if safe.

### Herdr Drill Templates

#### Launch Drill

Scenario: You are SSH'd into a machine and want Herdr to manage `~/projects/my-app`.

Prompt: What do you do first?

Correct path:

```sh
cd ~/projects/my-app
herdr
```

Feedback: Launch location chooses the starting room. Session name chooses the persistent world.

#### Worktree Lane Drill

Scenario: You have three tasks: login bug, docs update, settings refactor.

Correct answer: Create three worktree lanes and run one agent per branch.

Trap: Running all agents in `main` creates branch chaos.

#### Merge Drill

Scenario: `docs/worktree-playbook` is done and reviewed.

Correct path:

```sh
git checkout main
git merge docs/worktree-playbook
```

Feedback: You merge the branch, not the Herdr workspace.

#### Cleanup Drill

Scenario: The branch is merged and the checkout is clean.

Correct path:

```sh
git worktree remove <path>
git branch -d docs/worktree-playbook
```

Trap: Closing the Herdr workspace does not delete the Git worktree or branch.

## Quality Checklist

Before finalizing a drill pack, verify:

- The workflow model is accurate.
- Drills test decisions, not rote memorization only.
- Every command is safety-classified.
- Traps match real user mistakes.
- Feedback explains why, not just right/wrong.
- Boss scenario combines multiple concepts.
- Gamification reinforces the desired behavior.
- The output can become a CLI or browser game without rewriting the learning logic.
