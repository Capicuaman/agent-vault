---
name: bilan-blog-ops
description: Blog content operations, creation workflows, and publishing standards for bilan. Use when writing, editing, translating, or publishing blog posts. Covers frontmatter discipline, image handling, bilingual workflows, SEO per-post, and the content pipeline. Assumes bilan-base and bilan-webdev knowledge.
---

# bilan — Blog Operations Skill

## When to Use

Load this skill alongside `bilan-base` and `bilan-webdev` when the task involves:
- Creating, editing, or translating blog posts
- Planning content calendars or editorial workflows
- Optimizing posts for SEO or social sharing
- Managing images, tags, or post metadata
- Publishing drafts or scheduling content
- Troubleshooting why a post isn't appearing

## Content Philosophy

Bilan's blog is an **educational engine**, not a product catalog. Every post should teach something useful about hydration, electrolytes, or wellness — and let the reader conclude that clean electrolytes matter.

**Voice rules:**
- Empowering, not preachy
- Science-backed, not jargon-heavy
- Practical, not abstract
- Transparent about what we don't know

**Bilingual default:** All editorial planning assumes Spanish + English. Monolingual exceptions must be justified.

---

## 📝 The Content Creation Workflow

### Stage 1: Planning

1. **Choose a topic** aligned with the content calendar (see `bilan-marketing`)
2. **Select format:** standard article, guide, myth-buster, science explainer, or comparison
3. **Identify tags** (2–5) from the approved taxonomy
4. **Draft title + description** before writing body copy
5. **Set `translationKey`** (e.g., `electrolitos-ejercicio-2024`) — this links the Spanish and English versions forever

### Stage 2: Writing

1. Create the Spanish post first (source of truth)
2. Save as `src/content/posts/YYYY-MM-DD-slug-descriptivo.md`
3. Fill frontmatter completely (see Frontmatter Standard below)
4. Write in Markdown. Use `##` for sections, `###` for subsections
5. Keep paragraphs short (3–4 lines max on desktop)
6. Add a CTA section linking to bilan products or WhatsApp

### Stage 3: Translation

1. Create `src/content/posts/en/YYYY-MM-DD-slug-descriptivo.md`
2. Copy the Spanish frontmatter as a template
3. Translate `title`, `description`, `author`, `imageAlt`
4. **Keep identical:** `pubDate`, `translationKey`, `tags`, `image`, `draft`, `featured`
5. Translate body content. Adapt cultural references (e.g., Mexican heat → "hot climates")
6. Verify `lang: 'en'` is set

### Stage 4: Review

- [ ] Frontmatter validates (run `npm run dev` — Astro will error if invalid)
- [ ] Title is 50–60 characters
- [ ] Description is 150–160 characters
- [ ] Image exists in `public/blog-images/` and is <500KB
- [ ] Alt text describes the image, not just repeats the title
- [ ] Tags are lowercase, no accents, from approved list
- [ ] Links work (especially internal `/blog/` links)
- [ ] WhatsApp CTA URL is correct per `utils/whatsapp.ts`

### Stage 5: Publishing

1. Set `draft: false` on both language versions
2. Commit with descriptive message: `feat(blog): add electrolyte exercise guide [es+en]`
3. Push, build (`npm run build`), deploy `dist/`
4. Verify on production: check post URL, OG image, structured data, mobile layout

---

## 📋 Frontmatter Standard

Every post must begin with this YAML block between `---` delimiters:

```yaml
---
title: "Exact post title — max 60 chars"
description: "One or two sentences summarizing the post. 150–160 chars."
pubDate: 2026-07-14
author: "Equipo bilan MX"
lang: es
translationKey: "unique-topic-slug"  # Same across ES/EN versions
tags: ["hidratacion", "electrolitos", "deporte"]
image: "/blog-images/my-image.jpg"
imageAlt: "Descriptive alt text for accessibility and SEO"
draft: false
featured: false
---
```

### Field Reference

| Field | Required | Rules |
|-------|----------|-------|
| `title` | ✅ | 50–60 chars. Front-loaded keywords. No clickbait. |
| `description` | ✅ | 150–160 chars. Appears in Google results and social cards. |
| `pubDate` | ✅ | `YYYY-MM-DD`. Future dates hide the post until then. |
| `author` | ❌ | Default: "Equipo bilan MX". Use real names for guest posts. |
| `lang` | ❌ | Default: `es`. Must be `en` for English posts. |
| `translationKey` | ✅ | Unique string. Links ES↔EN versions. Never change after publishing. |
| `tags` | ❌ | Array of 2–5 strings. Lowercase, no spaces, no accents. From approved taxonomy. |
| `image` | ❌ | Path starting with `/blog-images/`. Image must exist in `public/blog-images/`. |
| `imageAlt` | ❌ | Required if `image` is set. Describe what's visible, not just "post image". |
| `draft` | ❌ | `true` = hidden from lists and RSS. `false` = published. |
| `featured` | ❌ | `true` = promoted in featured sections (max 3–4 active at once). |
| `theme_id` | ❌ | Future pipeline field. Campaign/theme grouping. |
| `atoms` | ❌ | Future pipeline field. Atomic content blocks for reuse. |

