# Drill and Ambiguity Register

The two artifacts that turn a brief into bearings.

## The ambiguity register

Every long session leaves a residue of decisions that were made *for* the user
without being named. The register names them.

### Format

```markdown
| # | Ambiguity | Why it is ambiguous | Resolution | Status |
|---|---|---|---|---|
| 1 | `old-name` vs `new-name` | The entity was renamed; the old name survives in git history | Use `new-name` from `HEAD` | resolved |
| 2 | "doctrine" | Means a Family, and was also the old name of a Steward | Say "Doctrine (Family)" or "pygmalion-steward" | open |
```

Status is `resolved`, `open`, or `needs-user`. Anything `open` at the end of the
drill is the real agenda for the next turn.

### What belongs in it

| Trigger | Example |
|---|---|
| **Rename / supersession** | An entity changed name mid-session |
| **Polysemy** | One word now means two things across time |
| **Near-duplicate names** | `genie-drill` vs `orientation-drill` |
| **Wrong-family placement** | Something adjacent is not a member of the family it resembles |
| **Historical summary** | A claim true at commit N, quoted after N+1 |
| **Misleading metric** | Exit 0 that hides warnings |
| **Copy vs link** | Two locations that can silently diverge |
| **Locally-set config** | Identity/path set in one repo, not globally |
| **Coverage gap** | A sweep that only covers part of the corpus |
| **Deferred decision** | Something explicitly postponed, with no owner |

Ten entries is normal for a long session. Zero means the pass was shallow.

## The questions

### Tier design

| Tier | Purpose | Example shape |
|---|---|---|
| **T1 Facts** | confirm the map | "How many X, and what is HEAD?" |
| **T2 Decisions** | confirm the reasoning | "Why was A chosen over B?" |
| **T3 Risks** | confirm the judgement | "Does metric M mean the thing it appears to mean?" |
| **T4 Action** | confirm the next step | "What would you do next, and what would you check first?" |

### Rules

1. **6–9 questions.** Fewer is a quiz; more is an exam.
2. **At least two from T2 and two from T3.** Facts alone test reading, not
   understanding.
3. **Every question answerable from the evidence pass.** If it is not in the
   evidence, it is trivia.
4. **One question per decision.** Do not bundle.
5. **Include one question the user is likely to get wrong.** That is where the
   learning is.
6. **Withhold answers.** Offer them only after the attempt.

### Grading

Report by tier, not by score:

```
T1 3/3   T2 1/2   T3 1/2   T4 1/1
Weakest: T3 — the difference between "exit 0" and "clean".
```

Then offer the misses to `genie-drill` as cards. The tier with the most misses is
the next study target.

## The next-action question

The drill ends with a decision, not a fact:

> "Given the open loops, what is the single next action, and what would you verify
> first?"

A correct answer names:

1. **one** action (not a list),
2. the evidence that would confirm it is the right action,
3. what would make you abandon it.

If the user names three actions, that is a sign the brief did not separate
priority from inventory.

## Ambiguity → drill mapping

Every `needs-user` ambiguity should generate a T2 or T3 question. This is the
point of the loop: the register finds the soft spots, the drill tests them.

| Register entry | Drill question |
|---|---|
| Rename | "Which name is current at HEAD?" |
| Polysemy | "What does 'doctrine' mean in this sentence?" |
| Misleading metric | "The audit exits 0. What is it not counting?" |
| Wrong family | "Is Pygmalion a genie? Why not?" |
| Deferred decision | "What was deferred, and who owns it?" |

## Keeping the drill honest

- **Do not telegraph answers in the question.** "Why did we promote `_doctrine/`
  to a real skill, given flat installs?" gives away the reason.
- **Do not ask questions whose answers are in the question.**
- **Do not ask about things the user could not know.** Orientation tests the
  conversation, not clairvoyance.
- **Do not grade on recall alone.** A user who reconstructs the right answer from
  the evidence is more oriented than one who memorized it.
