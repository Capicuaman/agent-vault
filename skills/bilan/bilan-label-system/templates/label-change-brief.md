# bilan label change brief

Fill this before touching any file. It is the intake card for label work.

## Request
- Requested by:
- Date:
- Target SKU(s): 100g / 200g / 1kg / 10kg / other:
- Target container(s):
- Goal:

## Change type
- [ ] source-of-truth copy (`source-of-truth/*.yaml`)
- [ ] front panel layout
- [ ] back panel layout
- [ ] typography
- [ ] barcode / QR / lot area
- [ ] print production prep
- [ ] container adaptation

## Discovery done
- [ ] `PACKAGING/README.md` read (phase status known)
- [ ] `source-of-truth/shared.yaml` read
- [ ] affected `source-of-truth/skus/*.yaml` read
- [ ] `source-of-truth/tokens.yaml` read
- [ ] `PACKAGING/CHANGELOG.md` checked for a locked decision
- [ ] affected HTML proof and SVG execution file read

## Affected files
- `source-of-truth/shared.yaml`
- `source-of-truth/tokens.yaml`
- `source-of-truth/skus/*.yaml`
- `etiqueta-*.html`
- `ETIQUETAS_*.svg`
- `DELIVERABLES/*`
- `CHANGELOG.md`

## Current state
-

## Proposed change
-

## Source-of-truth check
- Product facts verified against `bilan_source_of_truth.json`:
- Claims verified:
- Nutrition / servings verified:
- Preparation / storage verified:
- Warnings verified:
- Manufacturer block verified:
- Ingredient order still regulatory (descending by weight):

## Typography decision
- Current packaging font: Helvetica Neue / Arial
- Proposed font:
- Decision status: keep operational / proposed migration / approved standard
- Reason:

## Front-panel impact
-

## Back-panel impact
-

## Print / production notes
- Canvas size (mm):
- Bleed:
- Crop marks:
- CMYK / RGB:
- Printer constraints:

## Drift found

| Layer | Says | Source of truth says | Pending sync |
|---|---|---|---|
|  |  |  |  |

## Open questions
-

## Completion checklist
- [ ] YAML updated (copy starts here)
- [ ] HTML proof updated
- [ ] SVG execution file updated
- [ ] deliverable docs updated, if the system changed
- [ ] `CHANGELOG.md` entry (required if a locked standard changed)
- [ ] pending drift documented
- [ ] `dist/` not committed (it does not exist until the render pipeline does)
