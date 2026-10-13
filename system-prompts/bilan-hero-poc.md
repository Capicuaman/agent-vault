# BILAN Hero Section — Pi Context

## Project
- **File**: `WORKING/bilan-hero-poc-v1.html`
- **Goal**: Mobile-first hero section for BILAN hydration product website
- **Stack**: Vanilla HTML/CSS/JS, Canvas API for effects, no frameworks
- **Constraint**: No autoplay animations — all effects activate on user interaction only
- **Review target**: Telegram mobile browser (primary user reviews on phone)

## Current Status (last session Jul 16)
Working on adding mobile-first interactive effects to the hero:

### Effect A — Touch-reactive 3D product card 🎮
- Finger becomes light source
- Touch and drag on hero → product card tilts in 3D toward finger
- Glossy sheen slides across bag surface following touch
- Stops instantly on lift (no momentum/motion sickness)
- Must feel premium and tactile like native app

### Other planned effects (from last session)
- Effect B — Canvas particle burst on tap (mineral ions scatter and reform)
- Effect C — Scroll-reveal stagger for text elements (no parallax)

## BILAN Product Context
- **What**: Electrolyte hydration powder (sodium + potassium + magnesium)
- **Tagline**: "Hidratación con balance mineral" (Spanish primary)
- **SKUs**: 3g sachet ($15), 100g ($150), 200g ($330), 1kg ($1,450), 10kg B2B ($12,500)
- **Packaging**: 3g=foil sachet, 100g/200g/1kg=compostable kraft bags, 10kg=foil sack
- **Brand colors**: Deep navy, mineral teal, warm sand
- **Tone**: Scientific credibility + accessible lifestyle

## Technical Constraints
- NO rotating rings, drifting orbs, floating cards (user finds them annoying)
- Static decorative shapes only; one-time entrance fades OK
- No flicker, no jank on 60fps mobile
- Canvas effects must use `will-change` and `requestAnimationFrame` properly
- CSS transforms > position changes for performance

## User Preferences
- Reviews visually via screenshots before approving
- Spanish copy required alongside English
- Prefers agent execution over tutorials ("You do it")
- All copy-pasteable text (URLs, paths, IDs) must be in inline code or code blocks
