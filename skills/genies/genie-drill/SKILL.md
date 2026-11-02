---
name: genie-drill
description: Turn software-engineering lessons into durable skill through deliberate practice — the five-step drill, building casebooks from changelogs and postmortems, converting lessons into Anki cards, and weekly review rituals. Use when the user wants to practice or be quizzed on bug classes, wants to build a casebook, wants lessons turned into flashcards, asks for a study plan or drill, or wants to track their progress toward mastery.
metadata:
  family: genies
  version: 2.0.0
---

# genie-drill

**Convert residue into skill.** Reading change artifacts builds recognition.
Only retrieval builds recall. This skill is the training loop that connects
`genie-read`, `genie-error`, `genie-write`, and `genie-review` into something that
changes how you think under time pressure.

## When to use this skill

- "Drill me" / "quiz me" on bug classes or recent lessons.
- "Help me build a casebook" from a changelog or postmortem set.
- "Turn these lessons into Anki cards."
- "Give me a study plan for getting better at software engineering."
- "Am I actually improving?"

For the knowledge itself, use `genie-read` and `genie-error`. For card mechanics,
use the `anki-admin` skill.

## The mastery ladder

Each rung is a different activity. Do not skip to the top.

| Rung | Activity | Evidence you are here |
|---|---|---|
| 1. **Recognize** | Read classified artifacts | You can name the boundary of a fix after reading it |
| 2. **Recall** | Answer boundary questions without notes | You name the boundary from the *symptom alone* |
| 3. **Predict** | Guess the fix before reading the diff | You are right more than half the time |
| 4. **Detect** | Find the boundary in a pending diff (`genie-review`) | Your reviews produce findings others missed |
| 5. **Prevent** | Design the boundary out before code exists | Your designs need fewer lifecycle/concurrency fixes |
| 6. **Teach** | Explain the class with no project nouns | Your lesson transfers to a different stack |

Track which rung you are on per boundary class — mastery is uneven.

## The core drill (one artifact, ~20 minutes)

Full worksheet: [`../genie-doctrine/references/drill-worksheet.md`](../genie-doctrine/references/drill-worksheet.md).

1. **Reconstruct** the failure from the issue, not the summary.
2. **Name the boundary** — one of the seven in
   [`../genie-doctrine/references/boundaries.md`](../genie-doctrine/references/boundaries.md).
3. **Read the diff** — why is the fix *this* size? What did it preserve?
4. **Counterfactual** — what upstream decision would have made this impossible?
5. **File it** — reusable lesson, no project nouns.

### The prediction variant (rung 3)

Highest-yield form, and it takes discipline:

1. Read only the changelog line and the issue.
2. Write down: boundary class, likely fix, likely file.
3. **Then** read the diff.
4. Score yourself. A wrong prediction is worth more than a right one — record what
   misled you.

Keep a running log:

```markdown
| Date | Artifact | Predicted boundary | Actual | Predicted fix | Right? | What misled me |
|------|----------|--------------------|--------|---------------|--------|----------------|
|      |          |                    |        |               |        |                |
```

Review the "what misled me" column monthly. It is a map of your blind spots.

## Building a casebook

A casebook is one release or one incident set, fully classified. Model:
[`../genie-read/references/casebook-pi-1.4.0.md`](../genie-read/references/casebook-pi-1.4.0.md).

1. Pick **one release** or **one postmortem collection**.
2. Copy every *Fixed* entry (skip *Added* — features are easy).
3. Classify each by boundary.
4. Write one transferable lesson per entry, stripped of project nouns.
5. Count the distribution. It tells you where that project's real difficulty lives.
6. Do a **second** release from the same project and compare distributions.

### What the distribution tells you

- Dominated by **environment** → the project fights portability.
- Dominated by **lifecycle** → it owns too much state.
- Dominated by **interface** → it depends on providers it cannot see.
- Dominated by **input space** → it never fuzzed its parser.

Compare your *own* `error-notes` distribution against a project you admire. The
gap is your curriculum.

## Anki conversion

Use the `anki-admin` skill for the collection itself. The conversion rule matters
more than the card format:

**One card = one boundary decision.**

- **Front:** the *symptom scenario only*, no tool name.
  > "A CLI reads a JSON config written by a Windows GUI tool. It fails to parse on
  > one machine but not the developer's. What is the likely cause, and where
  > should the fix live?"
- **Back:** the boundary class, the mechanism, and the fix location.
  > "Environment. The writing tool prepends a UTF-8 BOM; the parser does not strip
  > it. Fix at the parse boundary, not at every call site."

Rules:

- **Never** make a card that is only a fact ("what does `--no-config` do?"). Facts
  decay; boundary decisions transfer.
- **Do** make cards from `failed_assumption` fields — they are pre-written
  misconceptions.
- **Do** use cloze for the seven boundary names once, then never again.
- **Do not** card more than ~3 lessons per artifact. Selectivity is the skill.

## Weekly ritual (15 minutes)

1. `errlog.py list` — what repeated in your own errors?
2. Pick the top entry; check its transferable lesson still holds.
3. Add one line to the prediction log if you did a drill.
4. Promote one recurring pattern into a guardrail: an alias, a preflight check, a
   checklist line, or an upstream bug report.
5. Retire one belief you can no longer defend.

## Monthly ritual (45 minutes)

1. Distribution check: boundary counts across your `error-notes` and casebooks.
2. Find your weakest rung per class; pick one activity that targets it.
3. Review "what misled me" — name the top two blind spots.
4. Convert the three best lessons into Anki cards.
5. Update the mastery table.

## Progress log

Keep it short and honest. One file, append-only:

```markdown
## YYYY-MM

- Casebooks built:
- Artifacts drilled:
- Prediction accuracy: X/Y
- New guardrails promoted:
- Blind spot discovered:
- Rung changes: <class> 2 -> 3
```

The system is working when you recognize a bug's class before you finish reading
its symptom, and when your reviews find boundaries the author did not see.

## Cautions

- **Recognition is not recall.** Rereading feels productive and teaches almost
  nothing. Always try to answer before looking.
- **Breadth before depth.** Twenty drills across the seven classes beats sixty
  drills in one class you already understand.
- **Do not card the artifact.** Card the *decision*. Facts about a specific
  version are worthless next year.
- **Uneven mastery is normal.** You will be rung 5 in concurrency and rung 2 in
  compatibility. Target the low rung, not the one that feels good.
