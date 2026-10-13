---
name: bilan-seo-conversion
description: Periodic SEO + conversion rate audit for bilan.mx. Use when the user wants to audit the bilan website for search visibility and conversion performance, propose site restructuring, prioritize fixes, or track progress against previous audits. Generates a dated audit report in BLOG/operations/. Assumes bilan-base knowledge is also loaded.
---

# bilan — SEO + Conversion Audit Skill

## When to Use

Load this skill when the task involves:
- Running a periodic SEO audit of bilan.mx
- Analyzing conversion funnel gaps
- Proposing or refining site architecture
- Tracking progress against previous audits
- Prioritizing what to build or fix next on the website
- Preparing a brief for a developer or content writer

**Always load `bilan-base` alongside this skill.**

---

## Audit Philosophy

bilan.mx operates a **content-led DTC funnel**:

```
Google (organic) → Blog post (educate) → Trust page → Product page → Purchase
```

Every audit must evaluate both **search visibility** (can users find us?) and **conversion flow** (do they buy when they arrive?). Improving only SEO without fixing conversion is like filling a leaky bucket.

---

## 📂 Audit Data Sources

Before writing the audit report, read these files in order:

### 1. Site Source of Truth
```
/home/capicuaman/Documents/textDump/01_PROJECTS/BILAN/bilan_source_of_truth.md
```
Check: current product catalog, pricing, distribution channels, personas.

### 2. Previous Audits (compare delta)
```
/home/capicuaman/Documents/textDump/01_PROJECTS/BILAN/BLOG/operations/
```
Read all files matching pattern `*seo*`, `*audit*`, `*analysis*` sorted by date.
The most recent audit before this one sets the **baseline**.

### 3. Blog Operations State
```
/home/capicuaman/Documents/textDump/01_PROJECTS/BILAN/BLOG/operations/README.md
/home/capicuaman/Documents/textDump/01_PROJECTS/BILAN/BLOG/operations/tag-seo-system-guide.md
```

### 4. Blog Content Inventory
```
/home/capicuaman/Documents/textDump/01_PROJECTS/BILAN/BLOG/astro-ready/
/home/capicuaman/Documents/textDump/01_PROJECTS/BILAN/BLOG/drafts/
```
Count published vs. draft posts. Check frontmatter for missing meta descriptions, tags, images.

### 5. Site Architecture Planning
```
/home/capicuaman/Documents/textDump/01_PROJECTS/BILAN/BLOG/strategy/blog_pages.md
/home/capicuaman/Documents/textDump/01_PROJECTS/BILAN/BLOG/strategy/blog_content_strategy_25_posts.md
/home/capicuaman/Documents/textDump/01_PROJECTS/BILAN/BLOG/strategy/seo_keyword_research_all_25_posts.md
```

### 6. Live Site Files (if accessible)
```
/home/capicuaman/Documents/bilan-mx/bilan-mx-astro/src/
```
Check: `astro.config.mjs`, `src/layouts/BaseLayout.astro`, `src/pages/index.astro`,
`src/pages/blog/[slug].astro`, `src/pages/blog/index.astro`, `public/robots.txt`.

### 7. Competitive Intelligence
```
/home/capicuaman/Documents/textDump/01_PROJECTS/BILAN/COMPETITIVEANALYSIS/
```

---

## 🔎 Audit Checklist

Work through each section. For each item, assign a grade: ✅ Good / ⚠️ Needs Work / ❌ Missing.

### Section A — Technical SEO
- [ ] Core Web Vitals: LCP < 2.5s, CLS < 0.1, TTFB < 600ms
- [ ] Mobile-responsive (viewport meta, fluid layout)
- [ ] `lang` attribute set correctly (`es` for Spanish pages)
- [ ] Sitemap enabled and submitted to Search Console
- [ ] `robots.txt` exists and points to sitemap
- [ ] Homepage has `<meta name="description">`
- [ ] Homepage has canonical URL (`<link rel="canonical">`)
- [ ] Homepage has Open Graph tags (og:title, og:description, og:image)
- [ ] Homepage has Twitter Card meta tags
- [ ] Product page has Schema.org `Product` + `Offer` markup
- [ ] Blog posts have `BlogPosting` JSON-LD
- [ ] Organization schema present
- [ ] FAQ schema on FAQ page (if exists)
- [ ] No broken internal links
- [ ] Font loading: no failed font requests
- [ ] Third-party scripts (GTM, Analytics) are async/deferred

