---
name: git-care
description: Safely review, stage, commit, and push notes or project updates without losing work, staging secrets, or committing generated files. Use when the user says git care, save my notes, backup my notes, sync my notes, or asks for a careful commit/push workflow.
---

# Git Care

Use this skill to preserve the user's work with a careful Git workflow.

Primary goal:
- do not lose notes
- do not commit secrets
- do not pollute the repo with generated or runtime files

## When to use

Use when the user asks for:
- `git care`
- `save my notes`
- `backup my notes`
- `sync my notes`
- `commit and push my markdown`
- any similar request about safely saving work to Git

If the user is asking to keep history clean, split work into better commits, review messy recent commits, or safely adopt rewritten history, also load the companion skill:
- `.pi/skills/git-history-hygiene/SKILL.md`

## Safety rules

- Never run destructive Git commands such as `git reset --hard`, `git checkout --`, `git clean`, force push, or amend.
- Run `git fetch origin` before deciding whether it is safe to push, but only when the user is explicitly asking for git/push/sync work.
- If the branch is behind, diverged, or has no upstream, stop and ask the user how to proceed.
- Never commit real secrets: `.env`, credentials, private keys, token files, OAuth files, or anything secret-looking.
- Do not stage generated dependency/build/runtime paths unless the user explicitly asks.
- Leave unrelated untracked generated files alone. Do not delete them.
- If a commit succeeds, push only with normal `git push`.
- Respect repo-local instruction files such as `AGENTS.md` and `CLAUDE.md`.
- Do not commit or push unless the user explicitly asks.

## Generated or local paths to exclude by default

- `node_modules/`
- `venv/`, `.venv/`, `env/`
- `dist/`, `build/`, `.next/`, `.astro/`, `.turbo/`
- `__pycache__/`, `*.pyc`, `*.pyo`
- `*.db`, `*.sqlite`, `*.sqlite3`
- `.DS_Store`, `Thumbs.db`
- `.env`, `.env.*` except `.env.example`
- credential/key/token files such as `credentials.json`, `client_secret*.json`, `token.json`, `*.pem`, `*.key`, `id_rsa*`
- repo runtime logs and machine state files when they are not intentional deliverables

## Preferred files to save

Stage useful, human-authored files by default:
- `.md`, `.markdown`, `.txt`, `.qmd`
- `.json`, `.jsonl`, `.csv`, `.tsv`, `.yaml`, `.yml`
- `.html`, `.css`, `.svg`
- `.py`, `.ts`, `.tsx`, `.js`, `.jsx`, `.mjs`, `.cjs`, `.sh`
- `package.json`, `package-lock.json`, `tsconfig*.json`, `.gitignore`, `.env.example`

## Workflow

1. Run `git fetch origin`.
2. Run `git status --short --branch`.
3. If the branch is behind, diverged, or missing upstream, stop and ask the user.
4. Review changed paths and identify unsafe/generated files.
5. Decide what should be included before staging.
6. Stage useful human-authored content.
7. Unstage excluded/generated/secret-like paths.
8. Verify staged paths with a generated/secret check.
9. Show `git diff --cached --stat`.
10. If nothing is staged, say so clearly.
11. Commit with a short lowercase descriptive message if the user asked for commit.
12. Push with normal `git push origin <branch>` if the user explicitly asked for push.
13. Run `git status --short --branch` after push and report remaining local files separately.

## Useful commands

```bash
git fetch origin
git status --short --branch
git add -A
git restore --staged -- ':(glob)**/node_modules/**' ':(glob)**/venv/**' ':(glob)**/.venv/**' ':(glob)**/dist/**' ':(glob)**/build/**' ':(glob)**/__pycache__/**' ':(glob)**/*.pyc' ':(glob)**/*.db' ':(glob)**/*.sqlite' ':(glob)**/*.sqlite3'
git diff --cached --name-only | rg '(^|/)\.env($|\.)|credentials|client_secret|token\.json|\.pem$|\.key$|id_rsa|node_modules|(^|/)venv/|(^|/)\.venv/|(^|/)dist/|(^|/)build/|__pycache__|\.pyc$|\.db$|\.sqlite3?$'
git diff --cached --stat
git commit -m "save notes and project updates"
git push origin main
git status --short --branch
```

If the secret/generated-file check prints staged paths, unstage them before committing unless the user explicitly approves and it is safe.

## Commit message guidance

Prefer simple, descriptive messages:
- `save notes and project updates`
- `save daily notes`
- `save bilan notes and dashboards`
- `save cooking notes`

## Response style

Keep updates concise:
- say whether the branch is safe to push
- say what would be excluded
- say the commit hash if a commit happened
- say whether push succeeded
- mention remaining generated files only if relevant
- if commit boundaries are unclear or history structure matters, say that `git-history-hygiene` should be used alongside this skill
