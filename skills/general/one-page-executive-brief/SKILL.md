---
name: one-page-executive-brief
description: Creates a decision-ready one-page executive brief from longer project docs, research memos, strategy notes, or technical plans. Use when the user needs a compressed leadership summary with recommendation, rationale, risks, required decisions, and near-term next steps.
---

# One-Page Executive Brief

Use this skill when a long document needs to become a **fast, executive-friendly decision artifact**.

The goal is not to summarize everything. The goal is to surface:
- what matters
- what should be decided
- why now
- what the recommendation is
- what the risks and next steps are

## What a strong one-page brief does

A strong executive brief helps a busy decision-maker answer these questions in under two minutes:

1. **What is this about?**
2. **What are you recommending?**
3. **Why is this the right move now?**
4. **What happens next?**
5. **What do you need from me?**

If the draft does not answer those clearly, it is not done.

## When to use this skill

Use this skill when the user asks for:
- a one-page executive brief
- a leadership summary
- a board-style summary
- a decision memo compressed to one page
- a project brief for founders, operators, or stakeholders
- a concise summary of a long strategy or R&D document

Do **not** use this skill for:
- educational explainers
- broad literature reviews
- detailed implementation plans
- meeting transcripts that still need interpretation

## Required workflow

### Step 1 — Read the real source material

Read the primary source document(s), not just the latest user message.

If several files matter, read the highest-signal ones first:
- main strategy doc
- source of truth / canonical spec
- decision logs
- budget / timeline / risk docs

Do not invent strategic certainty that the source documents do not support.

### Step 2 — Identify the decision frame

Before drafting, determine:
- **audience** — founder, leadership, operator, investor, client, etc.
- **decision type** — approve, prioritize, defer, fund, choose, align
- **time horizon** — immediate, quarter, year
- **stakes** — revenue, risk, speed, brand, operations, regulatory, technical feasibility

If the audience is not specified, default to:
- **internal leadership / operators**
- practical, direct, decision-oriented tone

### Step 3 — Extract only decision-critical content

Prioritize these elements:
- objective or problem
- recommendation
- business or strategic rationale
- options considered
- risks or constraints
- next 30/60/90 day steps
- explicit asks from leadership

Cut aggressively:
- background history unless it changes the decision
- definitions the audience already knows
- technical detail that belongs in the appendix
- duplicated reasoning

### Step 4 — Choose the tightest structure

Use the default structure unless the source clearly demands something else:

1. **Title**
2. **Decision summary**
3. **Why this matters / why now**
4. **Recommendation**
5. **Key risks or constraints**
6. **Next steps**
7. **Leadership asks**
8. **Bottom line**

Keep sections short.

## Style rules

- write for scanning, not for deep reading
- front-load the recommendation
- prefer bullets over dense paragraphs
- one idea per bullet when possible
- avoid jargon unless it saves space and the audience already knows it
- do not sound academic
- do not hedge unnecessarily
- be decisive, but stay faithful to the source material

## Compression rules

A one-page brief should feel like:
- **40% recommendation**
- **30% rationale**
- **20% execution / next steps**
- **10% risks / asks**

If the draft is mostly background, compress harder.

## Output quality checklist

Before finishing, verify:
- Is the recommendation visible in the first screenful?
- Can an executive understand the situation in under 2 minutes?
- Are the next steps clear?
- Is there an explicit ask, decision, or approval point?
- Did I remove detail that belongs in the longer source doc?
- Does the tone match the user's context?

## Default output behavior

When writing the brief:
- create or update a Markdown file if the user is working in repo-document mode
- clearly cite the source file(s)
- keep the brief standalone enough that it can be forwarded internally

If helpful, pair the brief with a pointer such as:
- `Source:` longer project document path

## Template reference

Read `references/template.md` if you need a concrete skeleton before drafting.
