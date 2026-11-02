---
name: genie-read
description: Mine software change artifacts — changelogs, release notes, pull requests, diffs, issue threads, postmortems, design docs, tests, and git history — to extract what is genuinely easy and hard about software engineering. Use when the user asks what to read to get better at software engineering, how to extract lessons from a changelog or release notes, wants to study a codebase's evolution or a specific bug fix, asks "what is actually hard in software", or wants a real fix dissected.
metadata:
  family: genies
  version: 2.0.0
---

# genie-read

**Go meta into other people's changes.** A changelog is an index of reality
contradicting someone's model. This skill turns that index into judgment.

A *genie* is a skill that goes meta into the artifacts software leaves behind.
See [`../genie-doctrine/SKILL.md`](../genie-doctrine/SKILL.md) for the family.

## When to use this skill

- "What should I read to get better at software engineering?"
- "What can I learn from this changelog / release notes / postmortem?"
- "Study this bug fix / this repo's evolution with me."
- "What is actually hard in software?"
- You want a real fix dissected end to end.

Use `genie-error` for **your own** errors, `genie-review` for a **pending** diff,
and `genie-write` when **producing** the artifacts.

## Read the doctrine first

Before answering, read:

1. [`../genie-doctrine/references/boundaries.md`](../genie-doctrine/references/boundaries.md) — the core thesis.
   **Hard bugs are collisions with a boundary you do not control.**
2. [`../genie-doctrine/references/easy-vs-hard.md`](../genie-doctrine/references/easy-vs-hard.md) — the taxonomy
   you are teaching toward.
3. [`../genie-doctrine/references/drill-worksheet.md`](../genie-doctrine/references/drill-worksheet.md) — the
   five-step drill you should walk the user through.

## The method

### 1. Start from the artifact, not from theory

Ask for or fetch the actual artifact before generalizing. Check the user's
environment for a local copy first (installed package, repo, changelog), then the
network. Read `references/artifacts.md` for how to obtain each of the nine lenses
and what each one uniquely teaches.

### 2. Classify every fix by boundary

For each entry in a *Fixed* section, name the boundary: environment,
lifecycle/state, concurrency, interface/contract, input space, human/time,
reproducibility. Do not classify by symptom; classify by cause shape.

### 3. Run the drill on one fix

Walk the five steps from `../genie-doctrine/references/drill-worksheet.md` explicitly. The
highest-value step is **4 (counterfactual)**: what upstream design decision would
have made this bug impossible?

### 4. Prefer the smallest diffs

A one-line fix for a subtle bug teaches more than a large feature. Look for fixes
that *stop owning state*, *stop trusting ambient config*, or *fail loudly at the
boundary*. Those are constraints finally being respected.

### 5. End with a transferable lesson

One sentence, no project nouns. If it still contains the product name, it is a
fact, not a lesson.

## The nine lenses

A changelog tells you *what* broke and *that* it is fixed. It hides the reasoning,
the rejected paths, and the cost. Pair it with:

| Artifact | What it uniquely reveals |
|---|---|
| **PR discussion / commit message** | *Why* this fix and not the obvious one; rejected approaches |
| **The raw diff** | Cost asymmetry: one-line fix for a subtle bug, huge fix for a tiny symptom |
| **Issue thread *before* the fix** | How bugs are actually discovered and reproduced |
| **Design docs / RFCs / ADRs** | The model of the system before reality contradicted it |
| **Tests** | A specification of known fragility; every "must not happen" test is a scar |
| **Postmortems** | Catastrophes are interactions, not single bugs; highest signal per word |
| **`git log` / `blame` on one file** | Churn = where reality pushes back; the stable core is equally telling |
| **CI config, dependency pins, packaging** | Reproducibility and supply-chain lessons |
| **Deprecations & breaking changes** | The long-term cost of getting an interface wrong |

Full expansion, with retrieval commands: [`references/artifacts.md`](references/artifacts.md).

## Cautions to state out loud

- **Survivorship bias.** Changelogs show bugs someone noticed, reproduced, and
  prioritized. Never-filed and silently-fixed bugs are invisible.
- **Sanitized for users.** The interesting sentence is usually the footnote.
- **Fix ≠ cause.** A fix is a choice under constraints. Ask what the constraints were.

## Bundled references

- [`references/artifacts.md`](references/artifacts.md) — the nine lenses, expanded, with commands
- [`references/casebook-pi-1.4.0.md`](references/casebook-pi-1.4.0.md) — worked example: 30+ real fixes classified by boundary
