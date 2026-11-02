# Bugfix Note

A bugfix note is the artifact you write after fixing something, for the person who
will hit the same boundary later. It sits between a PR body (too code-specific) and
a postmortem (too org-specific).

This template mirrors the eleven-section contract of the `error-notes` library so
that entries stay interchangeable between the two systems. See
`../../genie-error/references/entry-contract.md`.

## When to write one

- The bug cost more than ~5 minutes, or
- the cause was non-obvious, or
- it is likely to recur, or
- it revealed a wrong assumption.

Otherwise the commit message is enough.

## Template

````markdown
---
id: "BUG-YYYY-MM-DD-NNN"
title: "<symptom in one line, not the cause>"
date: "YYYY-MM-DD"
status: resolved
severity: medium
boundary: environment | lifecycle | concurrency | interface | input | human-time | reproducibility
failed_assumption: "<the belief that made this surprising>"
confidence: verified | probable | hypothesis
related: []
---

## 1. Symptom

<What a user saw, verbatim error text if any. No cause here.>

## 2. Impact

<Who was blocked, for how long, and the workaround.>

## 3. Reproduction

```sh
<the smallest command that still fails>
```

<Deterministic? Environment-specific? Prerequisites?>

## 4. Evidence

```text
<verbatim error output, stack top frame, relevant log lines>
```

## 5. Triage log

1. <action> -> <finding>
2. <dead end, and why it looked promising>

## 6. Root cause

- **Proximate:** <the failing condition>
- **Underlying:** <why that condition existed>
- **Aggravating:** <what made detection or recovery harder>

## 7. Fix

<The change, in behavior terms. What invariant it restores.>

## 8. Alternatives rejected

- **<option>** — rejected because <reason>.

## 9. Verification

<Positive check with command and output.>

## 10. Prevention

<What would have caught this earlier: a test, a guard, a message fix, a
preflight check, an upstream report.>

## 11. Transferable lesson

<One paragraph, no project nouns. The rule that generalizes.>
````

## Why each section exists

| Section | Prevents |
|---|---|
| Symptom first | Future readers giving up because the title describes the mechanism |
| Impact | Misjudging severity and re-inventing a workaround that already existed |
| Reproduction | "Cannot reproduce" wasting a second investigation |
| Evidence verbatim | Unsearchable paraphrase |
| Triage log | Re-walking dead ends; it is the most valuable section for future-you |
| Root cause split | Fixing the proximate condition and leaving the underlying one |
| Alternatives rejected | The next person "fixing" it back the way you rejected |
| Positive verification | Shipping a fix that merely stops the error message |
| Prevention | The same class recurring with a different symptom |
| Transferable lesson | A diary entry instead of a library entry |

## Converting between the two formats

`error-notes` entry → bugfix note:

- `Symptom`, `Impact`, `Reproduction`, `Evidence` map 1:1.
- `Triage log` maps 1:1.
- `Root cause` maps 1:1.
- `Resolution` + `Verification` → `Fix` + `Verification`.
- `Prevention` maps 1:1.
- `Transferable lesson` maps 1:1.
- `Automation notes` has no equivalent — keep it only if the capture tooling
  story matters.
- Add `boundary` and `Alternatives rejected`, which the error-notes contract
  does not have.

## The one-sentence test

After writing, cover everything except `## 11. Transferable lesson`. If the lesson
alone teaches someone who has never seen your code, the note is good. If it
mentions your product, it is a fact sheet, not a lesson.
