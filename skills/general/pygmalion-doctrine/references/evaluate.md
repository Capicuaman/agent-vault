# Evaluate

Two different evaluations, do not confuse them:

- **Before creation:** *should this exist at all?* (ripeness)
- **After creation:** *does it work?* (gates + scores)

## Part 1 — Ripeness (before you build)

### The three questions

1. **Does it already exist?** Search the vault, not your memory.
   ```bash
   grep -ril "<topic>" skills/*/*/SKILL.md registries/*.md
   ```
   If a near-match exists, the answer is usually *patch it*, not *add a sibling*.

2. **Has the shape repeated?** A procedure run once is a prompt. The echelon gates
   in `prompt-skill-agent-triage` apply: ≥5 proven runs for a skill, and only
   stable inputs/outputs. For a forge, `forge-scout`'s five-signal checklist applies
   (repeatable shape, ≥2 instances or ≥2 named candidates, explicit procedure,
   observable quality variance, no existing forge).

3. **Is the boundary nameable in one sentence?** If you cannot say what the entity
   does *and what it refuses to do*, you are not ready to sculpt it. Vagueness at
   this stage becomes a catch-all skill later.

### The ripeness diagnostic

> *"If this entity existed, what would its first three concrete findings or
> outputs be?"*

If you cannot name three, the need is not yet shaped. Keep working by hand and
revisit.

## Part 2 — The four gates (after you build)

All four are binary. One failure blocks the entity regardless of score.

### G1 — Routable

The description is the routing contract. Test it, do not admire it.

**Trigger test.** Write down:

- **Five must-fire utterances** — the exact phrases a real user would type,
  including synonyms and error symptoms, not your internal vocabulary.
- **Five must-not-fire utterances** — adjacent tasks that belong to a sibling
  entity.

Then answer honestly: would a model reading only the description route each one
correctly? If a must-fire phrase is absent, add it. If a must-not-fire phrase
would match, add an explicit non-goal.

**Red flags**

- Description describes the *topic* instead of the *situation*.
- Description contains only abstractions ("helps with engineering").
- Description claims a broad domain that a sibling already owns.
- Explicit activation phrase (`<name>-nerd`, "nerd mode on") missing when the
  family convention expects one.

### G2 — Different (the shadow test)

Run the same realistic task twice:

1. **With** the entity loaded.
2. **Without** it (disable it, or reason from the bare prompt).

Compare four things:

| Dimension | Ask |
|---|---|
| Coverage | Did it consider something it otherwise missed? |
| Grounding | Did it cite real paths/commands instead of plausible ones? |
| Procedure | Did the steps become followable instead of improvised? |
| Refusal | Did it correctly decline the out-of-scope part? |

If none of the four changed, the entity is decoration. Either sharpen it until a
delta appears, or retire it.

**Cheap approximation:** if you cannot state the delta in one sentence before
testing, you already know the answer.

### G3 — Bounded

Every entity needs an explicit edge:

- a **Non-goals** or **What this is NOT** section, and
- a **hand-off** naming the entity that owns the excluded work.

An entity with no edge becomes a catch-all, and catch-alls destroy routing for
everything around them. This is the most common failure in a growing corpus.

### G4 — Registered

- Exactly one scope (vault source + its install target).
- Exactly one registry line (family registry, or `README.md`/`MANIFEST.md`).
- No sibling whose description similarity is ≥ 85%.
- No name collision across categories.

## Part 3 — The nine points

Score 0–3 on each. Total 9. Ship at ≥ 7 with all gates passed.

### Grounding (0–3)

| Score | Evidence |
|---|---|
| 0 | Generic advice; no paths, commands, versions, or sources |
| 1 | Some real specifics, but unverifiable or undated |
| 2 | Real commands and paths; most claims traceable |
| 3 | Explicit priority chain (local docs → snapshot → live → `--help`), dated snapshot, staleness disclaimer, no invented numbers |

### Executability (0–3)

| Score | Evidence |
|---|---|
| 0 | Prose only; no procedure |
| 1 | A procedure, but steps are vague or unordered |
| 2 | Numbered procedure an agent can follow |
| 3 | Numbered procedure + failure branches + a verification step + a stopping condition |

### Maintainability (0–3)

| Score | Evidence |
|---|---|
| 0 | No versioning, no dates, no update path |
| 1 | Dated but no update procedure |
| 2 | `metadata.version` + dated grounding |
| 3 | Version + dates + written update path + named owner or cadence |

## Part 4 — Evaluating an existing corpus

Use the audit instead of re-reading everything by hand:

```bash
python3 scripts/vault-audit.py
```

Interpretation:

| Signal | Meaning | Priority |
|---|---|---|
| A **zombie** exists | An entity the model cannot load at all | Fix first — it is silently absent |
| **Ghosts** | The map points at nothing | High — causes confident wrong hand-offs |
| **Duplicates** | Routing conflict | High — both entities degrade |
| **Hollow** | Claims without substance | Medium |
| **Stale** | Grounding has aged out | Medium |
| **Orphans** | Invisible to the catalog | Low/Medium |
| **Statues** | Never invoked | Investigate triggers before deleting |

Order matters: a zombie is worse than a stale entry, because a stale entry at
least still loads. Fix load failures before content quality.

## The anti-pattern to name out loud

> **Scoring an entity by how it reads rather than by what it changes.**

Well-written, well-structured, well-cited prose that produces no behavior delta
is the most expensive kind of failure in a corpus, because it *looks* like
progress and survives review.
