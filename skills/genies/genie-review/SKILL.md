---
name: genie-review
description: Review a pending diff, pull request, or design for the bug classes that are hard to find — lifecycle, concurrency, environment, interface, input space, compatibility, and reproducibility. Use when reviewing code, when asked to look over a diff or PR, when reviewing a design or RFC before implementation, or when the user wants a second opinion on whether a change is safe to ship.
metadata:
  family: genies
  version: 1.0.0
---

# genie-review

**Apply the boundary lens to the present.** `genie-read` classifies fixes after
they ship. This skill runs the same taxonomy *before* — over a diff or a design —
to predict the bugs a change is about to create.

## When to use this skill

- Reviewing a diff, branch, or pull request.
- Reviewing a design doc or RFC before implementation.
- Asked "is this safe to ship?" or "what am I missing here?".
- Writing a review checklist for a team or a subsystem.

Use `genie-read` for published fixes, `genie-error` for failures you hit, and
`genie-write` for the artifacts around a change you ship.

## The method

### 1. Read the change for intent, not style

Before the boundary lens, answer: **what invariant does this change establish or
restore?** If the author cannot state it, that is the first finding.

### 2. Run the seven boundary passes

For each class in [`../genie-doctrine/references/boundaries.md`](../genie-doctrine/references/boundaries.md), ask
its detection questions of *this* diff. Most findings fall out of two or three
passes. Full question list with red flags:
[`references/review-checklist.md`](references/review-checklist.md).

| Pass | Ask |
|---|---|
| **Environment** | What does this assume about the OS, shell, encoding, cwd, or ambient config? |
| **Lifecycle** | What state does this add? Who releases it on *every* exit path, including cancel and crash? |
| **Concurrency** | What happens at the limit, in parallel, when cancelled mid-flight? |
| **Interface** | What contract does this rely on? What are its undocumented limits? What does it cache? |
| **Input space** | What classes of input are unhandled — empty, whitespace, non-ASCII, malformed? |
| **Human/time** | Who depends on the old behavior? What is their migration path? |
| **Reproducibility** | Does this work from a clean checkout, on target, with pinned inputs? |

### 3. Look for the three shapes of bad fix

These account for most reverted fixes:

- **Symptom patch** — suppresses the message without removing the condition.
- **New owned state** — adds a cache, flag, or registry that now needs an
  invalidation rule nobody wrote down.
- **Swallowed failure** — turns an error into a `null`, a retry, or a warning,
  moving the failure to a place with less context.

### 4. Check the verification

- Is there a test that **fails before and passes after**?
- Is it a *positive* check (the operation succeeds), not an absence check?
- Does it cover the boundary that was actually crossed?
- Is there a test for the case that used to crash — or only for the happy path
  plus the new fix?

### 5. Write findings as questions with evidence

A review comment should be actionable without being prescriptive:

> **Lifecycle:** this adds a module-level `listener` in `init()` but nothing
> removes it in `dispose()`. If `init()` runs twice — e.g. on reload — the second
> listener stacks. Is there a reason teardown is not symmetric here?

Structure: **boundary** → **the specific line** → **the concrete scenario** →
**the question**.

## Severity, not volume

Report in three tiers:

- **Blocking** — will corrupt state, leak a resource, or break existing users.
- **Should fix** — will fail on a boundary you can name, with a plausible trigger.
- **Consider** — a robustness or clarity improvement.

Do not pad. A review with two blocking findings is more useful than one with
twenty style notes. If the diff is genuinely fine, say so.

## When reviewing a design doc

Same lens, earlier:

- For each boundary: does the design *own* it (validate, normalize, assign
  ownership) or *assume* it?
- What is the failure mode when the boundary breaks, and who is paged?
- What is the change path for existing users?
- What is the simplest version that could work — and what was rejected?

The highest-value design comment is usually: **"what happens when X fails?"**,
where X is the boundary the doc does not mention.

## Cautions

- **Do not review style with this lens.** Use formatter/linter conventions for
  that; spend human attention on boundaries.
- **Do not assume the author missed it.** Ask. Many "missing" guards are owned
  elsewhere; the valuable finding is an *undocumented* ownership.
- **Diff size is a signal, not a finding.** A huge diff is harder to verify; say
  so, but do not block on it alone.

## Bundled references

- [`references/review-checklist.md`](references/review-checklist.md) — the full question set per boundary, with red flags and concrete examples
