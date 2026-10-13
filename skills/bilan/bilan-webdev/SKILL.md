---
name: bilan-webdev
description: Core web development architecture and progressive enhancement guide for the bilan Astro site. Use when modifying code, adding features, debugging, refactoring, or learning how the site works. Teaches Astro concepts, content collections, i18n patterns, feature flags, and the enhancement roadmap.
---

# bilan — Web Development & Architecture Skill

## When to Use

Load this skill alongside `bilan-base` when the task involves:
- Adding or modifying site features, pages, or components
- Debugging build errors, routing issues, or SEO problems
- Refactoring code or upgrading dependencies
- Understanding *why* a pattern was chosen and *how* to evolve it
- Planning progressive enhancements (new features, performance improvements, UX upgrades)
- Teaching or explaining web development concepts to the team

## Project Overview

**bilan.mx** is a statically-generated site built with **Astro** (v4+). It lives in `bilan-mx-astro/`.

| Technology | Purpose | Why It Was Chosen |
|------------|---------|-------------------|
| **Astro** | Static site generator | Zero JS by default; ships only the JS you explicitly add. Perfect for a content-heavy site where speed and SEO matter. |
| **Content Collections** | Blog + page schema | Zod-validated frontmatter. Type-safe content. No CMS needed. |
| **Bootstrap 5** | CSS framework | Already in use pre-Astro migration. Provides responsive grid and components without custom CSS overhead. |
| **Snipcart** | E-commerce cart | Drop-in checkout. Works with static sites. |
| **Google Apps Script** | Newsletter backend | Serverless form capture. No backend infrastructure needed. |

**Key architectural principle:** *Progressive enhancement via feature flags.* The site is built with "hidden-ready" bilingual hooks and optional features that can be enabled one at a time without breaking existing behavior.

---

## 🏗️ How Astro Works Here (The Concepts)

### Islands Architecture

Astro's core innovation is **partial hydration**. Think of your page as an ocean of static HTML with occasional "islands" of interactivity.

- **Static HTML (the ocean):** Blog post content, navigation, SEO meta tags, layout — all rendered to HTML at build time. The browser receives pure HTML. No React runtime loads. This is why the blog loads instantly.
- **Islands (interactive bits):** Newsletter signup form, language switcher, WhatsApp CTAs — these need JavaScript. Astro only hydrates these specific components.

**Teaching analogy:** Imagine a newspaper (static HTML) with one sticky note that has a button on it (the island). You don't need to print the button factory — just the button.

**In this codebase:**
- `BaseLayout.astro` — pure static HTML shell (no islands)
- `NewsletterSignup.astro` — an island (needs JS to POST to Google Apps Script)
- `LanguageSwitcher.astro` — an island (needs JS to navigate)
- `Header.astro` — mostly static, but includes a small script for mobile menu collapse

### Content Collections (Your Headless CMS, But Better)

Astro Content Collections replace a traditional CMS. Here's how they work:

1. **Schema definition** (`src/content/config.ts`): You write a Zod schema that describes what every blog post *must* have.
2. **Validation at build time**: If a post is missing `title` or has a malformed `pubDate`, the build fails immediately with a clear error.
3. **Type safety**: When you query posts with `getCollection('posts')`, TypeScript knows every field available.

```typescript
// src/content/config.ts — the contract
const postsCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string().min(1, 'Title is required'),
    description: z.string().min(1, 'Description is required'),
    pubDate: z.coerce.date(),
    author: z.string().default('Equipo bilan MX'),
    lang: z.enum(['es', 'en']).default('es'),
    translationKey: z.string().min(1, 'translationKey is required'),
    tags: z.array(z.string()).default([]),
    image: z.string().optional(),
    imageAlt: z.string().optional(),
    draft: z.boolean().default(false),
    featured: z.boolean().default(false),
    theme_id: z.string().optional(),      // Future content pipeline
    atoms: z.array(z.string()).optional(), // Future atomic content
  }),
});
```

**Why Zod?** It's a "schema validator." Think of it as a bouncer at a club. The bouncer checks every post's ID against the guest list (the schema). If the post is missing required info, it doesn't get in (build fails). This prevents broken pages from ever deploying.

### Static Site Generation (SSG) vs Server-Side Rendering (SSR)

This site uses **SSG**. At build time (`npm run build`), Astro:
1. Reads all Markdown/MDX files
2. Validates frontmatter against Zod schemas
3. Renders each page to a static `.html` file
4. Outputs everything to `dist/`

