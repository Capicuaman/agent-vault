# Herdr SSH Worktree Practice Pack

Example output for `.pi/skills/worktree-drill-forge`.

## Source Notes

- Designed for a user who is SSH'd into the machine.
- Herdr should be launched from the target repo when creating worktree lanes.
- Git owns branches and worktrees; Herdr organizes sessions, workspaces, panes, and agent states.

## Mental Model

- Git branch: named line of work.
- Git worktree: separate checkout directory for a branch.
- Herdr workspace: UI/session container around a repo or folder.
- Agent lane: one task, one branch, one worktree, one agent.

## Safety Map

| Action | Class | Why |
|---|---|---|
| `git status --short --branch` | Read-only | Shows branch and dirty state |
| `git worktree list` | Read-only | Shows all checkouts |
| `herdr` | Low-risk local | Starts or attaches to a session |
| `ctrl+b then shift+g` | Workflow mutation | Creates a Herdr/Git worktree lane |
| `git merge <branch>` | Workflow mutation | Changes current branch |
| `git worktree remove <path>` | Workflow mutation | Removes a checkout after Git safety checks |
| `git reset --hard` | Trap / destructive | Discards local changes |

## Drill Ladder

### Drill 1: Start At The Right Camp

Goal: Launch Herdr from the correct repo.

Scenario: You are SSH'd in and currently in `~`, but the project is `/home/capicuaman/Documents/textDump`.

Correct answer:

```sh
cd /home/capicuaman/Documents/textDump
herdr
```

Feedback: Launch location chooses the starting workspace.

Reward: +20 Trail Miles.

### Drill 2: Inspect Before Acting

Goal: Read Git state without changing anything.

Correct commands:

```sh
git status --short --branch
git worktree list
```

Trap: Starting cleanup before checking dirty files.

Reward: +15 Trail Miles.

### Drill 3: Split The Work

Goal: Pick the safe layout for three tasks.

Scenario: You have docs, bugfix, and refactor tasks.

Correct answer: create three worktree lanes, one branch per task, one agent per lane.

Trap: running three agents in `main`.

Reward: +30 Trail Miles.

### Drill 4: Read Agent Signals

Goal: Triage Herdr agent states.

State:

- docs: done
- bugfix: blocked
- refactor: working

Correct priority: unblock bugfix, review docs, let refactor continue.

Reward: +25 Signal Strength.

### Drill 5: Merge Branches, Not Folders

Goal: Merge a complete lane.

Correct command shape:

```sh
git checkout main
git merge docs/worktree-playbook
```

Feedback: Worktrees are directories. Branches are what Git merges.

Reward: +35 Review XP.

### Drill 6: Clean Up Deliberately

Goal: Remove only safe, merged checkouts.

Correct sequence:

```sh
git worktree list
git worktree remove <path>
git branch -d docs/worktree-playbook
```

Trap: believing closing the Herdr workspace deleted the Git worktree.

Reward: +30 Cleanup XP.

### Drill 7: Diverged Branch Map

Goal: Understand `ahead N, behind M`.

Correct inspection:

```sh
git fetch origin
git status --short --branch
git log --oneline --left-right --graph main...origin/main
```

Safe concept: commit intended work, rebase onto remote, push normally.

Trap: force-pushing because push failed.

Reward: +40 History XP.

## Boss Scenario: Branch Chaos

State:

- `main` is clean.
- `docs/worktree-playbook` is done and reviewed.
- `fix/login-timeout` is blocked.
- `refactor/settings` has conflicts.
- `experiment/cache-layer` is dirty and uncommitted.

Best answer:

1. Merge the clean reviewed docs branch.
2. Preserve the dirty experiment; do not remove it.
3. Unblock the login branch.
4. Handle refactor conflicts separately.
5. Clean up only merged clean worktrees.

Boss reward: Branch Tamer.

## Live Lab Option

Read-only commands only:

```sh
git status --short --branch
git branch --show-current
git worktree list
```

## Build Notes

- CLI adaptation: one scenario at a time, four choices, XP on first correct answer.
- Browser adaptation: simulated terminal plus visual map of main and child worktrees.
- Markdown adaptation: use as a static study guide or checklist.
