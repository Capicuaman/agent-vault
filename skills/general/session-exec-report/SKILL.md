---
name: session-exec-report
description: "Write a decision-ready executive report on the current pi session (or a specified slice of it) into 00_INBOX/exec-reports/. Use when the user says 'exec report on this session', 'summarize what we did', 'brief me on the <topic> work', 'informed executive report', 'session recap', 'write up what we built', 'send this to inbox as a brief', or asks for an actionable one-pager covering decisions made, artifacts produced, open questions, and next steps. Scope-flexible: full session or a named sub-thread (e.g. 'just the nerd-forge work', 'only the herdr diagnosis part'). Routes output to 00_INBOX for PARA triage. Complements one-page-executive-brief (which operates on existing documents, not conversations)."
---

# session-exec-report

Compress a pi conversation \u2014 the full session or a named slice \u2014 into a **decision-ready executive report** written to `00_INBOX/exec-reports/`. Future-you (or anyone else reading the inbox) should be able to answer in under two minutes: *what did we do, why, what's next, what's still open.*

## When this fires

- "exec report on this session" / "session recap" / "brief me on what we did"
- "write up the <topic> work" (e.g. "the nerd-forge work", "the herdr diagnosis")
- "send this to inbox as a brief"
- "informed executive report on <scope>"
- Any ask for an actionable one-pager summarizing live work, not an existing document

**Do NOT fire for:**
- Summarizing an existing document \u2192 use `one-page-executive-brief`
- Journaling raw events \u2192 use `daily-journal`
- Planning upcoming work \u2192 use `tasks/todo.md` directly

## Scope resolution (ask once if ambiguous)

Three legitimate scopes:

1. **Full session** \u2014 everything since this pi conversation started
2. **Named thread** \u2014 e.g. "the nerd-forge work", "the herdr diagnosis", "the training track build"
3. **Explicit range** \u2014 "from when we started talking about X" / "the last hour"

If the user said "write an exec report" without qualifier, ask once: *"Full session, or just the <most-recent-coherent-thread>?"* Then proceed. Don't ask twice.

## Output location & naming

```
00_INBOX/exec-reports/YYYY-MM-DD-<slug>.md
```

- Date = today's date (local, `date +%F`)
- Slug = kebab-case, 2\u20134 words, topic-driven. Examples:
  - `2026-10-06-nerd-skills-herdr.md`
  - `2026-10-06-bilan-label-audit.md`
  - `2026-10-06-session-full.md` (for full-session reports with no narrower topic)
- If the file already exists today for the same slug, append `-2`, `-3`, etc.

Create `00_INBOX/exec-reports/` if it doesn't exist. Routing to `00_INBOX` deliberately \u2014 reports are raw material pending PARA triage, not finished references.

## Report structure (the one-pager)

Exactly these sections, in this order. **Target: 1 printed page / \u2264 500 words of actual prose** (tables and code blocks don't count toward the budget).

### 1. Headline
One sentence. What did we accomplish, in plain language. No jargon unless the audience is technical.

### 2. Verdict
One short paragraph (3\u20134 sentences). The "if you only read one thing" summary. Includes the recommendation if there is one.

### 3. What we did
A tight bulleted list of concrete actions. Each bullet = one verb + one object + optional artifact path.
- "Installed Herdr's official agent skill \u2192 `~/.pi/agent/skills/herdr/SKILL.md`"
- "Regenerated the Herdr command reference against live 0.9.3 \u2192 `03_RESOURCES/.../herdr-command-reference-0.9.3.md`"

### 4. Why it matters
2\u20134 sentences on the strategic / practical case. Connect to a goal the user has stated or a problem they were having. If no clear "why," say so and ask for one.

### 5. Key findings & surprises
What did we learn that we didn't know going in? Dated, specific, honest.
- "Server-side protocol drift (CLI 22 vs server 11) silently blocks the API; `herdr --version` doesn't catch it."
- "The agent-guide claims 4 env vars inject per pane; reality on older servers is 2."

### 6. Decisions required
What does the user still need to decide? Explicit. If nothing \u2192 say "None pending."

### 7. Next steps
Concrete, time-boxed. Each item = who + what + when (even if "when" is just "today / this week / before next session"). Prefer 3\u20135 items. More = you haven't prioritized.

### 8. Artifacts produced
Files created or substantively modified, with absolute or repo-root paths. One line each. This is the paper trail.

### 9. Open questions / risks
What might bite later. Dated. Honest. If none, say "None flagged." Don't invent risks for symmetry.

### 10. References
URLs, docs, prior reports, related tasks. Links the reader could follow for depth.

## Voice rules

- **Decision-ready, not narrative.** No "we started by..., then we...". That's for the journal.
- **Honest.** If something failed, say so. If we didn't finish, say so. If the user hasn't given a goal, say so.
- **Pathed.** Every artifact mentioned has a full path. Future-you is searching.
- **Dated.** Every finding has today's date in parens if it's novel. Enables drift tracking.
- **No marketing.** This is an internal report, not a pitch.

## Pre-write checklist

Before writing, confirm you can answer:
1. **What was the user's goal in this session?** If unclear, ask once before writing.
2. **What's the smallest claim per bullet?** Each item should be defensible on its own.
3. **What would a future-me ask that this report doesn't answer?** Add it to \u00a79.
4. **Is anything in here speculation vs. observed fact?** Mark speculation explicitly.

## After writing

1. Confirm the file was created at the right path.
2. Print the path + a 3-line preview to the chat.
3. Suggest a PARA destination (e.g. "when triaging: likely `01_PROJECTS/<project>/decisions/` or `03_RESOURCES/...`").
4. Offer to append a `herdr-practice`-style entry to today's journal if the work was training-related.
5. Update `tasks/todo.md` Review section with a one-liner pointing to the report.

## Anti-patterns

- Writing 2000-word reports. Executive = short. If you need more, write a secondary deep-dive and link to it from \u00a710.
- Reports with no "decisions required" section populated \u2014 that defaults to "None pending," which is a legitimate state.
- Reports with no artifact paths \u2014 the whole point is reproducibility.
- Reports with imaginary surprises invented for symmetry \u2014 if nothing surprised you, say so.
- Reports that read like the chat transcript \u2014 compress aggressively; the transcript is the source, not the output.

## Composition with other skills

- **`one-page-executive-brief`** \u2014 use when the input is an existing document, not a conversation. Same output discipline, different input source.
- **`daily-journal`** \u2014 for raw event capture. The exec report is a *distillation* of what the journal would also note; cross-reference in \u00a710.
- **`prompt-skill-agent-triage`** \u2014 if the session itself produced a new workflow, consider whether that workflow should become a skill before writing the report.

## Reference examples

- First application (2026-10-06): `00_INBOX/exec-reports/2026-10-06-nerd-skills-herdr.md` \u2014 the *-nerd + herdr-nerd + training-track + global-promotion work from this session.