**Why SSG for bilan?**
- Blog content doesn't change per visitor (no personalization needed)
- CDN can cache every page forever
- No server to maintain, no cold starts, no database connection issues
- Maximum SEO (crawlers see complete HTML immediately)

**Trade-off:** To publish a new post, you must rebuild and redeploy. This is why the Git workflow matters.

---

## 📁 Project Structure Map

```
bilan-mx-astro/
├── src/
│   ├── components/          # Reusable Astro components (islands + static)
│   │   ├── Header.astro
│   │   ├── NewsletterSignup.astro      # Island — handles form POST
│   │   ├── NewsletterModal.astro         # Island — modal UI + timing
│   │   ├── LanguageSwitcher.astro      # Island — bilingual navigation
│   │   └── InlineWhatsappCta.astro
│   ├── content/
│   │   ├── config.ts        # Zod schemas — THE CONTRACT
│   │   ├── posts/           # Blog posts (es/ + en/ subdirs)
│   │   └── pages/           # Static pages (future)
│   ├── data/
│   │   └── bilan.ts         # Product data, pricing, SKUs
│   ├── layouts/
│   │   └── BaseLayout.astro # HTML shell, SEO meta, fonts, analytics
│   ├── pages/               # File-based routing
│   │   ├── index.astro      # Homepage
│   │   ├── rss.xml.js       # RSS feed (dynamic route)
│   │   └── blog/
│   │       ├── index.astro              # Blog listing (es)
│   │       ├── [...slug].astro          # Blog post template
│   │       ├── tags/[tag].astro         # Tag archive pages
│   │       └── en/index.astro           # Blog listing (en)
│   ├── styles/              # CSS (Bootstrap + custom)
│   └── utils/               # TypeScript helpers
│       ├── blogFeatureFlags.ts          # Progressive enhancement switches
│       ├── blogSeo.ts                   # Tag labels, metadata, related posts
│       ├── blogTranslations.ts          # Bilingual post resolution
│       ├── i18n.ts                      # UI string translations
│       ├── newsletter.ts              # Newsletter API client
│       └── whatsapp.ts                  # WhatsApp URL builder + UTM tracking
├── public/                  # Static assets (images, fonts, favicon)
│   └── blog-images/
└── dist/                    # Build output (deploy this)
```

**Routing rule:** Every file in `src/pages/` becomes a URL path. `src/pages/blog/index.astro` → `bilan.mx/blog/`. `src/pages/blog/[...slug].astro` → `bilan.mx/blog/any-post-slug/`.

---

## 🌐 Bilingual Architecture (es/en)

### How It Works

The site is designed to be fully bilingual, but features are rolled out progressively via flags.

**Content-level i18n:**
- Posts live in parallel: `posts/YYYY-MM-slug.md` (Spanish) and `posts/en/YYYY-MM-slug.md` (English)
- Both share the same `translationKey` in frontmatter. This is the "glue" that links them.
- `blogTranslations.ts` resolves counterparts: `getTranslatedPost(post)` finds the English version of a Spanish post.

**UI-level i18n:**
- `i18n.ts` holds a dictionary of UI strings (`blog.title`, `newsletter.button`, etc.)
- Components call `t('key', lang)` to get the correct translation.

**URL strategy (future-ready):**
- Currently: `/blog/` (Spanish), `/blog/en/` (English index), `/blog/slug` (individual posts detect lang from frontmatter)
- Future option: `/es/blog/` and `/en/blog/` with `getLocalizedPath()`
- Feature flag `enableLanguageSwitch` controls whether the language toggle UI appears.

### The Translation Workflow

1. Write the Spanish post first (source of truth)
2. Create the English version with the **same** `translationKey`
3. Ensure `lang: 'en'` and matching `pubDate` (or intentional offset)
4. The `LanguageSwitcher` component will automatically link them when `enableLanguageSwitch` is true.

---

## 🚦 Feature Flags (Progressive Enhancement Control)

All experimental or future features are gated by `blogFeatureFlags.ts`:

```typescript
export const blogFeatureFlags = {
  enableLanguageSwitch: true,          // Bilingual toggle UI
  enableLanguageFilteredIndex: true,   // Show only Spanish on /blog/
  enableLanguageSpecificTagPages: false, // /en/blog/tags/hidratacion ?
  enableLanguageSpecificRss: false,    // Separate RSS feeds per lang
} as const;
```