### Section B — Content SEO
- [ ] Blog post count: how many published vs. draft
- [ ] Posts published since last audit (velocity metric)
- [ ] Every published post has: title, meta description, image, alt text, 2+ tags
- [ ] Internal links per post: target ≥ 3 contextual + 1 "Related articles" module
- [ ] Tag taxonomy: no duplicate/near-duplicate tags (check for accents, plurals)
- [ ] Thin tag archives (<3 posts): are they `noindex,follow`?
- [ ] Comparison pages exist: `/bilan-vs-suero-oral`, `/bilan-vs-gatorade`
- [ ] Core educational pages exist: `/ingredientes`, `/preguntas-frecuentes`
- [ ] Pillar content clusters mapped (dehydration, electrolytes, use-cases)
- [ ] English blog: how many EN posts live vs. planned?

### Section C — Conversion Funnel
- [ ] Homepage: clear hero value prop above fold
- [ ] Homepage: ≥ 1 social proof element (testimonials, review count, media mention)
- [ ] Homepage: trust badges visible above fold (no sugar, pharma-grade, eco)
- [ ] Homepage: email capture present (popup, inline, or dedicated page)
- [ ] Homepage: ≥ 2 CTAs (primary: buy; secondary: email/learn)
- [ ] Dedicated product page exists at `/producto/bilan-electrolitos` (not just homepage)
- [ ] Product page: problem statement → ingredients → social proof → FAQ → CTA
- [ ] Bundle / subscription offering exists
- [ ] WhatsApp CTA: still live (primary purchase channel)
- [ ] Marketplace support pages: `/ingredientes` links in Mercado Libre/Amazon listings
- [ ] Blog posts: each has a CTA block linking to product or email capture
- [ ] Lead magnet / email sequence exists (e.g., hydration guide, 5-day challenge)
- [ ] B2B / bulk page exists for gym/yoga/corporate buyers

### Section D — Delta from Last Audit
List items that have been resolved since the previous audit.
List items that were flagged before but still open.
Identify any new regressions.

---

## 📊 Grading System

For each of the four sections, calculate a letter grade:

| % Items ✅ | Grade |
|---|---|
| 90–100% | A |
| 75–89% | B |
| 60–74% | C |
| 45–59% | D |
| < 45% | F |

---

## 📝 Audit Report Format

Generate a dated Markdown file at:
```
/home/capicuaman/Documents/textDump/01_PROJECTS/BILAN/BLOG/operations/YYYY-MM-DD_seo-conversion-audit.md
```

Use this structure:

```markdown
# bilan.mx — SEO + Conversion Audit
**Date:** YYYY-MM-DD
**Auditor:** [agent or human name]
**Previous audit:** [link to previous audit file]

## Summary (3 sentences max)
[What's the overall state? Biggest win since last audit? Most urgent problem?]

## 1. Technical SEO Scorecard
[Table: Signal | Status | Grade]

## 2. Content SEO Scorecard
[Table: Signal | Status | Grade]

## 3. Conversion Funnel Scorecard
[Table: Signal | Status | Grade]

## 4. Delta from Last Audit
### ✅ Resolved since [date]
- [item]

### ⚠️ Still Open
- [item]

### 🆕 New Issues
- [item]

## 5. Priority Action Matrix
[P0 (this week) / P1 (this month) / P2 (next month) / P3 (next quarter)]
[Table: Action | Why | Effort | Impact]

## 6. Site Architecture — Gaps
[List missing pages vs. the target architecture]

## 7. KPIs
[Table: Metric | Tool | Last Audit | Current | Target]

## Next audit recommended: YYYY-MM-DD
```

