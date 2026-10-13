# Propagation Guide

Detailed playbook for applying assumption changes across a project without breaking files.

## Pre-flight checklist

Before touching any file:

1. **Commit baseline** — `git add -A && git commit -m "baseline before assumption sync"`
2. **Export assumption grid** from the HTML intake form → save as JSON
3. **Sort by impact** — tackle `critical` before `important` before `cosmetic`
4. **Grep before edit** — never assume you know where a phrase lives

## Grep patterns

Find every occurrence of an old assumption:

```bash
grep -rn -i "3 herederos\|3 hermanos" --include="*.html" --include="*.md" .
grep -rn -i "mamá.*enferma\|mamá.*enferm" --include="*.html" --include="*.md" .
```

Use `-n` for line numbers. Use `-C 2` for context. Use `--include` to filter file types.

## Edit safety rules

### Rule 1: Exact match
The `oldText` field must match the file **byte-for-byte**, including spaces, newlines, and indentation. If uncertain, `read` the file first.

### Rule 2: Non-overlapping
If two edits touch nearby lines, merge them into one edit object. Never emit two edits whose `oldText` regions overlap.

### Rule 3: Verify after each file
After editing a file, `read` it to confirm the change took. If the file is large, `grep` the changed phrase.

### Rule 4: Batch within file, not across files
Use one `edit` call per file. Put multiple `edits[]` entries in that call for disjoint regions within the same file.

### Rule 5: HTML special cases
HTML files often have assumptions in:
- **Visible text** — easiest, plain text replacement
- **`<title>` tags** — update for SEO/context
- **Default `<input>` values** — change `value="15000000"` if price assumption changed
- **`<option selected>`** — change default dropdown state
- **JavaScript constants** — update `const UDI = 8.55` if needed
- **Matrix/table dimensions** — if heir count changes from 3→4, you may need to add rows/columns and update grid CSS (`grid-template-columns`)
- **Dynamic text in JS strings** — grep for template literals that include old assumptions

## Impact-specific tactics

### Critical (legal / financial)
- Legal docs: change heir counts, voting thresholds, majority rules
- Tax strategies: update exemption counts, depreciation assumptions
- Contracts: update party lists, address fields, ID requirements
- **Double-check** every number that derives from the assumption (e.g., 2/3 majority → 3/4)

### Important (user confusion)
- Pitch documents: update heir counts, family structure, urgency tone
- Meeting prep: replace "mom is sick" framing with neutral or accurate framing
- Calculators: update default participants, risk labels
- **Preserve strategic advice** — even if mom is healthy, the advice "don't reveal family health status to brokers" stays valid

### Cosmetic (nice to fix)
- README links and descriptions
- Index page card text
- Footer "last updated" dates
- **Skip if time-constrained** — but log for later

## Common pitfalls

### Pitfall: "3 hermanos" appears in both text and code
A phrase like `"3 hermanos"` may appear in:
- User-facing paragraph text
- JavaScript string literals
- Markdown table cells
- HTML `title` attributes

**Fix:** grep for each variant separately, or use a broad grep and inspect every match.

### Pitfall: Overlapping edits in the same block
If you try to replace `Los 3 hermanos` and later in the same paragraph replace `entre los 3`, the second edit may fail because the first changed the surrounding text.

**Fix:** Merge into one edit that replaces the entire paragraph or list item.

### Pitfall: HTML entities vs raw text
`&amp;` in HTML source is `&` in rendered text. Edit the source, not the rendered view.

### Pitfall: JS variable math tied to old numbers
If a calculator divides by 3 for expense splits, changing "3 hermanos" in text without changing `/ 3` in JS creates a silent bug.

**Fix:** grep for both the text and the arithmetic: `grep -n "/ 3\|* 3\|3 *" file.html`

### Pitfall: Matrix visualization grids
A decision matrix with 3 columns for heirs needs a 4th column if heir count changes. This often requires:
- Adding a new `<div class="col-hd">` header
- Adding a new `<div class="cell">` data cell per row
- Updating CSS `grid-template-columns`
- Updating JS logic that colors or labels cells

**Fix:** treat matrix HTML as a mini sub-project. Read the entire matrix section before editing.

## After propagation

1. **Update the assumption tracker** — mark each row `synced`
2. **Re-export** the intake form JSON/Markdown
3. **Append to tasks/todo.md**:
   ```markdown
   - [x] YYYY-MM-DD — Assumption sync: `HEIR-COUNT, MOM-STATUS` applied across 12 files. Commit: `abc1234`.
   ```
4. **Final commit**:
   ```bash
   git add -A && git commit -m "sync assumptions: HEIR-COUNT, MOM-STATUS, ADDRESS, AMENITIES"
   ```

## Rollback

If propagation goes wrong:

```bash
git reset --hard HEAD~1   # rollback to baseline commit
git log --oneline -3      # verify
```

Then fix the assumption grid and re-run.