**Pattern:** Every flag has matching "hidden-ready" code in the templates (commented or conditional). When a flag is flipped, the feature appears without code changes elsewhere.

**How to add a new flag:**
1. Add the boolean to `blogFeatureFlags.ts`
2. Wrap the new UI/feature in a conditional check
3. Keep the code visible (not deleted) so it's easy to enable later
4. Default to `false` until fully tested

---

## 🔍 SEO Utilities (`blogSeo.ts`)

### Tag Taxonomy System

Tags are not free-form. They have:
- **Labels:** Human-readable display names (`hidratacion` → `Hidratación`)
- **Metadata:** SEO titles, descriptions, and content highlights for tag archive pages
- **Indexing rules:** Tag pages only get `index,follow` when they have ≥3 posts (`BLOG_TAG_INDEX_MIN_POSTS`)

This prevents Google from indexing thin tag pages with 1 post, which can hurt SEO.

### Related Posts Algorithm

`getRelatedPosts()` uses a scoring system:
- +10 points per shared tag
- +1 bonus if the *first* tag matches (primary topic match)
- Sorted by score, then by date
- Returns top 3

**Why this matters:** Internal linking between related posts increases "time on site" and helps Google understand topical clusters.

### Structured Data (JSON-LD)

Every blog post injects `BlogPosting` schema into the `<head>`. This tells Google:
- Title, description, author, publish date
- Language
- Featured image

`BaseLayout.astro` also conditionally injects `Product` schema for the e-commerce SKUs when `includeDefaultProductSchema=true`.

---

## 🎨 Styling Architecture

### Current Stack

| File | Purpose |
|------|---------|
| `bootstrap.min.css` | Grid system, utility classes, components (Navbar, buttons, cards) |
| `style.css` | Bilan brand overrides, custom components, spacing |
| `ofo.css` | Additional custom styles (legacy name, likely "one file only") |

### Why Bootstrap?

The site predates the Astro migration and Bootstrap was already in use. Rather than rebuilding all UI from scratch, the migration kept Bootstrap for layout primitives and rebuilt the blog in Astro.

**How to progressively evolve styling:**
- New components should prefer **scoped `<style>` blocks** inside `.astro` files (see `blog/index.astro` and `[...slug].astro` for examples)
- Scoped styles only apply to that component's HTML — no global CSS pollution
- When a full redesign happens, Bootstrap can be removed page by page

**Scoped style example from the codebase:**
```astro
<style>
  .blog-card:hover {
    transform: translateY(-4px);
  }
  /* Only applies to elements in THIS component's template */
</style>
```

---

## 🛠️ Progressive Enhancement Roadmap

### Currently Active
- ✅ Content Collections with Zod validation
- ✅ Bilingual content (es/en)
- ✅ Tag system with SEO metadata
- ✅ Related posts
- ✅ Newsletter signup (Google Apps Script)
- ✅ WhatsApp CTAs with UTM tracking
- ✅ RSS feed
- ✅ Structured data / JSON-LD
- ✅ Feature flag system
- ✅ GA4 analytics

### Behind Flags (Ready to Enable)
- 🚦 Full language switcher UI (`enableLanguageSwitch`)
- 🚦 Language-filtered blog index (`enableLanguageFilteredIndex`)

### Suggested Next Enhancements

| Priority | Feature | Complexity | Concept to Learn |
|----------|---------|------------|-----------------|
| High | **Search** | Medium | Fuse.js or Pagefind for static search index |
| High | **Table of Contents** | Low | Auto-generate from `post.headings` via `render()` |
| Medium | **Reading time** | Low | Word count ÷ 200 WPM |
| Medium | **OpenGraph image generation** | Medium | `@vercel/og` or Satori for dynamic social cards |
| Medium | **Pagination** | Low | Slice post arrays, add `/blog/2/` routes |
| Medium | **Author pages** | Low | New collection or filter by `author` field |
| Low | **Comments** | Medium | Giscus (GitHub Discussions) or Cusdis |
| Low | **View counter** | High | PlanetScale/Upstash Redis (needs edge function) |

**Teaching note:** For a static site, "dynamic" features usually mean:
- **Build-time dynamic:** Generated at `npm run build` (related posts, tag pages, RSS). Fast, but updates only on deploy.
- **Client-side dynamic:** Runs in browser after page loads (search, comments). Requires JS.
- **Edge dynamic:** Requires a serverless function (view counters, forms with complex logic). Adds infrastructure.

