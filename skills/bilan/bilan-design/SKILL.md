---
name: bilan-design
description: Design system, CSS architecture, and visual consistency for bilan. Use when styling components, modifying layouts, migrating from Bootstrap, or establishing design tokens. Covers Tailwind CSS integration, scoped Astro styles, token systems, and responsive patterns. Assumes bilan-base and bilan-webdev knowledge.
---

# bilan — Design System & CSS Architecture Skill

## When to Use

Load this skill alongside `bilan-base` and `bilan-webdev` when the task involves:
- Styling or modifying any component, page, or layout
- Changing colors, fonts, spacing, or responsive behavior
- Adding new UI sections (landing page, blog cards, CTAs)
- Migrating away from Bootstrap or reducing CSS bloat
- Creating reusable component patterns
- Debugging visual regressions or layout issues

## Current State Diagnosis

Your site carries **CSS technical debt** from the pre-Astro era:

| File | Size | Role | Problem |
|------|------|------|---------|
| `bootstrap.min.css` | **164 KB** (6 lines minified) | Grid + buttons + utilities | You use ~10 classes (container, col, row, btn) but ship 164KB |
| `style.css` | **2,785 lines** | Custom brand styles | Battles Bootstrap specificity, has unused rules, monolithic |
| `ofo.css` | **13 lines** | Legacy overrides | `.special-text` font override + dead `.banner-section` rules |
| Inline `style="..."` | **9+ per page** | Quick fixes | Unmaintainable, scattered, breaks component reuse |

**The cost:** Every visitor downloads ~164KB of unused Bootstrap + 2,785 lines of potentially conflicting custom CSS. On mobile, that's render-blocking weight.

**The root cause:** You migrated the site to Astro but kept the pre-Astro CSS stack. The blog is modern (Content Collections, Astro components), but the landing page still depends on Bootstrap's grid system and utility classes.

---

## 🎯 Target Architecture: The Pro Setup

### Philosophy

**"One token source, scoped components, utility helpers, zero bloat."**

```
Design Tokens (CSS custom properties)
    ↓
Base Styles (minimal resets + font loading)
    ↓
Layout (grid + spacing — Tailwind or CSS Grid)
    ↓
Components (scoped Astro <style> blocks)
    ↓
Utilities (Tailwind for one-offs)
```

### The Stack

| Layer | Tool | Purpose |
|-------|------|---------|
| **Tokens** | CSS Custom Properties (`@theme` / `:root`) | Bilan colors, fonts, spacing, radii, shadows |
| **Base** | Modern CSS Reset (Tailwind Preflight) | Consistent cross-browser baseline |
| **Layout** | CSS Grid / Flexbox + Tailwind utilities | Responsive grids without Bootstrap |
| **Components** | Astro `<style>` scoped blocks | Component-specific CSS, no leakage |
| **Utilities** | Tailwind CSS v4 | One-off spacing, colors, responsive tweaks |
| **Icons** | Inline SVG or Lucide | No icon font bloat |

**Why Tailwind + Astro?**
- **Astro ships zero JS by default** — Tailwind is build-time only (CSS, no runtime)
- **Purge on steroids** — Tailwind scans your `.astro` files and generates *only* the CSS you use
- **Responsive design** — `md:text-lg`, `lg:grid-cols-3` beats media queries manually
- **Design token integration** — Tailwind v4 reads your custom properties as theme values

---

## 📐 Design Tokens (The Bilan Language)

### Color Tokens

These must match `BRAND_STYLE_SHEET.md` exactly. Currently `style.css` uses wrong colors (`#4b59e9` instead of `#0066CC`).

```css
:root {
  /* Brand */
  --bilan-blue: #0066CC;
  --bilan-accent-blue: #80cdff;
  --bilan-green: #00aa44;
  --bilan-red: #cc0000;
  
  /* Neutrals */
  --bilan-white: #ffffff;
  --bilan-black: #111111;
  --bilan-dark-gray: #333333;
  --bilan-light-gray: #f5f5f5;
  
  /* Semantic */
  --text-primary: var(--bilan-black);
  --text-secondary: var(--bilan-dark-gray);
  --surface-primary: var(--bilan-white);
  --surface-secondary: var(--bilan-light-gray);
  --surface-accent: #e0f2f7;
  --border-subtle: #e0e0e0;
}
```

### Typography Tokens

