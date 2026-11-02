# Drill Worksheet

Copy this template and fill it in for **one** fix. Do twenty; you will start
predicting bug classes before reading the fix.

---

## Fix under study

- **Project / version:**
- **Issue / PR / commit:**
- **One-line changelog entry:**

## 1. Reconstruct the failure

- What was the system state before the bug?
- What did the user (or caller) do?
- What happened instead of what should have happened?
- What did the *summary* leave out that the *issue* contained?

## 2. Name the boundary

Which boundary was crossed? (circle one, or add)

`environment` · `lifecycle/state` · `concurrency` · `interface/contract` ·
`input space` · `human/time` · `reproducibility`

- Why that one? What did the author not control?

## 3. Read the diff

- Diff size vs symptom size:
- What did the fix have to *preserve* while changing?
- What is the one line that actually matters?

## 4. Counterfactual

- What upstream design decision would have made this bug impossible?
  (Usually: don't own that state, or fail loudly at the boundary.)
- Could a test have caught it earlier? Which one?
- Is the fix a band-aid, a root-cause fix, or a constraint finally respected?

## 5. File it

- Boundary category:
- Reusable lesson (one sentence, no project nouns):
- Where have I seen this pattern before?

---

## Reusable lesson examples (no project nouns)

- "State set on a shared resource must be released on every exit path, including
  abnormal ones."
- "Never parse config written by a tool whose output format you do not control
  without stripping BOMs and normalizing encoding."
- "An environment variable that silently changes tool semantics is worse than a
  missing feature."
- "When a resource pool is exhausted, queue with a deadline instead of failing
  immediately."
- "Classify retryable errors by cause, not by message substring."
- "A cache is only as correct as its invalidation guarantee; write the guarantee
  down or do not cache."
- "Changing a default is a breaking change with a longer blast radius than changing
  an API."

## Promotion test

A lesson is ready to leave the worksheet when it:

1. Contains no project nouns (no product, package, or file names).
2. Predicts a bug you have not seen yet.
3. Can be turned into a checklist question (see `genie-review`).
4. Can be turned into one Anki card (see `genie-drill`).
