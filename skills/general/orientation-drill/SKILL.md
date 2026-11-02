---
name: orientation-drill
description: >-
  Reconstruct the true state of in-flight work from artifacts, audit a summary's
  claims against evidence, surface ambiguity and open loops, then drill the user
  with escalating questions until they have their bearings. Use when someone says
  "drill me", "get my bearings", "where are we", "catch me up", "we're moving too
  fast", "is that summary accurate", "verify what you just said", or after a long
  multi-step session where names, decisions, or counts may have drifted.
metadata:
  version: 1.0.0
  family: skill
---

# Orientation Drill

A summary is a **claim set**. Orientation is the act of testing it against reality
and then proving you understand the result.

This skill exists because long sessions accumulate three kinds of rot:

1. **Drift** — names change, counts move, files are renamed.
2. **Self-report bias** — the agent that did the work also wrote the summary, and
   summaries flatter their authors.
3. **Silent ambiguity** — decisions were made without being named, so the user
   cannot tell what was chosen *for* them.

## The loop

```
EVIDENCE → CLAIM AUDIT → STATE BRIEF → AMBIGUITY REGISTER → DRILL
```

Never start at the brief. The brief must be downstream of evidence, or it is just
a second summary.

| Step | Output | Reference |
|---|---|---|
| **Evidence** | raw facts: git state, file existence, audit output, loader output | [`references/evidence-pass.md`](references/evidence-pass.md) |
| **Claim audit** | every claim → verdict + evidence | [`references/claim-audit.md`](references/claim-audit.md) |
| **State brief** | what exists, what changed, what is open | this file |
| **Ambiguity register** | unresolved names, decisions, and assumptions | [`references/drill.md`](references/drill.md) |
| **Drill** | 6–9 escalating questions, answers withheld | [`references/drill.md`](references/drill.md) |

## Non-negotiables

- **Verify, do not restate.** A claim without a command or file behind it does not
  enter the brief.
- **Mark the unverifiable as unverifiable.** Never call something "wrong" because
  you could not check it, and never call it "verified" because it sounds right.
- **Report what is missing as loudly as what is done.** A clean summary that omits
  the open loops is worse than a messy one that includes them.
- **Test decisions, not trivia.** The drill must ask *why*, not only *what*.
- **Brevity is part of orientation.** A brief nobody finishes is not an
  orientation. One screen for the brief, one for the drill.

## The claim-audit verdicts

| Verdict | Meaning |
|---|---|
| ✅ **Verified** | Reproduced with a command and its output |
| ⚠️ **Imprecise** | True in substance, wrong in a detail |
| ❌ **Contradicted** | Evidence says otherwise |
| 🕰️ **Historical** | Was true and has since been superseded |
| ❓ **Unverifiable** | No available evidence; state what would settle it |

`🕰️ Historical` is the one most often missed: a summary can be true of an *earlier
commit* and false of `HEAD`. Check the current tree, not your memory of the work.

## The state brief

Five blocks, in this order:

1. **Now** — HEAD, branch, working-tree state, counts, what the audit says.
2. **Timeline** — the commits, one line each, oldest to newest.
3. **What exists** — the entities/artifacts this session produced.
4. **Open loops** — drift, staleness, hollow entities, uncommitted work, deferred
   decisions.
5. **What is *not* done** — explicitly. Silence reads as completion.

## The ambiguity register

List every place where the conversation is one misreading away from confusion:

| Ambiguity | Why it is ambiguous | Resolution | Status |
|---|---|---|---|

Typical entries:

- A rename, where the old name survives only in git history.
- One word with two meanings across time ("doctrine" as a Family vs as the old
  name of `pygmalion-steward`).
- Two Entities with similar names doing different jobs.
- A summary that was true at commit N and is now historical.
- A metric whose exit code suggests "clean" but hides warnings.
- An install location that is a copy, not a link, and can silently diverge.

If the register is empty, you have not looked hard enough.

## The drill

6–9 questions, escalating:

| Tier | Tests |
|---|---|
| **T1 Facts** | counts, names, current state |
| **T2 Decisions** | why this shape, what was rejected |
| **T3 Risks** | what is stale, what is misleading, what would break |
| **T4 Action** | what to do next, and what to verify first |

Rules:

- **Withhold the answers.** A drill with the answers visible is a reread.
- **Mix tiers.** Fact questions warm up; decision and risk questions are the point.
- **Every question must be answerable from the evidence pass.** If not, cut it.
- **Grade honestly**, naming the tier where the user stumbled, and offer to feed
  the misses to `genie-drill` for spaced repetition.

## When to insist on this

Run it, even if not asked, when any of these appears:

- The same entity has been renamed or superseded within the session.
- A count or claim is about to be repeated that has not been re-verified.
- The user says "we are moving too fast" or asks for a recap.
- Three or more commits have landed since the last orientation.
- A summary is being relied on to make a decision.

## Anti-patterns

| Anti-pattern | Why it defeats the purpose |
|---|---|
| Restating the summary with nicer formatting | Zero new information |
| Only checking facts | Misses the decisions and ambiguity that cause rework |
| Marking everything ✅ because the commands ran | A command running is not a claim being tested |
| Dumping every command output | Orientation is compression, not logging |
| Giving answers with the questions | Turns a drill into a reread |
| Ending without a next action | The point is bearings, not trivia |

## Hand-offs

| Need | Use |
|---|---|
| Turn misses into retention | `genie-drill` |
| Corpus-level truth (entities, drift, duplicates) | `pygmalion-steward` + `scripts/vault-audit.py` |
| Safe commit/push of what the brief found | `git-care` |
| Reconstruct *why* a system is shaped this way | `genie-read` |
