# bilan label source map

Paths are relative to the bilan project root
(`${BILAN_PROJECT:-$HOME/Documents/textDump/01_PROJECTS/BILAN}`).

## 1. Source of truth (wins over everything below)

- `PACKAGING/source-of-truth/SCHEMA.md` — rules for the YAML layout
- `PACKAGING/source-of-truth/shared.yaml` — brand, front/back panel, nutrition,
  ingredients, preparation, warnings, storage, manufacturer, seals
- `PACKAGING/source-of-truth/tokens.yaml` — colors, typography scale, layout
- `PACKAGING/source-of-truth/skus/100g.yaml`
- `PACKAGING/source-of-truth/skus/200g.yaml`
- `PACKAGING/source-of-truth/skus/1kg.yaml`
- `PACKAGING/source-of-truth/skus/10kg.yaml`
- `PACKAGING/source-of-truth/PHASE1_DIFF_REPORT.md` — what the consolidation
  changed and why (read this before "fixing" anything that looks odd)

Each SKU file starts with `extends: shared` and lists only deltas.

## 2. Product facts (not label copy)

- `bilan_source_of_truth.json` — canonical product facts, packaging commitment,
  known gaps (barcodes null, 3 g trial SKU, pricing omitted)
- `bilan_source_of_truth.md` — human-readable summary

## 3. Decisions

- `PACKAGING/CHANGELOG.md` — Keep-a-Changelog format; locked standards and dates
- `PACKAGING/README.md` — entrypoint, mental model, phase status

## 4. Human-facing deliverables (may lag the YAML)

- `PACKAGING/DELIVERABLES/BILAN_Label_Elements_Report.html`
- `PACKAGING/DELIVERABLES/BILAN_Label_Responsive_Generator.html`
- `PACKAGING/DELIVERABLES/BILAN_Label_Master_Dossier.html`
- `PACKAGING/DELIVERABLES/index.html`

## 5. HTML proofs

- `PACKAGING/etiqueta-100g.html`
- `PACKAGING/etiqueta-200g.html`
- `PACKAGING/etiqueta-1kg.html`

## 6. Vector execution files

- `PACKAGING/ETIQUETAS_100g.svg`
- `PACKAGING/ETIQUETAS_200g.svg`
- `PACKAGING/ETIQUETAS_1kg.svg`
- `PACKAGING/ETIQUETAS_10kg.svg`
- `PACKAGING/etiqueta_100g.svg` (older single-SKU export; check before trusting)

## 7. Brand / typography references

- `BRAND_STYLE_SHEET.md` — brand-wide fonts (site: Poppins/Metropolis/FoundryGridnik;
  poster: Inter) — not the packaging standard
- `PACKAGING/source-of-truth/tokens.yaml → typography` — packaging standard
- `ASSETS/fonts/Helvetica Neue/`, `ASSETS/fonts/Montserrat/`
- `poster/remotion/src/lib/fonts.ts` — poster system only

## 8. Assets

- `ASSETS/logo-bilan.svg`
- `ASSETS/exceso-sodio.svg`
- `ASSETS/svg/excessodeSodio.svg`

## 9. Expansion / pending work

- `PACKAGING/info.md` — Inkscape / MCP label adaptation notes
- `PACKAGING/HIRING/hiring_plan.md`
- `PACKAGING/HIRING/BILA-14_tracker.md`
- `PACKAGING/HIRING/readme.md`

## 10. Archive — history, never a source

- `PACKAGING/archive/pre-consolidation-2026-09-29/` — frozen pre-YAML state
  (the 4 `etiqueta-*.json` files and their HTML/SVG siblings). Rollback safety
  net only; never edit, never cite as current.

## Working rule

When there is disagreement:

1. `source-of-truth/shared.yaml` + `skus/*.yaml` + `tokens.yaml`
2. `bilan_source_of_truth.json` (for product facts)
3. `CHANGELOG.md` (for decisions already made)
4. deliverable docs
5. HTML proofs
6. SVG execution files
7. archive (never)
