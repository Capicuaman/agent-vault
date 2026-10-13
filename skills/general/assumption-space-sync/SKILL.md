---
name: assumption-space-sync
description: Synchronize project files when new facts invalidate old assumptions. Use when discovery/intake reveals new information that affects multiple documents, HTML pages, or decision matrices across a project. Tracks assumption space, generates intake forms, and orchestrates file-by-file propagation.
---

# Assumption Space Sync

When new facts arrive — a discovery call, an intake form, a legal document, a survey — they often invalidate assumptions baked into project files. This skill provides a repeatable workflow to:

1. **Capture** new facts in a structured HTML intake form
2. **Extract** assumptions and map them to affected files
3. **Propagate** changes across the entire project, including HTML, Markdown, JSON, and code
4. **Log** what changed and why, for auditability

## Core concept: Assumption Space

Every project file carries implicit assumptions:
- "Mom is sick" → affects legal strategy, medical checklists, tone of broker pitches
- "There are 3 heirs" → affects voting math, expense splits, matrix visualizations
- "Property is second-line beach" → affects ZOFEMAT risk, pricing, buyer pool

When intake reveals the true state, **every file whose assumptions changed must be updated**. Missing one creates a ticking bomb: a legal doc with wrong heir count, a pitch with wrong urgency, a calculator with wrong denominator.

## When to use this skill

- A discovery form, survey, or interview yields new facts
- A stakeholder reveals information that contradicts prior planning docs
- You need to commit intake results and then sync them across the project
- You want an auditable trail of which assumptions changed and when

## Workflow

### Step 1 · Intake

Open `assets/assumption-intake-form.html` in a browser. Fill out the assumption grid:

| Column | Purpose |
|---|---|
| **Assumption ID** | Short code (e.g., `HEIR-COUNT`, `MOM-STATUS`) |
| **Old belief** | What the project files currently say |
| **New fact** | What intake / discovery revealed |
| **Confidence** | `confirmed` / `likely` / `hearsay` |
| **Affected files** | Comma-separated paths or glob patterns |
| **Impact** | `critical` (wrong = legal/financial risk) / `important` (user confusion) / `cosmetic` |

Export as JSON. Save to `discovery/assumptions-YYYY-MM-DD.json`.

### Step 2 · Commit baseline

```bash
git add -A && git commit -m "baseline before assumption sync"
```

This creates a rollback point. If propagation goes wrong, `git reset --hard HEAD~1`.

### Step 3 · Read affected files

For each file in the Affected files column:

```bash
grep -n -i "<old belief fragment>" <file>
```

This gives line numbers and context for every occurrence.

### Step 4 · Propagate edits

Use `edit` for precise text replacement. Rules:
- **One file at a time** if many changes; batch only non-overlapping edits
- **Old text must match exactly**, including whitespace
- **Verify with read after each edit**
- **Never trust mental models** — always grep before editing

Priority order:
1. **Critical assumptions first** (legal docs, tax strategies, contracts)
2. **HTML calculators second** (numbers, defaults, labels)
3. **Pitch / meeting prep third** (heir count, tone, urgency)
4. **Index / overview last** (links, summaries, status badges)

### Step 5 · Update assumption tracker

In the intake form, mark each assumption as `synced` and note the commit hash.

### Step 6 · Log in project task file

Append to `tasks/todo.md`:

```markdown
- [x] YYYY-MM-DD — Assumption sync: `<Assumption IDs>` applied across `<N>` files. Commit: `<hash>`.
```

## HTML Intake Form

The form lives at `assets/assumption-intake-form.html`. It is a standalone, auto-saving browser form that:

- Generates a unique Assumption ID for each row
- Highlights `critical` impact rows in red
- Exports JSON + Markdown
- Tracks sync status per assumption

Open it directly in a browser, or serve it with any static server:

```bash
npx serve /path/to/skill/assets
```

## Reference

See `references/propagation-guide.md` for:
- Detailed grep-to-edit patterns
- Safe batching strategies
- HTML-specific propagation (default values, labels, option counts)
- Markdown table updates
- Common pitfalls (overlapping edits, regex greed, whitespace traps)

## Example invocation

User says:
> "The discovery form came back. Mom is healthy, not sick. There are 4 heirs, not 3. The property address is Sabalos cerritos 11, beachfront with pool. Commit and sync everything."

Agent executes:
1. `git add -A && git commit -m "add discovery intake files"`
2. Read `discovery/assumptions-YYYY-MM-DD.json` to extract new facts
3. Grep every project file for old assumptions (`3 herederos`, `mamá enferma`, etc.)
4. Edit each file, replacing old assumptions with new facts
5. Update `tasks/todo.md` with a completed sync entry
6. `git add -A && git commit -m "sync assumptions: HEIR-COUNT, MOM-STATUS, ADDRESS, AMENITIES"`
