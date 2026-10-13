# Herdr Worktree Drill Pack

Example output for `workflow-drill-forge`.

## Source Assumptions

- Herdr organizes sessions, workspaces, tabs, panes, and agent states.
- Git owns branches and worktrees.
- Herdr can create Git worktree lanes with `ctrl+b then shift+g`.
- One task per branch/worktree/agent is the cleanest multi-agent pattern.

## Workflow Model

- Actors: user, Herdr, Git, coding agent.
- Artifacts: session, parent workspace, child worktree workspace, branch, checkout, pane, agent state.
- States: clean main, dirty branch, blocked agent, done agent, merged branch, stale worktree.
- Transitions: launch Herdr, create worktree, start agent, inspect state, review diff, merge branch, remove worktree.
- Traps: running multiple agents in main, deleting dirty worktrees, thinking workspace close equals Git cleanup, merging directories instead of branches.

## Safety Map

| Action | Safety class | Why |
|---|---|---|
| `git status --short --branch` | Read-only | Shows current branch and file state |
| `git worktree list` | Read-only | Lists worktree paths and branches |
| `herdr` | Low-risk write | Attaches/starts a session but should not mutate repo files |
| `ctrl+b then shift+g` | Mutating workflow action | Creates a branch/worktree lane |
| `git merge <branch>` | Mutating workflow action | Changes current branch history/files |
| `git worktree remove <path>` | Mutating workflow action | Removes a checkout after Git safety checks |
| `git reset --hard` | Destructive / dangerous | Discards local changes |

## Drill Ladder

### Drill 1: Base Camp

Goal: Launch Herdr with the right parent context.

Scenario: You are in `~/Downloads`, but the project is `~/projects/my-app`.

Prompt: What should you do before starting Herdr?

Correct answer:

```sh
cd ~/projects/my-app
herdr
```

Feedback: Herdr's launch location creates the natural parent workspace.

Gamification reward: +20 Trail Miles.

### Drill 2: Split The Herd

Goal: Choose the safe multi-agent pattern.

Scenario: You have a bugfix, a docs update, and a refactor.

Correct answer: Create one worktree/branch per task and run one agent in each lane.

Trap: Three agents in `main` creates mixed diffs and review chaos.

Gamification reward: +30 Trail Miles.

### Drill 3: Read The Sidebar

Goal: Triage Herdr agent states.

Scenario: One agent is blocked, one is working, one is done.

Correct answer: Unblock the blocked agent first, then review the done agent, then let the working agent continue.

Feedback: Blocked means the system needs you. Done means the branch needs review. Working means wait.

Gamification reward: +25 Signal Strength.

### Drill 4: Merge The Loot

Goal: Understand branch vs. worktree.

Scenario: `docs/worktree-playbook` is complete.

Correct answer:

```sh
git checkout main
git merge docs/worktree-playbook
```

Feedback: Worktrees are directories. Branches are what Git merges.

Gamification reward: +35 Review XP.

### Boss Scenario: Branch Chaos

State:

- `main` is clean.
- `docs/worktree-playbook` is done and reviewed.
- `refactor/settings` has conflicts.
- `fix/login-timeout` is blocked waiting for credentials.

Prompt: What should you do next?

Best answer: Merge the clean docs branch first, then handle the blocked and conflicted lanes deliberately.

Trap answer: Delete all worktrees because the sidebar is noisy.

Boss reward: Rank up from Worktree Ranger to Branch Tamer.

## Build Notes

- CLI version: represent each drill as scenario, choices, answer, feedback, XP.
- Browser version: show a simulated terminal plus a worktree/state map.
- Live lab version: only use read-only commands until the learner explicitly opts into mutating actions.
