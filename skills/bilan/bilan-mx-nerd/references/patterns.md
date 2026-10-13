# bilan.mx — Patterns Cheatsheet

bilan.mx is a deployed static webpage, not a CLI. This file replaces `commands.md` with the recurring **inspection, refresh, and audit patterns** you reach for when nerding about the live site.

## Daily-entry patterns

### Refresh the live snapshot
```bash
# From any pi session. Updates raw/bilan_mx.md + graph.
graphify_add https://bilan.mx
```
Confirm with `ls -la /home/capicuaman/Documents/textDump/01_PROJECTS/BILAN/raw/bilan_mx.md`.

### Diff live copy against source of truth
```bash
cd /home/capicuaman/Documents/textDump/01_PROJECTS/BILAN
grep -i "porciones\|sodio\|potasio\|magnesio" raw/bilan_mx.md
grep -i "servings\|porciones\|1000mg\|200mg\|80mg" bilan_source_of_truth.md
```
Look for numeric drift (the 60 vs 66 porciones issue is the canonical example).

### Scan nav + footer links
```bash
grep -iE "home|nosotros|sales|blog|productos|faq|whatsapp|aviso|términos" \
  /home/capicuaman/Documents/textDump/01_PROJECTS/BILAN/raw/bilan_mx.md
```

### Pull live HTML (headers only — nerd who wants cache / server info)
```bash
curl -sI https://bilan.mx | head -20
```

### Pull full live HTML for structural audit (bypass the markdown snapshot)
```bash
curl -s https://bilan.mx -o /tmp/bilan_live.html
grep -oE '<a [^>]*href="[^"]*"' /tmp/bilan_live.html | sort -u | head -30
```

## Config / local sources (priority order)
1. `01_PROJECTS/BILAN/raw/bilan_mx.md` — latest live snapshot.
2. `01_PROJECTS/BILAN/bilan_source_of_truth.{md,json}` — canonical product/brand facts.
3. `01_PROJECTS/BILAN/MARKETING/RAG/faq.json` — deeper FAQ dataset.
4. `01_PROJECTS/BILAN/BLOG/` — blog drafts, outlines, strategy (what the live `/blog` surfaces).
5. `01_PROJECTS/BILAN/BUSINESS/pricingBilan.md` — pricing truth.
6. `01_PROJECTS/BILAN/DEPLOY.md` — the `app.bilan.mx` vs `bilan.mx` split.

## Audit patterns (nerd-grade)

### SEO snapshot via local skill
```text
Hand off to bilan-seo-conversion when the user asks for a full SEO + CRO audit —
it writes a dated report to BLOG/operations/.
```

### Lighthouse-style quick triage
```bash
# If chrome/chromium is on this box (it usually isn't under SSH):
command -v chromium || command -v google-chrome || echo "no headless chrome — use pagespeed.web.dev"
```
If no headless browser, point the user at `https://pagespeed.web.dev/report?url=https://bilan.mx`.

### Spot broken-nav / orphan pages
```bash
# After pulling live HTML:
grep -oE 'href="/[^"]*"' /tmp/bilan_live.html | sort -u
```
Compare against the nav list in `facts.md`. New hrefs = undocumented pages. Missing nav items = drift.

### Verify the Astro build isn't shipping dev noise
```bash
curl -s https://bilan.mx | grep -iE "console\.log|TODO|FIXME|localhost" || echo "clean"
```

## Signature nerd moves

### Move 1: live-vs-SoT reconciliation report
When asked "is anything wrong on bilan.mx?", produce a 3-row table:
`claim · live site value · SoT value · delta`
Start with porciones (60 vs 66), formula (should match), free-shipping threshold.

### Move 2: nav archaeology
When asked about a URL that isn't in the nav, check if it exists via `curl -sI https://bilan.mx/<path>` before guessing it's missing. The nav is small; the site is larger.

### Move 3: WhatsApp funnel trace
The primary CTA is WhatsApp, not a cart. Trace the funnel: hero CTA → WhatsApp link → sales script in `SALES/`. Flag any page that CTAs to a cart instead (inconsistency with primary conversion path).

### Move 4: bilingual completeness check
Default locale is es-MX. There's an `EN` toggle in the footer. When discussing copy changes, always check if the EN version exists and matches semantically.

## Escape hatches

- Live site and `raw/bilan_mx.md` disagree → refresh snapshot (`graphify_add`), then re-answer.
- SoT and live site disagree on a *fact* (number, SKU, formula) → SoT wins, log the drift as a content bug.
- SoT and live site disagree on *copy / tone* → live site is the current reality; propose aligning SoT.
- Routing or component question → stop; hand off to `bilan-webdev` (owns the Astro code).
- Full audit requested → hand off to `bilan-seo-conversion`.

## The authority ladder
1. `curl` / live site at the moment of asking
2. `raw/bilan_mx.md` snapshot (date-stamped)
3. `bilan_source_of_truth.{md,json}`
4. `references/facts.md` in this skill
5. Training-data guesses — **never**.
