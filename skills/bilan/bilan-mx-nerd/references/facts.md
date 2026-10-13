# bilan.mx — Facts Snapshot

**Snapshot date:** 2026-10-06
**Source:** https://bilan.mx (captured via graphify_add → `01_PROJECTS/BILAN/raw/bilan_mx.md`)
**Also referenced:** `01_PROJECTS/BILAN/bilan_source_of_truth.{md,json}`, `01_PROJECTS/BILAN/DEPLOY.md`

Treat as snapshot. For "latest" questions, refresh via `graphify_add https://bilan.mx` first.

---

## Identity
- **Site:** https://bilan.mx — public marketing site for the bilan electrolyte powder brand (Mexico).
- **Tagline (live site):** *"Hidratación Real — Solo lo esencial"*
- **Tagline (SoT ES):** *"Rehidratación limpia y funcional: Electrolitos grado farmacéutico sin azúcar ni colorantes"*
- **Tagline (SoT EN):** *"The Power of Balance"*
- **Primary conversion CTA on-page:** *Compra por WhatsApp* (appears in nav and multiple sections).
- **Language toggle:** `EN` link in footer. Default is Spanish (es-MX).
- **Brand casing:** always lowercase `bilan` in prose and copy. Uppercase only in path segments like `/BILAN/`.

## Hosting / deploy split
- **`bilan.mx`** (marketing site): shared hosting. Astro static site. Deployed via standard Astro build pipeline. **Does NOT run on this machine.**
- **`app.bilan.mx`**: this box, behind Google login. Cloudflare DNS → Cloudflare Tunnel → `cloudflared` → Caddy `:8080` → Astro `localhost:3000` (bilan App) + OMNI API `localhost:8000`.
- Treat `bilan.mx` and `app.bilan.mx` as separate deployments. Don't conflate them.

## Primary nav (live)
`HOME · NOSOTROS · SALES · BLOG · PRODUCTOS · FAQ · Compra por WhatsApp`

> `SALES` in the top nav is literally that English word on the Spanish site. Worth flagging if auditing.

## Footer / secondary nav
- **Aprende:** Blog · Preguntas frecuentes · Nuestra historia · Recetas
- **Legal:** Aviso de privacidad · Términos y condiciones
- **Copyright line:** © 2026 bilan. Todos los derechos reservados.
- **Newsletter CTA:** *"Recibe consejos de hidratación — Suscribirme"*
- **Popup/modal:** *"Únete a la comunidad bilan — Suscríbete y recibe contenido exclusivo…"*

## Hero / value prop (live copy)
- H1 vibe: **"Hidratación real · Solo lo esencial"**
- Subhead: *"Electrolitos sin azúcar, sin saborizantes y sin aditivos. Solo sodio, potasio y magnesio — nada más."*
- CTA: **Compra por WhatsApp**

## Star product section (live)
- Pitch: **200gr** de fórmula, consumible diariamente, incluso por niños.
- **Live claim:** `200 gr Cont. Neto · 60 porciones por envase`
- **⚠️ Drift vs. source of truth:** `bilan_source_of_truth.md` says bilan-200g = **66 porciones**, not 60. Live site is understating. Flag this when it comes up.

## Product canon (from `bilan_source_of_truth.md`)
All SKUs share the same salt formula.

| SKU | Net weight | Servings | Flavor | Positioning |
|---|---|---|---|---|
| bilan-100g | 100 g | 33 | Natural | entry-level / frequent users |
| bilan-200g | 200 g | 66 | Natural | star product (live site shows 60) |
| (verify in SoT JSON for 500 g / bulk) | — | — | — | — |

**Per-serving formula (3 g scoop):** 1000 mg sodio · 200 mg potasio · 80 mg magnesio.

**Ingredients (live site):** Cloruro de Sodio · Cloruro de Potasio · Cloruro de Magnesio.

## "Lo que NO contiene" list (live, verbatim order)
Azúcar · Edulcorantes · Colorantes · Saborizantes · Rellenos · Gomas · Conservadores · Gluten · Lácteos · Soya

## Preparation (3-step block, live copy)
1. Mezcla 1 scoop (3 g) en 500 ml de agua o más.
2. Inicia tu hidratación 40 min antes del ejercicio.
3. Tómalo en un periodo de 30 min.

## FAQ block on the homepage (8 questions, verbatim order)
1. ¿Qué son los electrolitos y por qué importan?
2. ¿Por qué bilan no tiene azúcar ni saborizantes?
3. ¿Cuánto sodio tiene cada porción?
4. ¿Cómo se prepara bilan?
5. ¿Es seguro para niños o personas mayores?
6. ¿Puedo tomar bilan todos los días?
7. ¿Hacen envíos a todo México?
8. ¿Puedo usar bilan en ayuno intermitente o dieta keto?

The deep FAQ dataset lives in `01_PROJECTS/BILAN/MARKETING/RAG/faq.json` (richer than the homepage block).

## Commerce / fulfillment facts (live)
- **Shipping:** all of Mexico, 2–5 business days.
- **Free shipping threshold:** orders > $1,000 MXN.
- **Primary order channel on-page:** WhatsApp. (E-commerce platform docs live in `01_PROJECTS/BILAN/SALES/ECOMMERCE/`.)

## Known related skills (do not duplicate)
| Skill | Owns |
|---|---|
| `bilan-base` | brand DNA, personas, palette, typography |
| `bilan-marketing` | campaigns, personas, messaging |
| `bilan-sales` | pricing tiers, objections, CRM |
| `bilan-blog-ops` | blog publishing workflow |
| `bilan-design` | design tokens, CSS architecture |
| `bilan-webdev` | the **Astro codebase** behind bilan.mx |
| `bilan-seo-conversion` | periodic audit of bilan.mx SEO + CRO |

`bilan-mx-nerd` (this one) owns: **what the live page actually says and where** — the deployed artifact, not the strategy or the source code.

## Snapshot discipline
- `facts.md` is dated at the top. Refresh with `graphify_add https://bilan.mx` whenever asked about "latest", "current page", or copy changes.
- Local `bilan_source_of_truth.{md,json}` is ground truth for *facts* (SKUs, formula, pricing). When it disagrees with the live site, the SoT wins and the delta is a bug to flag.
- The Astro repo (separate from this one per `AGENTS.md`) is ground truth for *routing and components*.
