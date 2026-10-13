---
name: bilan-base
description: Core company knowledge for bilan (health and wellness brand). Use when any task involves company strategy, products, brand voice, visual identity, key personnel, or terminology. Covers mission, product lines, target market, brand palette, typography rules, and bilingual content conventions.
---

# bilan — Base Knowledge

## Mission & Values

- **Mission:** Make metabolic health visible and actionable for Spanish-speaking populations through affordable, lab-accurate wellness testing.
- **Core values:** Scientific accuracy, accessibility, cultural relevance (LatAm-first), privacy-first data handling.
- **Tagline (Spanish):** *Tu salud, en números.*
- **Tagline (English):** *Your health, in numbers.*

## Product Lines

1. **Metabolic Panel (Panel Metabólico)** — 12 biomarkers: glucose, HbA1c, lipids, liver enzymes, uric acid, creatinine.
2. **Hormonal Panel (Panel Hormonal)** — 6 biomarkers: testosterone, estradiol, TSH, cortisol, DHEA-S, SHBG.
3. **Inflammation Add-on** — hsCRP, homocysteine.
4. **Corporate Wellness (Bienestar Corporativo)** — On-site testing + dashboards for HR teams.

## Target Market & Personas

- **Primary:** Health-conscious individuals aged 25–45 in Mexico, Colombia, Argentina.
- **Secondary:** HR/benefits managers at mid-size companies (50–500 employees).
- **Personas:**
  - *Ana (The Optimizer):* 32, tracks macros, wants data to fine-tune diet.
  - *Carlos (The Preventer):* 45, family history of diabetes, wants early signals.
  - *Lucía (The HR Lead):* 38, responsible for employee wellness budgets.

## Brand Voice & Terminology

- **Brand name:** Always write `bilan` in lowercase, even at the start of a sentence. Preserve uppercase only inside actual folder/path names such as `01_PROJECTS/BILAN/`.
- **Bilingual default:** Content is often English + Spanish. When drafting, provide both unless the channel is monolingual.
- **Tone:** Professional but accessible. Avoid medical jargon unless followed by a plain-language explanation.
- **Scientific accuracy:** Validate health claims against `01_PROJECTS/BILAN/MARKETING/RAG/faq.json` and `glosario_unified.md`. Cite sources when possible.
- **Data privacy:** Never imply data is sold. Use "encrypted, anonymized diagnostics."

## Visual Identity

### Color Palette (Digital HEX / Print CMYK)

| Token | HEX | CMYK | Usage |
|-------|-----|------|-------|
| bilan Blue | `#0066CC` | C100 M50 Y0 K0 | Primary brand color, headlines, CTAs |
| White | `#FFFFFF` | — | Backgrounds, negative space |
| Black (UI text) | `#111111` | C0 M0 Y0 K93 | Primary text |
| Dark Gray | `#333333` | C0 M0 Y0 K80 | Body text |
| Light Gray | `#F5F5F5` | C0 M0 Y0 K5 | Surfaces, cards |
| Performance Green | `#00AA44` | C85 M0 Y100 K0 | Positive results, "after" states |
| Depletion Red | `#CC0000` | C0 M100 Y100 K20 | Problems, "before" states, alerts |

**Usage rules:**
- One dominant color per piece. If background is blue, accents are white. If background is white, headlines are blue.
- Green is for positive/"after", red for problems/"before". Pair them; avoid using either alone.
- Dark gray only for body and secondary information.

### Typography

- **Digital site (bilan.mx):**
  - Headlines: Poppins 700/500
  - Body/UI: Metropolis 400/500
  - Accent/Display (optional): FoundryGridnik 700
- **Poster/print system:** Inter 400/600/700

### CSS Tokens

```css
:root {
  --bilan-blue: #0066cc;
  --bilan-accent-blue: #80cdff;
  --bilan-white: #ffffff;
  --bilan-black: #1a1a1a;
  --bilan-dark-gray: #333333;
  --bilan-light-gray: #f5f5f5;
  --bilan-green: #00aa44;
  --bilan-red: #cc0000;
  --font-head: 'Poppins', system-ui, sans-serif;
  --font-body: 'Metropolis', system-ui, sans-serif;
}
```

### Quick Do/Don't

- Do: One font family per piece; contrast via size and weight.
- Do: Keep ≥20% whitespace; avoid decorative elements and gradients.
- Don't: Use drop shadows, bevels, or mixed fonts.
- Don't: Place the logo at the top of a layout (center or bottom-left preferred).

## Key Personnel

- **CEO / Product Lead:** [Name] — Vision, partnerships, regulatory compliance.
- **Head of Marketing:** [Name] — Brand, campaigns, content strategy.
- **Head of Operations:** [Name] — Logistics, lab partnerships, fulfillment.

## File References

- Brand style sheet: `01_PROJECTS/BILAN/BRAND_STYLE_SHEET.md`
- Colors (code): `01_PROJECTS/BILAN/poster/remotion/src/lib/colors.ts`
- Fonts (code): `01_PROJECTS/BILAN/poster/remotion/src/lib/fonts.ts`
- FAQ / RAG source: `01_PROJECTS/BILAN/MARKETING/RAG/faq.json`
- Glossary: `01_PROJECTS/BILAN/glosario_unified.md`