```css
:root {
  /* Font families */
  --font-head: 'Poppins', system-ui, sans-serif;
  --font-body: 'Metropolis', system-ui, sans-serif;
  
  /* Scale — major third (1.25 ratio) */
  --text-xs: 0.75rem;      /* 12px */
  --text-sm: 0.875rem;     /* 14px */
  --text-base: 1rem;       /* 16px */
  --text-md: 1.125rem;     /* 18px */
  --text-lg: 1.25rem;      /* 20px */
  --text-xl: 1.5rem;       /* 24px */
  --text-2xl: 1.875rem;    /* 30px */
  --text-3xl: 2.25rem;     /* 36px */
  --text-4xl: 3rem;        /* 48px */
  --text-5xl: 3.75rem;     /* 60px */
  --text-6xl: 4.5rem;      /* 72px */
  
  /* Weights */
  --weight-normal: 400;
  --weight-medium: 500;
  --weight-semibold: 600;
  --weight-bold: 700;
  
  /* Line heights */
  --leading-tight: 1.2;
  --leading-snug: 1.35;
  --leading-normal: 1.5;
  --leading-relaxed: 1.7;
}
```

### Spacing Tokens

```css
:root {
  --space-1: 0.25rem;   /* 4px */
  --space-2: 0.5rem;    /* 8px */
  --space-3: 0.75rem;   /* 12px */
  --space-4: 1rem;      /* 16px */
  --space-5: 1.25rem;   /* 20px */
  --space-6: 1.5rem;    /* 24px */
  --space-8: 2rem;      /* 32px */
  --space-10: 2.5rem;   /* 40px */
  --space-12: 3rem;     /* 48px */
  --space-16: 4rem;     /* 64px */
  --space-20: 5rem;     /* 80px */
  --space-24: 6rem;     /* 96px */
  --space-32: 8rem;     /* 128px */
}
```

### Radii & Shadows

```css
:root {
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --radius-full: 9999px;
  
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-md: 0 4px 6px rgba(0,0,0,0.07);
  --shadow-lg: 0 10px 15px rgba(0,0,0,0.1);
  --shadow-card: 0 2px 12px rgba(0,0,0,0.08);
}
```

---

## 🎨 Tailwind CSS v4 + Astro Integration

### Installation

```bash
cd bilan-mx-astro
npx astro add tailwind
```

This installs `@tailwindcss/vite` and adds it to `astro.config.mjs`.

### Configuration (CSS-native, no JS config file needed)

Create `src/styles/theme.css`:

```css
@import "tailwindcss";

@theme {
  /* Colors */
  --color-bilan-blue: #0066CC;
  --color-bilan-accent: #80cdff;
  --color-bilan-green: #00aa44;
  --color-bilan-red: #cc0000;
  --color-bilan-black: #111111;
  --color-bilan-dark: #333333;
  --color-bilan-light: #f5f5f5;
  --color-surface-accent: #e0f2f7;
  
  /* Fonts */
  --font-head: 'Poppins', system-ui, sans-serif;
  --font-body: 'Metropolis', system-ui, sans-serif;
  
  /* The token system above becomes Tailwind classes:
     text-bilan-blue, bg-surface-accent, font-head, etc.
  */
}
```

### Usage in Astro Components

```astro
---
// Card.astro
const { title, description } = Astro.props;
---

<article class="bg-white rounded-xl shadow-card p-6 transition-transform hover:-translate-y-1">
  <h3 class="font-head font-bold text-xl text-bilan-black mb-2">{title}</h3>
  <p class="font-body text-bilan-dark leading-relaxed">{description}</p>
</article>

<style>
  /* Scoped overrides if needed */
  article:hover {
    box-shadow: 0 8px 24px rgba(0,0,0,0.12);
  }
</style>
```

**No inline `style=""` needed.** Every style is a class that references the token system.

---

## 🏗️ Scoped Component Patterns (Astro-native)

Astro's killer feature: `<style>` blocks inside `.astro` files are **scoped by default**. The CSS only applies to elements in that component's template.

### Pattern 1: Blog Card (from your existing blog)

