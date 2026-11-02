---
name: bilan-label-system
description: "Manage bilan packaging labels end-to-end: front/back panel structure, typography decisions, source-of-truth discipline, Inkscape/SVG adaptation workflow, and print-readiness for new container formats. Use when editing label copy, changing fonts, resizing labels, adapting pouches to bottles/jars/tubes, or reconciling drift across JSON, HTML, SVG, and packaging docs."
---

# bilan Label System

Use this skill for **any work on bilan product labels**: copy, layout,
typography, container adaptation, print readiness, and drift reconciliation
across the structured source of truth, HTML proofs, SVG execution files, and
deliverable docs.

The label system is spread across layers that disagree easily. Your job is to
keep them aligned and to say plainly which layer changed.

**Last verified:** 2026-11-02 — the packaging folder now uses the YAML
source-of-truth introduced in the 2026-09-29 consolidation
(`source-of-truth/SCHEMA.md`, `shared.yaml`, `tokens.yaml`, `skus/*.yaml`).
The old per-SKU JSON is frozen in `archive/pre-consolidation-2026-09-29/`. The
Node render/validate pipeline and SVG templates are planned but not built yet —
`PACKAGING/README.md` is the authority on phase status.

## Where the project lives

The label system is part of the bilan project, which lives in the textDump
checkout, not in this vault:

```text
${BILAN_PROJECT:-$HOME/Documents/textDump/01_PROJECTS/BILAN}
```

If that directory is absent (a different machine, a fresh checkout), stop and
ask for the current checkout path. This skill carries the procedure; it does not
carry the product data. Do not invent label copy from memory.

Read these first, in order:

1. `PACKAGING/README.md` — project entrypoint and phase status
2. `PACKAGING/source-of-truth/SCHEMA.md` — the rules of the YAML layout
3. `PACKAGING/CHANGELOG.md` — locked decisions and their dates
4. `references/label-source-map.md` next to this skill — the full file map

## Source-of-truth hierarchy

When layers disagree, this order wins unless the operator explicitly overrides
it:

1. **YAML source of truth** (copy, tokens, per-SKU deltas)
   - `PACKAGING/source-of-truth/shared.yaml`
   - `PACKAGING/source-of-truth/skus/{100g,200g,1kg,10kg}.yaml`
   - `PACKAGING/source-of-truth/tokens.yaml`
2. **Product truth** — `bilan_source_of_truth.json` for facts that are not label
   copy (ingredients, servings, packaging commitment)
3. **Decision log** — `PACKAGING/CHANGELOG.md`
4. **Deliverable docs** — `PACKAGING/DELIVERABLES/*.html` (human-facing, may lag)
5. **HTML proofs** — `PACKAGING/etiqueta-*.html`
6. **SVG execution files** — `PACKAGING/ETIQUETAS_*.svg`
7. **Archive** — `PACKAGING/archive/pre-consolidation-2026-09-29/` is history.
   Never edit it and never treat it as current.

`source-of-truth/` inherits: `skus/<sku>.yaml` starts with `extends: shared` and
lists only deltas. Numeric field names carry units (`sodium_mg`,
`dimensions_cm`, `weight_g`). Colors reference tokens by name, never by hex.

When you find drift, report it in exactly these terms:

- **current implementation** — what the file actually says
- **source of truth** — what the YAML says
- **pending sync** — the propagation still owed

## Before editing — discovery procedure

1. Restate the request as a label change: which SKU(s), which container, which
   layer (copy, layout, typography, print, container format).
2. Read `PACKAGING/README.md` and note which phases are actually built. Do not
   assume the render pipeline exists.
3. Read `shared.yaml`, the affected `skus/*.yaml`, and `tokens.yaml` in full.
4. Read the affected HTML proof and SVG execution file, if any.
5. Check `PACKAGING/CHANGELOG.md` for a locked decision covering the request
   (typography, colors, tagline, ingredient order, 10kg format).
6. Copy `templates/label-change-brief.md` and fill it in **before** touching
   files.
7. Make the YAML edit first, then propagate.

## Locked standards (2026-09-29)

| Standard | Value | Where |
|---|---|---|
| Packaging typography | Helvetica Neue / Helvetica / Arial | `tokens.yaml → typography.primary_family` |
| Accent blue | `#0066CC` (`brand_blue`); old `#2E5AAC` deprecated | `tokens.yaml → color` |
| Official tagline | "Sube de nivel tu hidratación" | `shared.yaml → brand.tagline` |
| Ingredients (order rule) | Cloruro de sodio, potasio, magnesio; `descending_weight_in_formula` | `shared.yaml → back.ingredients` |
| 10kg format | pouch-led (Mylar bag); redesign deferred | `skus/10kg.yaml` |
| Build tool | Node (render/validate scripts: planned) | `PACKAGING/README.md` |

