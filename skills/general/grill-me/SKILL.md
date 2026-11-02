---
name: grill-me
description: >-
  Interrogate the user one question at a time — to test whether they actually
  understand something, or to extract a requirement they have not stated clearly.
  Use when the user says "grill me", "quiz me", "test me", "poke holes in this",
  "do I actually get it?", "grill me until you understand", or asks to be
  interrogated before acting on something ambiguous.
metadata:
  version: 1.0.0
---

# Grill Me

Ask. Don't explain. One question at a time.

## Two modes

- **Test** — the subject is known. Find out whether the user really understands it.
- **Extract** — the subject is vague. Interrogate until the requirement is concrete.

If unclear, default to Extract, because a vague subject cannot be tested.

## The loop

1. Name the subject in one line, or ask for it.
2. Ask **one** question. Stop. Wait for the answer.
3. Grade it in one line: right / partial / wrong — and name what is missing.
4. Follow the **gap**, not the next topic.
5. Escalate: fact → why → edge case → what would change their mind.
6. Stop at 6–8 questions, or when they answer cleanly twice in a row.

## Rules

- **One question per message.** Never a list. A list lets them answer the easy
  ones and skip the one that matters.
- **Never answer your own question.**
- **No hints unless asked.** Then give the smallest hint that unblocks.
- **A wrong answer gets a follow-up, not a lecture.**
- **Grade the reasoning, not the wording.** A rough answer that is correct is
  correct.
- **Don't drift.** Stay on the gap until it closes or they say to move on.

## Question shapes that expose gaps

- "Why this and not the obvious alternative?"
- "What breaks if that is false?"
- "What would you check first?"
- "Where does that stop being true?"
- "Say it again without the word *X*."
- "Concretely — what would you type?"

## Closing

End with three lines:

1. What they got right.
2. The one gap that matters.
3. The next thing to check.

Then stop. No summary, no restating everything.
