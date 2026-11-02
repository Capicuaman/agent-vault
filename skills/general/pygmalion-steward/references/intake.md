# Intake — From Request to Decision

The Steward's core procedure. A request arrives as a solution ("make me a nerd for
X"); the job is to convert it into a *behavior problem*, then decide the minimum
response.

## Step 1 — Restate as a behavior problem

Strip the proposed solution. Ask what the agent currently does wrong, or cannot
do, and when.

| Request | Restated |
|---|---|
| "Make a nerd for Tailwind" | "When styling a template, I want the agent grounded in Tailwind v4 specifics instead of v3 habits." |
| "Create a skill for release notes" | "Every release, I retype the same changelog structure and get inconsistent prose." |
| "Add a forge for audit reports" | "I produce audit reports to a shape I keep re-inventing." |

If you cannot restate it without the word "skill"/"nerd"/"forge", the request is
not understood yet. Ask one sharpening question, then restate.

## Step 2 — Does it already exist?

Search before deciding. Cheap, and prevents the most common failure.

```bash
cd ~/Documents/agent-vault
grep -ril "<topic>" skills/*/*/SKILL.md registries/*.md README.md MANIFEST.md
python3 scripts/vault-audit.py --short
```

Three outcomes:

- **Exact match** → the verdict is *patch existing*, not *create*.
- **Adjacent match** → decide whether the new need is inside the existing routing
  boundary (patch) or genuinely separate (create, with a sharpened description).
- **Nothing** → continue.

## Step 3 — Is the need ripe?

Use the echelon gates in `prompt-skill-agent-triage` and, for production Families,
`forge-scout`'s five-signal checklist.

Minimum bar:

- The operation has been performed **≥5 times**, or a shape has **≥2 instances**
  (or ≥2 named candidates).
- The inputs and outputs are stable enough to describe.
- You can name **three concrete outputs** the Entity would produce.

If any bar fails → verdict *defer*, with the condition that would change the call.

## Step 4 — Decompose

Ask: how many routing boundaries does this contain?

| Test | Conclusion |
|---|---|
| Two user phrases would route to different behaviors | two Entities |
| Two user phrases would route to the same behavior | one Entity |
| One part is a step of the other | one Entity, sections |
| One part is a different Family (answers vs produces) | two Entities, different Families |
| One part is a rule, not a procedure | patch the Entity that already triggers there |

**Decomposition output:** a table of Entities with Family, Scope, and the reason
each is separate. If more than three Entities emerge, return a phased plan instead
and mark the verdict *defer*.

## Step 5 — Choose the Family and role

Follow the fit tree in [`taxonomy.md`](taxonomy.md). Then place it in the
[organization chart](org-chart.md): layer, reports-to, producer.

The two questions to answer explicitly:

1. **Does it answer, produce, detect, judge, govern, or audit?**
2. **Where does the ladder stop for this Family?**

## Step 6 — Set the gates

Fill the four gates before routing:

- **G1 Routable** — five must-fire and five must-not-fire utterances.
- **G2 Different** — the shadow test, stated in one sentence.
- **G3 Bounded** — non-goals and the hand-off owner.
- **G4 Registered** — the Registry of record and the absence of a ≥85% duplicate.

If any gate cannot be filled, the intake is not ready to route. Say which gate is
open and what is needed.

## Step 7 — Route

| Family | Route to |
|---|---|
| nerd | `nerd-forge` |
| forge | Steward + `_forge-pattern.md` spec |
| skill | `instruction-skill-forge`, or Steward directly for small ones |
| doctrine | Steward directly (must meet all four doctrine criteria) |
| steward | Operator approval — never self-created |
| genie | Steward directly, following `skills/genies/README.md` |
| scout | Steward directly, following `_tech-nerd-pattern.md` |

## Step 8 — Record

Produce the intake card (see `SKILL.md`), then in the same change:

1. Add or update the line in the **Registry of record**.
2. Update `README.md` (category table + total) and `MANIFEST.md` (section + total).
3. If a new Family: add its row to the org chart.
4. Bump counts in `scripts/vault-install.sh` only if a category total changed.

## Step 9 — Close

State the next action with an owner. An intake card without a next action is a
dead end.

---

## Rejection catalogue

Reject with a reason and a next action. A clean rejection saves more corpus than a
mediocre creation.

### Duplicate
*Signal:* description similarity ≥85%, or the trigger test matches a sibling, or
the restated request is already covered.
*Next action:* patch the existing Entity, or sharpen both descriptions.

### Premature
*Signal:* <5 runs; the shape is still changing; the request is a wish.
*Next action:* name the condition ("after the third report"), and record it in the
candidate list of the Family registry.

### Not an entity
*Signal:* it is data, a one-off prompt, a session note, or a section of an
existing Entity.
*Next action:* put it where it belongs — prompt file, note, or a section.

### Wrong family
*Signal:* it produces artifacts (forge), answers about one tech (nerd), detects
(scout), judges (doctrine), or governs (steward).
*Next action:* re-route with the correct producer.

### No delta
*Signal:* you cannot state `behavior(with) != behavior(without)`.
*Next action:* do not build. Either sharpen the need or drop it.

### Subsumed
*Signal:* two lines added to an existing Entity cover it.
*Next action:* patch, and note the addition in that Entity's changelog.

### Forbidden climb
*Signal:* the proposal is a meta level above a terminal Family —
`forge-forge`, `nerd-forge-nerd-nerd`, `doctrine-doctrine`.
*Next action:* fix the spec one level below instead.

---

## Intake questions, in the order that saves time

1. What does the agent do today that is wrong?
2. When does it happen — what would the user type?
3. Has it happened five times?
4. Does anything already cover it?
5. Is this one behavior or two?
6. Does it answer, produce, detect, judge, govern, or audit?
7. Where does the ladder stop?
8. What are the five must-fire phrases?
9. What must it hand off?
10. Who registers it, and in which file?

If you can answer all ten, the intake card writes itself.
