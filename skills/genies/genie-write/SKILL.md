---
name: genie-write
description: Write change artifacts that teach — commit messages, pull request bodies, changelog entries, bugfix notes, and postmortems. Use when committing or opening a PR, when asked to write up a fix or a root-cause analysis, when documenting an incident, when writing release notes, or when the user wants their fix notes to be useful to future readers.
metadata:
  family: genies
  version: 2.0.0
---

# genie-write

**Leave better residue.** Every genie reads artifacts others produced. This one
makes you the producer — writing the smallest artifact that preserves the most
judgment for the person who hits the same boundary later.

## When to use this skill

- Committing a fix or opening a PR.
- Writing a changelog entry or release notes.
- Writing up a bugfix note or root-cause analysis.
- Writing an incident postmortem.
- The user asks "how should I document this fix?"

Use `genie-error` when recording an error **you** hit. Use `genie-read` to study
other people's artifacts. Use `genie-review` before you ship the change.

## The core rule

> **Write for the future reader who will hit the same boundary.** Optimize for
> two properties:
>
> - **Retrievability** — they can find it by the *symptom* they are seeing.
> - **Transferability** — the lesson survives without your project nouns.

Almost every bad change artifact fails one of these. "Fixed bug" fails both.

## The residue hierarchy

Each artifact has a different reader, half-life, and cost. Write the smallest one
that carries the judgment, and never write two that say the same thing.

| Artifact | Reader | Half-life | Carries |
|---|---|---|---|
| **Commit message** | `git log` / `blame` searcher | Long | Why, in one paragraph |
| **PR body** | Reviewer now, archaeologist later | Medium | Problem, evidence, approach, alternatives, risk |
| **Changelog entry** | User deciding whether to upgrade | Medium | User-visible symptom → new behavior |
| **Bugfix note** | You, and `genie-error` | Long | The full failure story + failed assumption |
| **Postmortem** | The whole org | Very long | Contributing factors, detection, action items |
| **Design doc / ADR** | Future maintainers | Very long | The model, and the rejected alternatives |

**Rule of thumb:** a commit message explains *why this line changed*. A PR body
explains *why this change and not another*. A bugfix note explains *why anyone
should care*. Do not collapse them into one.

## What each artifact must contain

Details, templates, and anti-patterns in the bundled references:

- [`references/commit-and-pr.md`](references/commit-and-pr.md) — commit subject/body, PR body skeleton, changelog entries, review responses
- [`references/postmortem.md`](references/postmortem.md) — blameless structure, timeline, contributing factors, action items
- [`references/bugfix-note.md`](references/bugfix-note.md) — the bugfix-note template that mirrors the `error-notes` eleven-section contract

## The four sentences every fix write-up needs

If you write nothing else, write these:

1. **Who was hurt and how** — the user-visible symptom, in their words.
2. **What was false** — the assumption that made the bug possible.
3. **Why this fix** — and what you rejected.
4. **How you know** — the positive verification, not "no error now".

A fix write-up missing sentence 2 is a changelog entry. Present in all four, it is
a bugfix note. Expanded with timeline and contributing factors, it is a postmortem.

## Rules

- **Symptom first, mechanism second.** Search engines and humans both match on
  symptoms. Put the error text or user complaint early, verbatim.
- **Quote the error.** Paraphrased errors cannot be found by the person pasting
  the real one.
- **Name the boundary.** Say explicitly which boundary was crossed (see
  [`../genie-doctrine/references/boundaries.md`](../genie-doctrine/references/boundaries.md)).
- **Record what did not work.** The dead ends are half the value of a triage log.
- **Separate fix from workaround.** Never let a workaround read as a fix.
- **Never say "various fixes" or "improvements".** Split the commit.
- **Do not assign blame to a person.** Assign it to a missing guard, a misleading
  message, or an unstated assumption.
- **Date and version everything.** "Fixed in 1.4.0" is the most useful phrase in
  a changelog.
- **Link, don't repeat.** A PR body links the issue; a changelog links the PR.

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| "Fixed bug" | Fails retrievability and transferability. |
| "Root cause: human error" | Stops the analysis one level too early. Ask what let the error through. |
| Changelog entry describing the implementation | Users search by symptom; implementers read the PR. |
| Postmortem with no timeline | Without detection point, you cannot reason about time-to-detect. |
| Action items with no owner or date | They do not happen. |
| Bugfix note with no failed assumption | You fixed the symptom and learned nothing. |
| Paraphrased error text | Unsearchable. |
| One giant commit | Destroys `git blame` and bisect — the two tools future-you needs most. |

## Checklist before publishing a write-up

- [ ] Can someone find this by pasting the error text?
- [ ] Is the failed assumption stated in one sentence?
- [ ] Is the rejected alternative named?
- [ ] Is the verification a positive check with output?
- [ ] Does the transferable lesson contain no project nouns?
- [ ] Is the boundary named?
- [ ] Are workaround and fix clearly separated?