Prefer build-time > client-side > edge, in that order, for a content blog.

---

## 🔧 Common Technical Tasks

### Add a New Page

1. Create `src/pages/nueva-pagina.astro`
2. Import `BaseLayout` and set `title`, `description`, `lang`
3. Write HTML + scoped styles
4. `npm run dev` to preview at `http://localhost:4321/nueva-pagina`

### Add a New Component

1. Create `src/components/MiComponente.astro`
2. Use `---` frontmatter for logic, HTML template below
3. If it needs client-side JS, add `<script>` or a `client:*` directive
4. Import and use in pages or other components

### Modify the Content Schema

1. Edit `src/content/config.ts`
2. Add/modify Zod fields
3. Run `npm run dev` — Astro will tell you which posts violate the new schema
4. Fix those posts before committing

### Add a New Tag with SEO Metadata

1. Add the tag to `BLOG_TAG_LABELS` in `blogSeo.ts`
2. Add full metadata to `BLOG_TAG_METADATA` (only if the tag will have ≥3 posts)
3. Use the tag in post frontmatter

---

## 🧪 Development Workflow

```bash
# Start dev server with hot reload
cd bilan-mx-astro
npm run dev
# → http://localhost:4321

# Build for production
npm run build
# → Output in dist/

# Preview production build locally
npm run preview

# Clean cache when things get weird
rm -rf .astro dist node_modules
npm install
npm run dev
```

---

## 🚀 Deployment

**The site auto-deploys to production on every commit to `main`.**

A GitHub Actions workflow triggers on push to `main`, runs `npm run build`, and deploys the `dist/` output to the production host (bilan.mx). This means:

- **No manual deployment needed** — `git push origin main` is the deploy button
- **Build must pass** before deployment succeeds; if the build fails, the site stays at the last successful commit
- **Always commit before asking "is this live?"** — the answer is "it will be once the GitHub Action finishes"
- `dist/` is the deployable artifact; previewing via `npm run preview` or here.now is useful for QA but production only updates from `main` branch commits

**When the user asks about production status**, remind them: commit + push to `main` triggers the auto-deploy. If they want to preview first, use `npm run build` + here.now or `npm run preview`, but production is strictly via GitHub Actions.

---

## 📚 Key File References

| File | Role |
|------|------|
| `src/content/config.ts` | Zod schema — the content contract |
| `src/utils/blogFeatureFlags.ts` | Progressive enhancement switches |
| `src/utils/blogSeo.ts` | Tag taxonomy, related posts, indexing rules |
| `src/utils/blogTranslations.ts` | Bilingual post resolution |
| `src/utils/i18n.ts` | UI string dictionary |
| `src/layouts/BaseLayout.astro` | HTML shell, meta tags, analytics, fonts |
| `src/pages/blog/[...slug].astro` | Blog post template (most complex page) |

---

## 🔗 Related Skills

| Skill | Load When |
|-------|-----------|
| `bilan-base` | Every task — brand knowledge |
| `bilan-design` | Styling, layout, CSS changes, visual improvements, Tailwind migration |
| `bilan-blog-ops` | Content creation, frontmatter, publishing |
| `bilan-marketing` | Landing page copy, campaigns, social |
| `bilan-sales` | Pricing, checkout, CRM integrations |

---

## 🧠 Teaching Quick Reference

**Q: Why Astro instead of Next.js?**
A: Next.js ships React runtime to every visitor. For a blog, that's unnecessary weight. Astro sends zero JS by default and only hydrates interactive islands. The blog loads faster, scores higher on Core Web Vitals, and uses less bandwidth.

**Q: What's the difference between `.md` and `.mdx`?**
A: Markdown (`.md`) = text + images only. MDX (`.mdx`) = Markdown + JSX components. Use `.mdx` when you need to embed interactive charts, custom callout boxes, or product cards inside a blog post. Use `.md` for standard articles.

**Q: What is `getStaticPaths()`?**
A: It's Astro's way of saying "generate one page per item in this list." In `[...slug].astro`, it takes every published post and tells Astro: "Build a page at `/blog/post-slug/` for each one." At build time, all these pages become static HTML files.

**Q: Why feature flags instead of branches?**
A: Branches hide code. Feature flags keep code visible and testable, but invisible to users. You can merge partial features safely and enable them when ready — no merge conflicts, no forgotten branches.