```astro
---
// BlogCard.astro
const { post } = Astro.props;
---

<article class="blog-card">
  {post.data.image && (
    <a href={`/blog/${post.slug}`}>
      <img src={post.data.image} alt={post.data.imageAlt || post.data.title} />
    </a>
  )}
  <div class="content">
    <div class="tags">
      {post.data.tags.map(tag => (
        <a href={`/blog/tags/${tag}`} class="tag">{tag}</a>
      ))}
    </div>
    <h3><a href={`/blog/${post.slug}`}>{post.data.title}</a></h3>
    <p>{post.data.description}</p>
    <div class="meta">
      <time>{post.data.pubDate.toLocaleDateString('es-MX')}</time>
      <a href={`/blog/${post.slug}`} class="read-more">Leer más →</a>
    </div>
  </div>
</article>

<style>
  .blog-card {
    background: var(--bilan-white);
    border-radius: var(--radius-lg);
    overflow: hidden;
    box-shadow: var(--shadow-card);
    height: 100%;
    display: flex;
    flex-direction: column;
    transition: transform 0.2s;
  }
  .blog-card:hover {
    transform: translateY(-4px);
  }
  .blog-card img {
    width: 100%;
    height: 200px;
    object-fit: cover;
  }
  .blog-card .content {
    padding: var(--space-6);
    flex: 1;
    display: flex;
    flex-direction: column;
  }
  .blog-card .tag {
    display: inline-block;
    background: #e3f2fd;
    color: var(--bilan-blue);
    padding: var(--space-1) var(--space-3);
    border-radius: var(--radius-full);
    font-size: var(--text-sm);
    text-decoration: none;
    transition: all 0.2s;
  }
  .blog-card .tag:hover {
    background: var(--bilan-blue);
    color: var(--bilan-white);
  }
  .blog-card h3 {
    font-family: var(--font-head);
    font-size: var(--text-xl);
    font-weight: var(--weight-bold);
    margin-bottom: var(--space-3);
  }
  .blog-card h3 a {
    color: inherit;
    text-decoration: none;
  }
  .blog-card p {
    color: var(--bilan-dark);
    flex: 1;
  }
  .blog-card .meta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: auto;
    font-size: var(--text-sm);
    color: var(--bilan-gray);
  }
  .blog-card .read-more {
    color: var(--bilan-blue);
    font-weight: var(--weight-medium);
    text-decoration: none;
  }
  .blog-card .read-more:hover {
    text-decoration: underline;
  }
</style>
```

