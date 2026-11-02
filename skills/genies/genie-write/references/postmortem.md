# Postmortem

A postmortem is a bugfix note for an event that affected other people. The
difference is not length — it is that a postmortem must explain **how the system
failed as a system**, including why it was not caught sooner.

## Blameless, precisely

"Blameless" does not mean "nobody did anything". It means the analysis targets the
conditions that made the action reasonable at the time:

- ✗ "The engineer ran the wrong command."
- ✓ "The command's name differed by one character from the safe one, and the safe
  one was documented in a different file than the dangerous one was defined."

If the root cause is a person, the analysis stopped one level too early.

## Structure

```markdown
# <Incident title: the user-visible effect, not the mechanism>

**Status:** resolved | mitigated | monitoring
**Severity:** SEV1 | SEV2 | SEV3
**Duration:** <start> → <end> (<total>)
**Time to detect:** <minutes>
**Time to mitigate:** <minutes>
**Author:** <name>
**Reviewers:** <names>

## Summary

<Three or four sentences a non-engineer can follow: what broke, who was
affected, how long, and how it ended.>

## Impact

<Quantified where possible: requests failed, users affected, data lost, revenue,
SLO burn. Distinguish "degraded" from "unavailable".>

## Timeline

All times UTC. Mark detection, mitigation start, and resolution explicitly.

| Time | Event |
|---|---|
| 14:02 | Deploy of <change> begins |
| 14:07 | Error rate on <endpoint> rises from 0.1% to 12% |
| 14:19 | **Detected** — alert `HighErrorRate` fires |
| 14:24 | **Mitigation started** — rollback initiated |
| 14:31 | **Resolved** — error rate back to baseline |
| 15:10 | Root cause identified |

Do not omit the boring minutes. Time-to-detect is the most actionable number in
the document.

## Contributing factors

Not "the cause" — factors, plural. Most incidents are interactions.

- **Trigger:** the change or event that started it.
- **Latent condition:** the pre-existing weakness it exposed.
- **Detection gap:** why monitoring did not catch it earlier.
- **Response gap:** why mitigation took as long as it did.
- **Amplifier:** what made the impact larger than expected.

## What went well

<Genuinely. Fast rollback? Good runbook? Clear escalation? This is how you learn
which safeguards to keep investing in.>

## What went poorly

<Blunt, still blameless. Unclear ownership, missing dashboards, ambiguous alerts.>

## Where we got lucky

<The most underrated section. Luck is a latent incident. "The deploy happened at
low traffic" is a finding, not a comfort.>

## Action items

Every item needs an owner, a date, and a type:

| Action | Type | Owner | Due |
|---|---|---|---|
| Add alert on <signal> | detect | @person | date |
| Make <dangerous op> require confirmation | prevent | @person | date |
| Document <runbook step> | mitigate | @person | date |

Types: **prevent** (stop it happening), **detect** (catch it sooner),
**mitigate** (recover faster), **learn** (understand it better).

Prefer **detect** and **mitigate** over **prevent** when the failure class is
inherently open-ended — you cannot prevent every boundary, but you can shorten
detection.

## Lessons

<One to three transferable rules, no project nouns, in the same spirit as a
bugfix note's `Transferable lesson`.>

## Appendix

<Graphs, logs, code links, the exact error text. Verbatim.>
```

## Rules

1. **Write it within a week.** Memory decays faster than you think, and the
   timeline is the first thing to go.
2. **Times are absolute and timezone-marked.** Relative times ("five minutes
   later") are unusable in review.
3. **Quantify impact.** "Many users" is not impact.
4. **Name detection explicitly.** It is the number that determines whether the
   next incident is shorter.
5. **Action items must be closable.** "Improve monitoring" is not an action item.
6. **No single root cause.** If you wrote one, you likely stopped early.
7. **Publish internally by default.** A postmortem nobody reads teaches nobody.

## Review questions

- Could a new engineer reconstruct the incident from the timeline alone?
- Does every contributing factor have a corresponding action item?
- Are the action items detect/mitigate as well as prevent?
- Is "where we got lucky" honest, or is it empty?
- Would the transferable lesson still be true in a different codebase?