### Frontmatter Examples

**Standard article:**
```yaml
---
title: "Sodio y rendimiento: lo que dice la ciencia"
description: "Descubre cómo el sodio afecta tu rendimiento atlético y por qué la hidratación con electrolitos importa más que solo agua."
pubDate: 2026-05-12
author: "Equipo bilan MX"
lang: es
translationKey: "sodio-rendimiento-ciencia"
tags: ["sodio", "rendimiento", "ciencia", "deporte"]
image: "/blog-images/sodio-rendimiento.jpg"
imageAlt: "Atleta sudando durante entrenamiento intensivo al aire libre"
draft: false
featured: false
---
```

**Featured guide:**
```yaml
---
title: "Guía completa de hidratación para ciclistas"
description: "Todo lo que necesitas saber sobre hidratación en ciclismo: sodio, carbohidratos, agua y electrolitos."
pubDate: 2026-04-20
author: "Dr. Carlos Méndez"
lang: es
translationKey: "guia-hidratacion-ciclismo"
tags: ["ciclismo", "hidratacion", "electrolitos", "guia"]
image: "/blog-images/ciclismo-hidratacion.jpg"
imageAlt: "Ciclista de ruta bebiendo de bidón en montaña"
draft: false
featured: true
---
```

---

## 🏷️ Tag Taxonomy Rules

### Approved Tags

Use these existing tags whenever possible. Adding new tags requires updating `blogSeo.ts` with a label and metadata.

**Core topics:**
- `hidratacion`, `electrolitos`, `sodio`, `potasio`, `magnesio`, `agua`
- `salud`, `bienestar`, `nutricion`, `recuperacion`, `energia`
- `deporte`, `rendimiento`, `resistencia`, `entrenamiento`
- `ciclismo`, `running`, `natacion`, `triatlon`, `gym`
- `ciencia`, `mitos`, `seguridad`
- `cerebro`, `cognicion`, `neurologia`, `migranas`
- `intestino`, `microbiota`, `salud-digestiva`
- `cafe`, `cafeina`, `keto`
- `calor`, `verano`, `oficina`, `vida-cotidiana`, `productividad`
- `absorcion`, `deshidratacion`

### Tag Format Rules

- ✅ `hidratacion` (lowercase, no accents where possible)
- ✅ `salud-digestiva` (kebab-case for compound terms)
- ❌ `Hidratación` (no caps)
- ❌ `salud digestiva` (no spaces)
- ❌ `hidratacion-verano-2024` (no dates in tags)

### When to Add a New Tag

1. The topic is distinct and will have ≥3 posts in the next 6 months
2. Add to `BLOG_TAG_LABELS` with a display name
3. Add to `BLOG_TAG_METADATA` with SEO title, description, intro, and 3 highlights
4. If <3 posts exist, use the tag but the archive page will be `noindex` until threshold is met

---

## 🖼️ Image Pipeline

### Image Requirements

| Property | Standard |
|----------|----------|
| **Format** | JPG for photos, PNG for graphics with transparency, WebP when supported |
| **Featured size** | 1200×675px (16:9) |
| **Inline size** | Max 1200px width |
| **File size** | <500KB (compress with TinyPNG or Squoosh) |
| **Naming** | Descriptive, lowercase, kebab-case, no spaces |

### Image Workflow

1. Optimize the source image
2. Save to `public/blog-images/nombre-descriptivo.jpg`
3. Reference in frontmatter: `image: "/blog-images/nombre-descriptivo.jpg"`
4. Reference inline: `![Alt text](/blog-images/nombre-descriptivo.jpg)`
5. Always provide `imageAlt` in frontmatter and alt text in Markdown

**Alt text rules:**
- Describe what is literally visible in the image
- Include context if relevant: "Runner drinking from water bottle at 10k race"
- Never: "Image", "Photo", "Figure 1", or just repeating the post title

---

## 🔄 Translation Workflow Details

### File Naming Convention

| Language | Path | Example |
|----------|------|---------|
| Spanish | `src/content/posts/YYYY-MM-DD-slug.md` | `2026-05-12-sodio-rendimiento-atletico.md` |
| English | `src/content/posts/en/YYYY-MM-DD-slug.md` | `2026-05-12-sodium-athletic-performance.md` |

### Translation Checklist

- [ ] `translationKey` is identical in both files
- [ ] `pubDate` is identical (or intentionally offset with note)
- [ ] `tags` are identical (the tag taxonomy is language-agnostic)
- [ ] `image` path is identical (images are shared, not duplicated)
- [ ] `imageAlt` is translated
- [ ] `lang` is correct (`es` vs `en`)
- [ ] Slug can differ (Spanish SEO vs English SEO), but keep date prefix consistent
- [ ] Body CTAs are localized (WhatsApp message, currency, cultural references)

### Translation Pitfalls

