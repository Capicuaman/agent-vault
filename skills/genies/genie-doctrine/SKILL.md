---
name: genie-doctrine
description: Shared doctrine for the genies family — the boundary taxonomy that explains why bugs are hard, what is genuinely easy versus hard in software engineering, and the five-step drill for turning a bug fix into a transferable lesson. Use when asked what is actually hard in software, when classifying a bug or failure by boundary, when designing a guardrail or checklist, or as the shared reference loaded by genie-read, genie-error, genie-write, genie-review, and genie-drill.
metadata:
  family: genies
  version: 2.0.0
---

# genie-doctrine

The shared root of the **genies** family.

> **Genies are skills that go meta into the artifacts software leaves behind** —
> bug fixes, changelogs, pull requests and diffs, issue threads, postmortems,
> design docs, tests, and git history.

They do not teach from tutorials or the happy path. They mine the *residue of
change* for transferable judgment.

## The family

They form a cycle: observe → experience → record → apply → train.

| Genie | Direction | What it does |
|---|---|---|
| `genie-read` | past, other people | Mine changelogs, PRs, diffs, issues, postmortems, design docs, tests, git history. |
| `genie-error` | past, your own | Capture, fingerprint, triage, and write up errors into the error-notes library. |
| `genie-write` | future, for others | Write commit messages, PR bodies, bugfix notes, changelog entries, postmortems that teach. |
| `genie-review` | present | Apply the boundary lens to a pending diff or design to predict bugs before they ship. |
| `genie-drill` | learning loop | Convert lessons into skill: the drill, casebooks, Anki cards, review rituals. |
| `genie-doctrine` | shared | This skill: the lens all the others rest on. |

## The one thesis

> **Nearly every hard bug is a collision with a boundary the author did not
> control.** The easy work lives entirely inside boundaries you fully own. The
> hard work is lifecycle, concurrency, environment, and interfaces with things
> you cannot see.

So for any fix, artifact, or diff, ask the one question that unlocks it:

> **Which boundary did this cross?**

Bug trackers classify by *symptom*, which does not transfer. Boundaries classify
by *cause shape*, which does. Once you can name the boundary, you can predict the
bug class in code you have never seen — and design it out before it exists.

## The seven classes (summary)

| Class | You do not control | Symptom |
|---|---|---|
| **Environment** | the machine — OS, shell, encoding, `PATH`, ambient config | "works on Linux, breaks on Windows" |
| **Lifecycle / state** | time beyond the call — what outlives what set it | "works until you close it wrong" |
| **Concurrency** | interleaving, admission, cancellation | "works alone, fails under load" |
| **Interface / contract** | the other side — APIs, providers, caches | "works on one provider"; "stale after a change" |
| **Input space** | what inputs exist | "one weird input breaks it" |
| **Human / time** | the future — compatibility, deprecation | "the upgrade broke everyone's config" |
| **Reproducibility** | the build graph — deps, packaging, determinism | "works in dev, fails on fresh install" |

Full detection questions, real examples, and design implications:
[`references/boundaries.md`](references/boundaries.md).

## What is easy vs hard

**Easy, and chronically underestimated:** the happy path, the isolated feature,
"works on my machine", adding to a catalog, rendering and plumbing.

**Hard, and almost never the algorithm:** lifecycle, concurrency and admission,
cross-platform reality, caching and consistency, failure semantics, backward
compatibility, reproducibility, input space.

> **The tell:** if you can describe a change without the words *state*, *other*,
> *concurrent*, *version*, *environment*, or *exit path*, it is probably easy.

Full taxonomy with symptoms and practice suggestions:
[`references/easy-vs-hard.md`](references/easy-vs-hard.md).

## The five-step drill

For one artifact, about twenty minutes:

1. **Reconstruct** the failure from the issue, not the summary.
2. **Name the boundary** — one of the seven.
3. **Read the diff** — why is the fix *this* size? What did it preserve?
4. **Counterfactual** — what upstream decision would have made this impossible?
5. **File it** — reusable lesson, no project nouns.

Worksheet and promotion test:
[`references/drill-worksheet.md`](references/drill-worksheet.md).

## Applying the doctrine

- **Retrospectively** (`genie-read`, `genie-error`): classify artifacts. After
  ~20, the distribution tells you where a project's real difficulty lives.
- **Prospectively** (`genie-review`): ask each class's detection questions of the
  diff. Most findings fall out of two or three.
- **In design** (`genie-write`): for each class, either own the boundary
  explicitly (validate, normalize, assign ownership) or declare that you do not
  and fail loudly there.

## The meta-lesson

> The hard part of software is not writing code that does the thing. It is
> writing code that keeps doing the thing in an environment you do not control,
> across states you did not enumerate, for people whose needs change.

Every genie is a different way of proving that sentence to yourself.
