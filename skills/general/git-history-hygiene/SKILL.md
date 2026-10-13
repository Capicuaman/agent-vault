---
name: git-history-hygiene
description: Keep Git history readable by planning commit boundaries, spotting mixed changes early, using cleanup branches instead of rewriting shared main directly, and preserving rollback paths. Use when the user asks to keep history clean, split work into better commits, review recent commits, or safely adopt cleaned history.
---

# Git History Hygiene

Use this skill to keep the repo history understandable over time.

Primary goals:
- prevent mixed commits before they happen
- keep commits small and topic-scoped when practical
- clean messy history safely when needed
- protect rollback paths before any shared-history rewrite

## When to use

Use when the user asks for:
- `keep history clean`
- `split this into better commits`
- `what should be separate commits`
- `review these commits`
- `clean up commit history`
- `make this commit history easier to read`
- `adopt the cleaned history`
- any similar request about commit structure, rewrite safety, or rollback planning

Also use proactively when a Git task clearly spans unrelated areas such as:
- `01_PROJECTS/BILAN/`
- `01_PROJECTS/ALICIA/`
- `02_AREAS/HOME-LAB/`
- `03_RESOURCES/AI/`
- `05_JOURNAL/`

## Core rules

- Prefer prevention over rewrite.
- Prefer one main idea per commit.
- If work spans multiple unrelated topics, propose a commit plan before staging.
- Separate journal/archive sync from project/product work.
- Separate generated/runtime artifacts from human-authored content unless the generated output is the real deliverable.
- Do not rewrite shared history without explicit user approval.
- Do not rewrite `main` first. Build and review a cleanup branch first.
- Before replacing shared history, create a backup branch that preserves the old branch tip exactly.
- Use `--force-with-lease`, never blind force, and only after approval.
- If the remote moved unexpectedly, stop and ask.

## Commit boundary heuristics

Good commit boundaries usually follow one of these lines:
- one project or domain per commit
- one intent per commit
- one refactor or reorganization per commit
- one content batch with a clear shared purpose per commit

Typical splits in this repo:
- `03_RESOURCES/AI/pi/` changes separate from `01_PROJECTS/BILAN/`
- `02_AREAS/HOME-LAB/` separate from journals
- `05_JOURNAL/` and `04_ARCHIVES/` separate from active project work
- operational analytics/log sync separate from UI/content/documentation changes

Warning signs of a bad mixed commit:
- commit message needs `and` several times
- changes span unrelated top-level areas
- journals, resources, product work, and experiments are all mixed together
- the only honest message would be `general sync`

## Preventive workflow

1. If this is a Git/push/sync task, fetch the remote first.
2. Review `git status --short --branch`.
3. Group changed paths by topic, project, or intent.
4. If the grouping is ambiguous, show the proposed commit buckets before staging.
5. Stage one bucket at a time.
6. Verify staged files match the intended topic.
7. Commit with a short, specific message.
8. Push normally if the user asked to push.
9. Report what remains unstaged so mixed work does not silently slip into one commit.

## Cleanup workflow for already messy history

1. Review the recent commits and identify which are already good.
2. Decide whether the problem is only commit messages or truly mixed content.
3. If history is already pushed/shared, avoid rewriting `main` directly.
4. Create a separate cleanup branch from a safe base.
5. Rebuild the mixed commits into smaller topic-scoped commits.
6. Verify the final tree matches the original history's end state.
7. Push the cleanup branch for review.
8. Only replace shared `main` after explicit user approval and after creating a backup branch.

## Shared-history adoption workflow

Use this only after the user explicitly approves replacing shared history.

1. Verify the current remote branch tip.
2. Create and push a backup branch from the current remote tip.
3. Switch the remote branch to the cleaned history using `--force-with-lease`.
4. Verify the file tree matches the reviewed cleanup branch.
5. Give the user the exact rollback command.
6. Warn that other clones will need to resync because the timeline changed.

## Stop conditions

Stop and ask the user if:
- the remote branch is behind, diverged, or changed unexpectedly
- the worktree contains secret-like or generated files that may pollute commits
- the commit grouping is unclear
- the user has not approved a rewrite of shared history
- no backup branch exists for a planned shared-history replacement
- a force operation would be performed from a dirty or unclear state

## Commit message guidance

Prefer messages like:
- `pi: add workflow-forge workspace and workflow library`
- `bilan: sync operations and promotion updates`
- `journal and archives: sync daily notes`
- `ai resources: add pi study materials`

Avoid messages like:
- `general sync`
- `misc updates`
- `save notes and stuff`
- `big update`

## Relationship to git-care

- Use `git-care` for safe staging, secret avoidance, commit creation, and normal pushing.
- Use `git-history-hygiene` for deciding commit boundaries, reviewing messy history, planning cleanup branches, and safely adopting rewritten history.
- These two skills complement each other: `git-history-hygiene` decides the shape of history, `git-care` handles careful execution.

## Response style

Keep updates concise.

Always tell the user:
- what the proposed commit buckets are
- whether history cleanup is preventive or rewrite-based
- whether `main` will stay untouched
- what the rollback path is if shared history changes
