# Claim Audit

Converting a prose summary into a verdict table.

## Atomic claims

Split every sentence until each row tests **one** thing.

> "Zero zombies, ghosts, duplicates, or orphans and exits 0."

→ five rows. A mixed claim graded as a unit hides the wrong part.

## Verdicts

| Verdict | Test | Wording in the table |
|---|---|---|
| ✅ **Verified** | Reproduced now, level 4–5 evidence | `✅` + command → output |
| ⚠️ **Imprecise** | Right conclusion, wrong detail | `⚠️` + what is off |
| ❌ **Contradicted** | Evidence says otherwise | `❌` + the contradicting output |
| 🕰️ **Historical** | True at an earlier commit | `🕰️` + commit where it was true |
| ❓ **Unverifiable** | No evidence available now | `❓` + what would settle it |

## The five failure patterns to look for

### 1. The stale truth
The claim was accurate when written and is no longer.

> "Pygmalion is a doctrine." — true at `cb178af`, false at `HEAD`.

**How to catch it:** compare the claim's nouns against the *current* tree, not
your memory of the work. Search for the old noun.

### 2. The flattering metric
A number that sounds like health but measures something narrower.

> "The audit exits 0 — the corpus is clean."

Exit 0 means *no errors*, not *no findings*. Hollow and stale entities are
warnings. The claim is true and misleading at the same time.

**How to catch it:** always ask *what does this metric not count?*

### 3. The invisible omission
Something is missing from the summary and its absence reads as completion.

> A summary lists six delivered files but not the one deferred decision.

**How to catch it:** list what you *expected* to be there. Diff expectation
against the summary. The gap is the omission.

### 4. The unverified repetition
A claim carried forward from an earlier summary without re-running anything.

> "49 skills" repeated across three turns; nobody counted.

**How to catch it:** re-run the cheapest command that proves it. If a claim
survived two turns unchecked, check it now.

### 5. The self-serving adjective
"Clean", "robust", "complete", "zero" — words that assert a standard without
naming the test.

**How to catch it:** replace the adjective with the measurement. If the sentence
cannot survive, the adjective was doing the work.

## Evidence rules

- **One claim, one command.** Bundle nothing.
- **Quote the output, not your reading of it.** `→ 49` beats "it shows 49".
- **Separate existence from operation.** A file existing ≠ a file loading.
- **Separate warning from error.** Report both.
- **Never upgrade evidence by confidence.** "I'm sure" is not a verdict.
- **Check the inverse.** If the summary says X was removed, grep for X. If it says
  Y was added, check that Y loads.

## Table format

```markdown
| # | Claim | Verdict | Evidence | Note |
|---|---|---|---|---|
| 1 | 3 commits pushed | ✅ | `status -sb` clean, ahead=0, origin=210a75d | |
| 2 | 49 skills | ✅ | find/wc → 49; README 49; MANIFEST 49 | |
| 3 | corpus has no zombies | ✅ | audit summary has no zombie line | |
| 4 | "corpus is clean" | ⚠️ | hollow=1, stale=3 still reported | true only for errors |
| 5 | Pygmalion is a doctrine | 🕰️ | renamed at 210a75d | historical |
| 6 | drift found 2 | ✅ | drift exit 1; HA + rea listed | |
| 7 | rea drift 6.3→6.8 | ✅ | `npm view rea-agents version` → 6.8.0 | |
```

## Writing the verdict note

The note column is where orientation actually happens. Prefer:

- **What was true instead**, not just "wrong".
- **Which commit** changed it.
- **What the metric omits.**
- **What would settle it** for unverifiable claims.

## Rules for reporting the audit

1. Lead with contradictions and historical claims. They change decisions.
2. Report imprecision even when the conclusion holds — precision is the point.
3. State the evidence level when it is low; do not hide behind ✅.
4. If nothing was contradicted, say so plainly. A clean audit is a valid result —
   but only after the inverse checks (section "Evidence rules").

## Common false positives in a self-audit

| You will be tempted to… | Because | Instead |
|---|---|---|
| Mark ✅ because you ran the command | Action feels like verification | Mark ✅ only if the output matches the claim |
| Mark ❌ because a file is absent | Absence may be intentional | Check whether it was renamed |
| Skip the "not done" list | It is uncomfortable | It is the most useful part of the brief |
| Trust a green exit code | It is designed to be trusted | Read the findings above it |
| Grade the summary as a whole | Faster | Grade atomically; mixed claims hide errors |