- **Don't** translate `translationKey` — it's the database primary key
- **Don't** translate tag strings — tags are URLs: `/blog/tags/hidratacion` works for both languages
- **Don't** duplicate images into `public/blog-images/en/` — use the same asset
- **Do** adapt examples: "Mexico City heat" → "tropical climates" or "hot weather training"

---

## ✍️ Markdown & MDX Guidelines

### Use `.md` (Markdown) when:
- Standard article with text, headings, lists, images, links
- No interactive elements needed
- Fastest build, simplest editing

### Use `.mdx` (MDX) when:
- Embedding interactive components (calculators, product cards, toggles)
- Reusing React/Vue/Svelte components inside prose
- Need dynamic imports or JavaScript expressions

**MDX example:**
```mdx
---
title: "Calculadora de electrolitos"
---

## ¿Cuánto necesitas?

import ElectrolyteCalculator from '../../components/ElectrolyteCalculator.astro';

<ElectrolyteCalculator />
```

### Markdown Formatting Standards

```markdown
## Sección principal (usa ##, no #)

Párrafo corto. Máximo 3-4 líneas en pantalla.

### Subsección (usa ###)

**Negrita** para conceptos clave.

- Lista con viñetas para items relacionados
- Máximo 5-7 items por lista

1. Lista numerada para pasos secuenciales
2. Paso dos

> Cita destacada para insights o datos sorprendentes

[Enlace interno](/blog/otro-articulo) para SEO de sitio
```

### Prohibited in Posts

- `<h1>` (`#` in Markdown) — reserved for page title from frontmatter
- Raw HTML unless necessary (breaks static rendering assumptions)
- External images (hotlinking) — always use `public/blog-images/`
- Tables wider than 3 columns (break mobile layout)

---

## 🚀 Publishing Checklist

### Pre-commit

- [ ] `npm run dev` starts without errors
- [ ] Post appears at `http://localhost:4321/blog/slug-del-post/`
- [ ] Mobile preview looks correct (narrow browser window)
- [ ] Image loads and `imageAlt` appears on hover/inspector
- [ ] Tags link to correct tag pages
- [ ] Related posts section appears (if tags match other posts)
- [ ] Newsletter signup renders
- [ ] WhatsApp CTA links correctly with UTM params
- [ ] `draft: false` on both language versions
- [ ] Spanish version `featured` matches English version

### Post-deploy

- [ ] Production URL loads: `https://bilan.mx/blog/slug-del-post/`
- [ ] OG image appears in [MetaTags.io](https://metatags.io/) preview
- [ ] Structured data validates in [Google Rich Results Test](https://search.google.com/test/rich-results)
- [ ] RSS feed includes the new post: `/rss.xml`
- [ ] Tag page shows the post and count is correct
- [ ] No 404s in Google Search Console within 48 hours

---

## 🐛 Troubleshooting

### Post doesn't appear in blog list

| Symptom | Cause | Fix |
|---------|-------|-----|
| `draft: true` | Post is intentionally hidden | Set to `false` |
| Future `pubDate` | Astro hides future-dated posts | Use today's date or past date |
| Build error in console | Invalid frontmatter | Check YAML syntax, quotes, indentation |
| File in wrong folder | Must be in `src/content/posts/` | Move file |
| No `title`/`description`/`pubDate` | Missing required fields | Add to frontmatter |
| `.mdx` without closing tags | JSX syntax error | Validate all tags close properly |

### Image doesn't load

```bash
# Verify image exists
ls public/blog-images/nombre-imagen.jpg

# Verify path starts with /
image: "/blog-images/nombre-imagen.jpg"   # ✅
image: "blog-images/nombre-imagen.jpg"    # ❌ missing /
image: "/images/nombre-imagen.jpg"        # ❌ wrong folder
```

### Translation not linked

```bash
# Find posts by translationKey
grep -r "mi-translation-key" src/content/posts/
# Should show 2 files: one in posts/, one in posts/en/
```

### Tag page returns 404

Tag pages are generated at build time from all published posts. If you add a new tag to an existing post, you must rebuild for the new tag route to exist.

---

## 📊 Content Pipeline (Future)

The schema includes two forward-looking fields for a future content system:

- `theme_id`: Groups posts by campaign or theme (e.g., `verano-2026`, `science-series-3`)
- `atoms`: Array of atomic content block IDs for remixing content across channels

**For now**, these are optional and unused. When the marketing team wants to run a themed campaign, populate `theme_id` consistently across related posts. Later, this will enable automatic landing page generation and cross-channel content reuse.

---

## 📚 References

| File | Purpose |
|------|---------|
| `BLOG_USER_MANUAL.md` | Human-readable guide for non-technical writers |
| `BLOG_QUICK_REFERENCE.md` | One-page cheat sheet |
| `src/content/config.ts` | Zod schema — the technical contract |
| `src/utils/blogSeo.ts` | Tag taxonomy and SEO metadata |
| `src/utils/blogTranslations.ts` | Bilingual resolution logic |
| `src/utils/blogFeatureFlags.ts` | Progressive rollout controls |
| `src/pages/rss.xml.js` | RSS feed generation |
