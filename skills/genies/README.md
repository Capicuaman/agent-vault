# Genies

Software-engineering mastery skills that **go meta into the artifacts software
leaves behind** — bug fixes, changelogs, pull requests and diffs, issue threads,
postmortems, design docs, tests, and git history.

They teach from change, not from tutorials or the happy path.

## Skills (6)

| Skill | Direction | Trigger |
|---|---|---|
| [`genie-doctrine`](genie-doctrine/SKILL.md) | shared lens | boundary taxonomy, easy vs hard, the drill worksheet |
| [`genie-read`](genie-read/SKILL.md) | past, other people | mine changelogs / PRs / issues / postmortems / git history |
| [`genie-error`](genie-error/SKILL.md) | past, your own | capture, fingerprint, triage, write up errors |
| [`genie-write`](genie-write/SKILL.md) | future, for others | commit messages, PR bodies, bugfix notes, changelogs, postmortems |
| [`genie-review`](genie-review/SKILL.md) | present | boundary lens on a pending diff or design |
| [`genie-drill`](genie-drill/SKILL.md) | learning loop | drills, casebooks, Anki conversion, review rituals |

## The cycle

```
observe (read) → experience (error) → record (write) → apply (review) → train (drill)
                                    ↖______________ doctrine ______________↗
```

`genie-doctrine` is the shared reference the other five load by relative path
(`../genie-doctrine/references/...`). Install the whole category together so
those links resolve.

## The core idea

Hard bugs are collisions with a **boundary the author did not control**:
environment, lifecycle/state, concurrency, interface/contract, input space,
human/time, reproducibility.

The hard part of software is not writing code that does the thing. It is writing
code that keeps doing the thing in an environment you do not control, across
states you did not enumerate, for people whose needs change.

## Candidate entities (not yet built)

| Candidate | Layer | Ripeness | Why |
|---|---|---|---|
| `genie-forge` | L2 producer → L5 corpus | ✅ **ripe** | Six genies, rigid anatomy (`SKILL.md` + `references/`), explicit procedure, observable quality variance. Layer-legal. |
| `genie-nerd` | L6 auditor | ⏸ defer | Auditing one family's corpus is a `*-forge-nerd`-shaped job; the genie corpus is homogeneous enough that `genie-forge` covers it. |

Threshold (per `registries/_forge-pattern.md`): ≥2 instances, explicit procedure,
quality variance, and no existing forge covering the shape. `genie-forge` meets
all four; it is registered here so it is a known future entity, not a surprise.

## Install

```bash
cd ~/Documents/agent-vault
./scripts/vault-install.sh genies
```

## Related skills

- `general/git-care` — safe commit/push workflow used when contributing changes
- `general/technology-teaching` — turn docs and repos into teaching artifacts