---

## 🗺️ Target Site Architecture Reference

This is the **approved long-term information architecture** for bilan.mx. Use it as the benchmark when auditing missing pages:

```
bilan.mx/
├── /                              → Homepage (conversion-first hero)
├── /producto/bilan-electrolitos   → Main product page (80% of revenue)
├── /paquetes                      → Bundle / subscription page
├── /ingredientes                  → Science/trust page (links from marketplaces)
├── /preguntas-frecuentes          → FAQ page (schema + objection removal)
├── /nosotros                      → About / mission (trust signal)
│
├── /blog/                         → SEO content hub
│   ├── /[slug]
│   └── /tags/[tag]
│
├── /bilan-vs-suero-oral           → Comparison page (buyer intent)
├── /bilan-vs-gatorade             → Comparison page (buyer intent)
├── /mejores-electrolitos-sin-azucar → Decision page
│
├── /para-deportistas              → Persona landing (Active Athlete Alex)
├── /para-bienestar                → Persona landing (Wellness-Seeker Wendy)
├── /mayoreo                       → B2B page (gyms, yoga studios, corporate)
│
└── /reto-5-dias-hidratacion       → Lead magnet funnel (email capture)
```

**Priority order for new page creation:**
1. `/ingredientes` — low effort, high SEO + trust value, needed for marketplace links
2. `/preguntas-frecuentes` — FAQ schema rich snippets, removes last-mile objections
3. `/producto/bilan-electrolitos` — proper product page (separate from homepage)
4. `/bilan-vs-suero-oral` — highest buyer-intent comparison query in Mexico
5. `/reto-5-dias-hidratacion` — email capture, LTV multiplier

---

## 📣 Blog CTA Block Template

Add to the end of every blog post that doesn't already have one:

```markdown
---

## ¿Listo para hidratarte de verdad?

**bilan** tiene exactamente lo que tu cuerpo necesita: sodio, potasio y magnesio —
grado farmacéutico, sin azúcar, sin saborizantes, sin ingredientes de relleno.

[Ver bilan Electrolitos →](/producto/bilan-electrolitos)
```

---

## 🔑 SEO KPIs Tracked Each Cycle

| Metric | Tool | Frequency |
|---|---|---|
| Organic sessions | Google Search Console | Monthly |
| Top 10 keyword positions | Search Console | Monthly |
| Homepage CTR | Search Console | Monthly |
| Core Web Vitals | PageSpeed Insights | Per audit |
| Blog → product click-through | GA4 | Monthly |
| Email capture rate | Email platform | Monthly |
| WhatsApp conversion clicks | GA4 events | Monthly |
| Avg. session depth | GA4 | Monthly |

**Key targets:**
- Organic sessions: +20% quarter-over-quarter
- Homepage CTR: > 3.5%
- Email capture rate: > 2% of all visitors
- Blog → product click-through: > 5%
- LCP: stay under 800ms

---

## 📅 Audit Cadence

| Cadence | Scope |
|---|---|
| **Monthly** | KPI check + new content velocity check |
| **Quarterly** | Full checklist audit → new dated report |
| **Bi-annually** | Site architecture review + major restructuring proposals |

---

## Copy Guardrails (Always Apply)

✅ Allowed language:
- "Apoya la hidratación"
- "Ayuda a reponer electrolitos"  
- "Diseñado para rehidratación"
- "Contribuye al equilibrio electrolítico"

❌ Never use (medical claims):
- "Cura", "Trata", "Previene enfermedades"
- "Mejora condiciones médicas"
- "Clínicamente probado" (without actual trial citation)

---

## Audit History Index

| Date | File | Main Focus | Grade |
|---|---|---|---|
| 2026-02-04 | `bilan-mx-analysis-2026-02-04.md` | Initial technical baseline | B− |
| 2026-06-11 | `2026-06-11_blog-seo-audit-top-5.md` | Blog internal linking + tags | C+ |
| 2026-08-16 | `2026-08-16_seo-conversion-audit.md` | Full funnel + site restructure | D+ (conversion) |