Changing any of these requires a `CHANGELOG.md` entry **and** an update to this
skill. Never migrate a font silently because another bilan system uses it.

## Front-panel checklist

- [ ] correct logo asset (`ASSETS/logo-bilan.svg`)
- [ ] `EXCESO SODIO` seal present, octagon, top-right, `warning_red`
- [ ] product identity consistent with the source of truth
- [ ] hero stats unchanged: **1000 mg sodium / 200 mg potassium / 80 mg magnesium**
- [ ] claims identical across YAML, HTML, and SVG
- [ ] net content matches the SKU delta
- [ ] hierarchy still works at the new dimensions

## Back-panel checklist

- [ ] nutrition table matches `back.nutrition` (3 g serving; 0 kcal; sodium 44%,
      potassium 4%, magnesium 19% daily values)
- [ ] servings per package match the SKU delta
- [ ] ingredient order is regulatory (descending by weight, NOM-051)
- [ ] preparation text is the full scoop version (not the old short one)
- [ ] warnings and storage blocks present and complete
- [ ] manufacturer block present (BILAN, Av de los Maestros 56, Tlalnepantla)
- [ ] lot / expiry / barcode / QR zones reserved even when values are null
- [ ] no truncation after resizing

## Typography policy

- **Operational packaging font:** Helvetica Neue / Helvetica / Arial. Font
  files are licensed and live in `ASSETS/fonts/`; do not commit new copies.
- **Other bilan systems are not packaging.** bilan.mx uses Poppins + Metropolis
  + FoundryGridnik; the poster/print system uses Inter. Do not copy those
  families onto labels.
- Every font change must be labeled **keep operational packaging font**,
  **proposed packaging migration**, or **approved packaging standard**. Until
  approved, treat Helvetica Neue / Arial as the execution default.
- Sizes live in `tokens.yaml → typography.scale_pt`, not in copy documents.

## Change workflow

1. **Identify the SKU(s)** and the target container.
2. **Identify the layer changing:** truth/content, layout, font, print
   production, or container format.
3. **Read all affected files** (discovery procedure above).
4. **Edit the YAML source of truth first.** Copy changes never start in HTML or
   SVG.
5. **Propagate** to templates, HTML proofs, SVG execution files, and deliverable
   docs as far as they exist.
6. **Update `CHANGELOG.md`** when a standard changed; otherwise state the change
   in the change brief.
7. **Log drift or open decisions explicitly** — do not smooth them over.

## Container adaptation (pouch → bottle / jar / tube / stand-up pouch)

1. Convert the original Illustrator PDF to SVG if needed.
2. Confirm the target label area in millimetres.
3. Resize the canvas to the new container format.
4. Refit the front and back hierarchy (stats first, then claims, then legal).
5. Re-check copy fit, seal placement, and legal areas.
6. Export the editable SVG, a proof PNG, and a print-ready PDF.
7. Finalize CMYK, bleed, crop marks, and printer specs.
8. Verify against a physical dieline or supplier spec before declaring it done.

## Build pipeline (planned, not yet built)

`PACKAGING/README.md` describes the target pipeline:

```text
source-of-truth/*.yaml → templates/*.svg → scripts/render.mjs → dist/
```

Today only Phase 1 (YAML SSOT) and Phase 2 (tokens) exist; `templates/` and
`scripts/` do not. Until Phase 4 lands, follow the manual propagation in the
change workflow and say so in the change brief. `dist/` must never be committed.

## Typical outputs

- label change brief (from `templates/label-change-brief.md`)
- source-of-truth sync summary
- typography decision memo
- front/back audit
- container adaptation checklist
- print-readiness checklist
- master HTML dossier or review page

## Watch-outs

- Do not confuse **package dimensions** with **label panel dimensions**.
- Do not treat preview HTML as authoritative.
- Do not assume barcode / GTIN fields are complete — they are `null` on purpose
  until registered; keep the zone reserved.
- The 3 g trial SKU is documented in product constraints but is **not** a
  finalized packaging source set.
- The "grado farmacéutico, origen Alemania" qualifier is deliberately excluded
  from label copy; it belongs in the product ficha técnica only.
- Repo-wide label rules also appear in `PACKAGING/AGENTS.md`; if it and this
  skill disagree, fix both.

## References

- `references/label-source-map.md` — every file that may hold label truth
- `templates/label-change-brief.md` — fill this before editing