**Why this is better than inline styles:**
- All styles in one place (the component file)
- Uses tokens (maintainable)
- Scoped (won't leak to other cards)
- No `!important` battles with Bootstrap
- Readable, debuggable in DevTools

### Pattern 2: Hero Section (replacing your inline styles)

```astro
---
// HeroSection.astro
import { homeHeroPurchaseWhatsappUrl, homeHeroConsultWhatsappUrl } from '../utils/whatsapp';
---

<section class="hero">
  <div class="container">
    <h1>
      <span class="accent">Hidratación real</span>
      <br />
      Solo lo esencial
    </h1>
    <h2>
      Electrolitos sin azúcar, sin saborizantes y sin aditivos.
      <br />
      Solo sodio, potasio y magnesio — nada más.
    </h2>
    <div class="actions">
      <a href={homeHeroPurchaseWhatsappUrl} class="btn btn-primary">
        Compra por WhatsApp
      </a>
      <a href={homeHeroConsultWhatsappUrl} class="btn btn-outline">
        Resuelve tus dudas
      </a>
    </div>
  </div>
</section>

<style>
  .hero {
    background-image: url("/images/home-page/home-cycle-bg.png");
    background-position: center;
    background-size: cover;
    min-height: 643px;
    display: grid;
    place-items: center;
    text-align: center;
  }
  .hero .container {
    max-width: 800px;
    padding: var(--space-8);
  }
  .hero h1 {
    font-family: var(--font-head);
    font-size: clamp(2.75rem, 5vw, 4.5rem);
    font-weight: var(--weight-bold);
    color: var(--bilan-white);
    line-height: var(--leading-tight);
  }
  .hero h1 .accent {
    color: var(--bilan-accent-blue);
  }
  .hero h2 {
    font-family: var(--font-body);
    font-size: clamp(1.5rem, 2.5vw, 1.875rem);
    font-weight: var(--weight-semibold);
    color: var(--bilan-white);
    line-height: var(--leading-snug);
    margin-top: var(--space-5);
    letter-spacing: 0.05em;
  }
  .hero .actions {
    display: flex;
    gap: var(--space-4);
    flex-wrap: wrap;
    justify-content: center;
    margin-top: var(--space-8);
  }
  .hero .btn {
    padding: var(--space-3) var(--space-6);
    border-radius: var(--radius-md);
    font-weight: var(--weight-semibold);
    text-decoration: none;
    transition: all 0.2s;
  }
  .hero .btn-primary {
    background: var(--bilan-green);
    color: var(--bilan-white);
    border: 2px solid var(--bilan-green);
  }
  .hero .btn-outline {
    background: transparent;
    color: var(--bilan-green);
    border: 2px solid var(--bilan-green);
  }
  .hero .btn:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
  }
  
  @media (max-width: 576px) {
    .hero {
      min-height: 400px;
      padding-top: var(--space-16);
    }
    .hero h1 {
      font-size: 2.5rem;
    }
    .hero .actions {
      flex-direction: column;
      align-items: stretch;
    }
  }
</style>
```

---

## 🔄 Bootstrap Migration Roadmap

### Why Migrate?

| Metric | With Bootstrap | After Migration |
|--------|---------------|-----------------|
| CSS download | ~164 KB | ~8–15 KB (Tailwind, purged) |
| Custom CSS | 2,798 lines | ~200–400 lines (tokens + scoped) |
| Unused CSS | ~85% | ~0% (Tailwind scans files) |
| Specificity wars | Constant | None (utility classes) |
| Mobile debugging | Hard (override chains) | Easy (one class = one property) |

### The Phased Plan

**Phase 0: Foundation (1–2 days)**
1. Install Tailwind CSS v4 + Astro integration
2. Create `src/styles/theme.css` with Bilan tokens
3. Add `@import "tailwindcss"` to BaseLayout
4. Verify build passes, no visual regression

**Phase 1: Tokenize (ongoing as you touch files)**
1. Replace hardcoded colors in `style.css` with token references
2. Replace inline `style=""` with Tailwind utility classes
3. Extract repeated patterns into scoped component styles

**Phase 2: Grid Migration (1 day)**
1. Replace `container` / `row` / `col-*` with CSS Grid or Tailwind grid utilities
2. The blog index page is easiest (card grid)
3. Landing page sections one by one

**Phase 3: Component Extraction (ongoing)**
1. Turn repeated HTML patterns into `.astro` components
2. Move their CSS into scoped `<style>` blocks
3. Delete the corresponding rules from `style.css`

**Phase 4: Bootstrap Removal (1 day)**
1. Remove Bootstrap CSS import from BaseLayout
2. Remove Bootstrap JS import from BaseLayout
3. Delete `bootstrap.min.css` from project
4. Delete `ofo.css` (it's dead)
5. Audit `style.css` — delete unused rules

**Phase 5: Polish (ongoing)**
1. Add `@layer` architecture to `theme.css`
2. Optimize font loading (`font-display: swap`)
3. Add `prefers-reduced-motion` support
4. Accessibility audit (focus states, color contrast)

---

## 📏 Responsive Design System

### Breakpoint Strategy

```css
/* Mobile-first approach */
/* Base styles = mobile */
/* @media (min-width: ...) = larger screens */

--breakpoint-sm: 640px;   /* Large phones */
--breakpoint-md: 768px;   /* Tablets */
--breakpoint-lg: 1024px;  /* Small laptops */
--breakpoint-xl: 1280px;  /* Desktops */
--breakpoint-2xl: 1536px; /* Large screens */
```

### Tailwind Responsive Pattern

```astro
<!-- Card grid: 1 col mobile → 2 col tablet → 3 col desktop -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  {posts.map(post => <BlogCard {post} />)}
</div>

<!-- Hero text: smaller on mobile, scales up -->
<h1 class="text-3xl md:text-4xl lg:text-5xl xl:text-6xl">
  Hidratación real
</h1>
```

**Teaching note:** Mobile-first means you write the mobile styles first (default), then add `@media (min-width: ...)` for larger screens. This is the opposite of Bootstrap's desktop-first approach (`col-md-6` means "6 columns at md and up"). Mobile-first is the modern standard because mobile traffic dominates.

---

## 🧪 CSS Architecture Rules

### Do
- ✅ Use tokens for all colors, fonts, spacing, shadows
- ✅ Scope component styles in `<style>` blocks
- ✅ Use Tailwind utilities for one-offs (margins, paddings, colors)
- ✅ Write mobile-first responsive styles
- ✅ Use `clamp()` for fluid typography
- ✅ Group related components in `src/components/` subfolders

### Don't
- ❌ Add inline `style=""` attributes (use classes or scoped styles)
- ❌ Use `!important` (signal of specificity battle)
- ❌ Write new CSS in `style.css` (add to component scopes instead)
- ❌ Hardcode colors/values (always reference tokens)
- ❌ Use Bootstrap classes for new components
- ❌ Mix Bootstrap grid with CSS Grid (pick one)

---

## 📚 File Locations (Target State)

```
bilan-mx-astro/
├── src/
│   ├── styles/
│   │   ├── theme.css          # Tailwind + Bilan tokens
│   │   ├── base.css           # Minimal resets (imported by theme)
│   │   └── globals.css        # Any unavoidable global rules
│   ├── components/
│   │   ├── ui/                # Reusable UI primitives
│   │   │   ├── Button.astro
│   │   │   ├── Card.astro
│   │   │   └── Badge.astro
│   │   ├── layout/
│   │   │   ├── Header.astro
│   │   │   ├── Footer.astro
│   │   │   └── Container.astro
│   │   ├── blog/
│   │   │   ├── BlogCard.astro
│   │   │   ├── BlogPost.astro
│   │   │   └── TagBadge.astro
│   │   └── landing/
│   │       ├── HeroSection.astro
│   │       ├── FeatureGrid.astro
│   │       └── ProductShowcase.astro
│   └── pages/
│       ├── index.astro        # Composes landing components
│       └── blog/
├── public/
│   └── images/
└── dist/                      # Build output
```

---

## 🎓 Teaching Quick Reference

**Q: Why Tailwind instead of writing my own CSS?**
A: Tailwind doesn't replace your design system — it encodes it. You define tokens once (`--color-bilan-blue`), then use `text-bilan-blue`, `bg-bilan-blue`, `border-bilan-blue` anywhere. Tailwind scans your files at build time and generates *only* the CSS you actually use. A full Tailwind build is 3.5MB, but after purging your site probably uses 8–15KB. You write faster, ship less.

**Q: What's the difference between scoped Astro styles and Tailwind utilities?**
A: Scoped styles are for component structure ("this card has padding, border-radius, and a hover effect"). Tailwind utilities are for one-off adjustments ("this specific card needs extra top margin"). A good rule: if you write the same 3+ Tailwind classes together more than twice, extract them into a scoped component style.

**Q: Why mobile-first?**
A: Because ~60% of web traffic is mobile. Mobile-first means your base styles work on phones, and you add complexity for larger screens with `@media (min-width:)`. Desktop-first (Bootstrap's approach) means you write desktop styles first, then override them for mobile. More code, more bugs.

**Q: What about the existing 2,785 lines in `style.css`?**
A: We don't rewrite them all at once. As we migrate each section (hero, features, blog), we move its CSS into scoped components and delete the corresponding rules from `style.css`. Over 2–3 months, `style.css` shrinks to just global resets and unavoidable legacy rules.

**Q: Can I keep Bootstrap for the navbar only?**
A: Technically yes, but it's expensive. The navbar uses `navbar`, `navbar-expand-xl`, `collapse`, `navbar-nav`, `nav-item`, `nav-link` — maybe 5KB of Bootstrap's CSS. But you ship all 164KB. Better to rewrite the navbar as a simple Astro component with scoped styles. It's 50 lines of HTML + 80 lines of CSS.

---

## 🔧 Skills Ecosystem for Pro Web Dev

You asked about "systems, skills, agents." Here's the complete skill architecture I recommend:

| Skill | Purpose | When to Load |
|-------|---------|--------------|
| `bilan-base` | Brand, products, voice, terminology | **Every task** |
| `bilan-webdev` | Astro architecture, i18n, feature flags, build system | Code changes, debugging, planning enhancements |
| `bilan-design` | **This skill** — CSS, tokens, Tailwind, responsive, migration | Styling, layout, visual changes, new components |
| `bilan-blog-ops` | Content creation, frontmatter, publishing workflow | Writing/editing posts, translations |
| `bilan-marketing` | Campaigns, personas, copy, social | Marketing content, landing page copy |
| `bilan-sales` | Pricing, CRM, proposals, objections | Sales pages, checkout flows, partnerships |
| `graphify` | Codebase queries, architecture visualization | Understanding file relationships, refactoring |

**The skill interaction model:**
- User asks about styling → load `bilan-design` + `bilan-base`
- User asks about a new landing section → load `bilan-design` + `bilan-webdev` + `bilan-marketing`
- User asks about blog post + styling → load `bilan-blog-ops` + `bilan-design` + `bilan-base`

**Pro tip:** Each skill is a context window. Loading more skills = more context = better decisions. But loading irrelevant skills = noise. Pi should intelligently select the right combination.

---

## 📋 Next Action: Start the Migration

If you want to begin, the first step is:

```bash
cd bilan-mx-astro
npx astro add tailwind
```

Then create `src/styles/theme.css` with the token system above, import it in `BaseLayout.astro`, and verify the build still passes. **Zero visual changes** — just infrastructure.

After that, we tackle one component at a time (hero, blog cards, navbar) through the 4-gate review workflow.

**Ready to start, or do you want to see a specific component migrated first as a demo?**
