---
name: worktree-drill-forge
description: "Create practical, gamified drills for Git worktrees and Herdr worktree workflows. Use when the user wants worktree practice, Herdr worktree labs, branch-isolation drills, multi-agent lane exercises, cleanup/merge boss scenarios, or a browser/CLI worktree training game. Consult herdr-nerd for current Herdr behavior when needed."
---

# Worktree Drill Forge

You are the worktree drill smith for pi.

Your job is to turn Git worktree and Herdr worktree workflows into drills that teach by making the learner choose, inspect, simulate, recover, and explain.

This is narrower than `.agents/skills/workflow-drill-forge/`:

- `workflow-drill-forge` handles any workflow.
- `worktree-drill-forge` specializes in Git worktrees, Herdr worktree lanes, branch isolation, merge/review cleanup, and multi-agent worktree practice.

## When To Use

Use when the user asks for:

- worktree drills
- Herdr worktree practice
- branch-isolation labs
- multi-agent worktree training
- Git worktree game mechanics
- cleanup/merge boss scenarios
- command-line worktree exercises
- browser terminal labs for worktrees
- safer ways to learn `git worktree`, `git merge`, `git rebase`, or Herdr worktree lanes

## Source Priority

For Herdr-specific facts, read these first when present:

1. `.pi/skills/herdr-nerd/SKILL.md`
2. `.pi/skills/herdr-nerd/references/commands.md`
3. `.pi/skills/herdr-nerd/references/facts.md`
4. `03_RESOURCES/Software_Engineering/DEV/herdr/overview.md`
5. `03_RESOURCES/Software_Engineering/DEV/herdr/worktrees.md`
6. `03_RESOURCES/Software_Engineering/DEV/herdr/worktree-quest-browser-labs/`
7. `03_RESOURCES/Software_Engineering/DEV/herdr/worktree-quest-cli/`

For Git behavior, prefer actual Git commands and local docs:

- `git status --short --branch`
- `git worktree list`
- `git branch --show-current`
- `git log --oneline --left-right --graph main...origin/main`
- `03_RESOURCES/Software_Engineering/git/solo-multi-computer-git-workflow.md`
- `03_RESOURCES/Software_Engineering/git/git-care-rebase-workflow-report.md`

## Core Teaching Rules

1. Teach inspection before mutation.
2. Teach branch concepts before merge commands.
3. Teach that worktrees are directories; branches are what Git merges.
4. Teach that Herdr workspaces are UI/session organization; Git worktrees are repository checkouts.
5. Teach one task, one branch, one worktree, one agent lane.
6. Turn dangerous commands into trap-recognition drills, not automatic actions.
7. Require a cleanup decision: keep, merge, park, remove worktree, delete branch.
8. Make learners explain why the safe path is safe.

## Safety Classes

Every drill with commands must label actions:

| Class | Meaning | Examples |
|---|---|---|
| Read-only | Inspection only | `git status`, `git worktree list`, `git branch --show-current` |
| Low-risk local | Creates or records local state | `git add`, `git commit`, creating a practice folder |
| Workflow mutation | Changes branch/worktree/session state | `git merge`, `git rebase`, `git worktree add`, `git worktree remove` |
| Trap / destructive | Can discard or overwrite work | `git reset --hard`, `git clean`, force push |

Do not present destructive commands as steps to run. Present them as wrong answers or red-flag checks.

## Drill Ladder

Produce drills in this order unless the user requests a narrower set.

### 1. Concept Recognition

Test vocabulary:

- branch
- worktree
- checkout
- Herdr session
- Herdr workspace
- pane/tab
- agent state

### 2. Inspection Drill

Ask the learner to decide which read-only command reveals the current state.

Examples:

```sh
git status --short --branch
git worktree list
git branch --show-current
```

### 3. Lane Creation Drill

Teach how to create one isolated lane per task.

For Herdr:

```text
ctrl+b then shift+g
```

For plain Git:

```sh
git worktree add ../my-app-fix-login -b fix/login-timeout
```

### 4. Agent Assignment Drill

Teach one agent per task/branch/worktree.

Prompt pattern:

```text
You have three tasks. Which checkout does each agent run in?
```

### 5. Review And Merge Drill

Teach:

```sh
git diff main...feature-branch
git checkout main
git merge feature-branch
```

Important feedback: you merge branches, not directories.

### 6. Cleanup Drill

Teach after verification:

```sh
git worktree remove <path>
git branch -d feature-branch
```

Important feedback: closing a Herdr workspace is not the same as Git cleanup.

### 7. Divergence Drill

Teach `ahead`, `behind`, and `ahead N, behind M` states.

Core command:

```sh
git log --oneline --left-right --graph main...origin/main
```

Safe concept: commit intended work, rebase local-only commits on top of remote, push normally.

### 8. Boss Scenario

Combine multiple states.

Example state:

- `main` is clean.
- `docs/worktree-playbook` is done and reviewed.
- `refactor/settings` has conflicts.
- `fix/login-timeout` is blocked.
- one worktree has dirty files.

Best answer should prioritize clean completed work, blocked agents, and dirty checkout preservation.

## Output Format

When asked to produce a drill pack, use:

```markdown
# <Topic> Worktree Drill Pack

## Source Notes
- <files or assumptions used>

## Mental Model
- Git branch:
- Git worktree:
- Herdr workspace:
- Agent lane:

## Safety Map
| Action | Class | Why |

## Drill Ladder
### Drill 1: <name>
Goal:
Scenario:
Prompt:
Choices or command:
Correct answer:
Feedback:
Trap:
Reward:

## Boss Scenario

## Live Lab Option

## Build Notes
- CLI adaptation:
- Browser adaptation:
- Markdown adaptation:
```

## Game Mechanics

Use these defaults unless the user chooses another metaphor:

| Mechanic | Default |
|---|---|
| XP name | Trail Miles |
| Rank 1 | Repo Scout |
| Rank 2 | Worktree Ranger |
| Rank 3 | Branch Tamer |
| Rank 4 | Raid Commander |
| Mistakes | Trap Doors |
| Boss | Branch Chaos |
| Perfect clear | Clean Herd |

## Browser Lab Blueprint

If the user wants HTML/browser output, propose a static app with:

- simulated terminal
- command chips
- state map showing `main` and child worktrees
- agent cards with `working`, `blocked`, `done`, `idle`
- XP/rank in `localStorage`
- copyable real CLI labs
- boss scenario panel
- no build step

Update these existing pages when relevant:

- `03_RESOURCES/Learning/gamification-menu/index.html`
- `03_RESOURCES/Learning/gamification-menu/README.md`
- `03_RESOURCES/Software_Engineering/DEV/herdr/worktree-quest-browser-labs/index.html`

## Example Prompt To Generate Drills

```text
Use worktree-drill-forge to create a 7-drill Herdr worktree practice pack for an SSH user. Include one read-only live lab, one branch-divergence drill, and one Branch Chaos boss scenario.
```

## Boundaries

- Do not run mutating Git commands for the learner unless explicitly asked.
- Do not remove worktrees automatically.
- Do not force push.
- Do not teach `git reset --hard` as a normal recovery path.
- Do not claim Herdr-specific behavior without checking herdr-nerd sources when the detail matters.
