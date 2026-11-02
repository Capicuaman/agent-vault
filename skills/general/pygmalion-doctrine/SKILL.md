---
name: pygmalion-doctrine
description: >-
  System-level doctrine for evaluating, creating, administering, and updating
  agent entities — skills, nerds, forges, forge-nerds, scouts, genies, doctrines,
  registries, prompts, and drill packs. Use when deciding whether something
  should be a skill or a prompt or a nerd, when creating or reviewing a new
  entity, when auditing the vault for zombies, ghosts, orphans, hollow, stale or
  duplicate entities, when deprecating or superseding an entity, when catalogs
  and reality have drifted, or when asked to keep the entity corpus coherent.
metadata:
  version: 1.0.0
  family: governance
---

# Pygmalion Doctrine

Pygmalion sculpted a statue so carefully that it came alive. Your entities are
statues. **The description is the invocation that animates them** — and a statue
that is never addressed never wakes.

This skill governs the whole entity corpus of the agent-vault: what to make, how
to judge it, how to keep it true, and how to retire it. It sits *above* the
per-family pattern registries; it does not replace them.

## The three laws

**1. The behavior-delta law.**
> An entity earns its existence only by changing behavior at the moment of use.

The unit of value is not text written, files created, or tokens saved. It is:
*does the agent do something different — reliably — because this entity exists?*
If `behavior(with) == behavior(without)`, the entity is decoration.

**2. The routing-contract law (the Pygmalion effect).**
> Expectations embedded in the description shape the behavior it produces.

The description is the single most consequential line in the file: it decides
whether the entity ever fires. A vague description does not merely route poorly —
it licenses vague work, because the model infers its standards from what you wrote.

**3. The drift law.**
> Statues crumble silently.

Nothing fails loudly when a registry goes stale or a reference dangles. The corpus
just slowly stops matching reality, and the agent keeps confidently using the old
map. Administration is not filing; it is maintenance.

## The four phases

| Phase | Question | Reference |
|---|---|---|
| **Evaluate** | Is this worth existing, and is it good? | [`references/evaluate.md`](references/evaluate.md) |
| **Create** | How do I sculpt it so it comes alive? | [`references/create.md`](references/create.md) |
| **Administer** | Is the corpus still coherent? | [`references/administer.md`](references/administer.md) |
| **Update** | How does it change without breaking its users? | [`references/update.md`](references/update.md) |

Fit between entity families — nerd vs forge vs scout vs genie vs doctrine, and the
terminal climb level of each:
[`references/taxonomy.md`](references/taxonomy.md).

## The four gates (binary, must all pass)

| Gate | Test | Fail means |
|---|---|---|
| **G1 Routable** | Five real user utterances would match; none of the five should-not cases match | It never fires, or it steals routing |
| **G2 Different** | The shadow test: same task with and without it produces a materially different result | It is decoration |
| **G3 Bounded** | It states what it does *not* do and where it hands off | It becomes a catch-all |
| **G4 Registered** | One home, one registry line, no ≥85%-similar sibling | The corpus forks |

## The nine points (quality, 0–3 each)

| Dimension | 3 means |
|---|---|
| **Grounding** | Real paths, commands, versions, dated sources; explicit priority chain; no vibes |
| **Executability** | Numbered procedure an agent can follow without guessing; failure branches; verification step |
| **Maintainability** | Versioned metadata, dated grounding, a written update path, a named owner |

**Ship rule:** all four gates pass and total ≥ 7 / 9.

## Corpus health vocabulary

Use these seven words consistently; they are the shared language of the audit.

| State | Meaning | Typical fix |
|---|---|---|
| **Zombie** | Fails to load — bad YAML, missing description, name ≠ dir | Fix the frontmatter; re-run the loader |
| **Ghost** | Something references an entity that does not exist | Create it, or remove the reference |
| **Orphan** | Entity exists but no registry or catalog lists it | Register it, or retire it |
| **Hollow** | SKILL.md with no procedure, no references, no examples | Fill it or delete it |
| **Stale** | Dated grounding older than the threshold | Re-ground it, or date the staleness |
| **Duplicate** | Two entities with overlapping triggers | Merge, or sharpen the boundary |
| **Statue** | Never invoked; no evidence of use | Sharpen triggers, or retire it |

## Run the audit

The doctrine is executable, not aspirational. The audit is read-only:

```bash
cd ~/Documents/agent-vault
python3 scripts/vault-audit.py            # full report
python3 scripts/vault-audit.py --short    # one line per finding
python3 scripts/vault-audit.py --json     # machine-readable
```

Exit code 1 means zombies, duplicates, or ghosts are present. See
[`references/administer.md`](references/administer.md) for how to read the report
and what to do about each state.

## Hand-offs (do not duplicate these)

| Need | Use |
|---|---|
| Prompt vs skill vs agent echelon | `prompt-skill-agent-triage` |
| Turn an instruction into an artifact | `instruction-skill-forge` |
| Spec for a new `*-nerd` | `nerd-forge` + `registries/_tech-nerd-pattern.md` |
| Spec for a new `*-forge` | `registries/_forge-pattern.md` |
| Detect a forge opportunity | `forge-scout` |
| The climb-one-level prompt pattern | `registries/_meta-consultant-spawn.md` |
| The software-change lens | `genie-doctrine` and the genie family |

**Recursion stop:** every family has a terminal climb level. There is no
`forge-forge`, no `nerd-forge-nerd-nerd`, and no `doctrine-doctrine`. The registry
and the doctrine are where the ladder ends.
