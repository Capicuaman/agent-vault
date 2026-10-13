---
name: bilan-sales
description: Sales-specific workflows, pricing tiers, objection handling, CRM stages, and competitive battle cards for bilan. Use when drafting proposals, pricing negotiations, sales emails, CRM updates, or competitive positioning. Assumes bilan-base knowledge is also loaded.
---

# bilan — Sales Domain Skill

## When to Use

Load this skill alongside `bilan-base` when the task involves:
- Pricing discussions or proposal generation
- Objection handling or sales scripts
- CRM stage definitions or pipeline review
- Competitive positioning or battle cards
- Upsell/cross-sell strategy
- Corporate wellness (B2B) deal flow

## Pricing Tiers (Consumer — B2C)

| Tier | Price (MXN) | Biomarkers | Add-ons | Delivery |
|------|-------------|------------|---------|----------|
| Essential | $1,499 | 6 basic metabolic | — | Digital report, 48h |
| Complete | $2,499 | 12 metabolic + hormonal | 1 add-on | Digital report + 15-min consult, 48h |
| Premium | $3,999 | Full 18-marker panel | 2 add-ons | Digital report + 30-min consult + 90-day re-test, 48h |

**Bundle rules:**
- Couples/family bundles: 15% off for 2+ kits purchased together.
- Subscription: 20% off quarterly re-tests. Minimum 2 deliveries.
- Corporate volume: See B2B table below.

## Pricing Tiers (Corporate — B2B)

| Company Size | Tests/Year | Price/Test | Services Included |
|--------------|------------|------------|-------------------|
| 50–100 employees | 50–150 | $1,199 | On-site collection, aggregate dashboard, 1 wellness webinar |
| 101–300 employees | 151–500 | $999 | Above + quarterly aggregate report, priority scheduling |
| 301–500 employees | 501+ | Custom | Above + dedicated account manager, white-label report option |

**B2B contract terms:**
- Minimum commitment: 12 months or 50 tests (whichever comes first).
- Payment: 50% upfront, 50% on delivery of first batch.
- Cancellation: 30-day notice. Refund prorated for unused tests.

## CRM Stages (HubSpot / Pipedrive)

1. **Lead** — Inbound form fill, event scan, referral.
2. **Qualified** — SDR confirms budget, authority, need, timeline (BANT).
3. **Proposal Sent** — Pricing and scope shared. 3-day follow-up rule.
4. **Negotiation** — Objections surfaced, terms discussed.
5. **Closed Won** — Contract signed, onboarding scheduled.
6. **Closed Lost** — Reason logged (price, timing, competition, no-need).
7. **Nurture** — Re-engagement drip for 6 months.

## Objection Handling

| Objection | Response Framework |
|-----------|-------------------|
| "Too expensive" | Anchor to clinic cost (3× higher), introduce subscription or Essential tier, offer payment plan. |
| "I can get this at my doctor" | Acknowledge. Differentiate: speed (48h vs. 2 weeks), convenience (home), depth (lifestyle context, not just diagnosis). |
| "I don't understand the results" | Lean into consult tiers. "Your Complete tier includes a 15-minute walkthrough with a health coach." |
| "My company already has a wellness program" | Probe for data. "Does your current program show metabolic ROI? We provide aggregate dashboards." |
| "I need to ask my partner / doctor" | Provide a shareable PDF summary. Set a 7-day follow-up. Offer a joint consult call. |
| "Privacy concerns" | Reference encryption, anonymization, no-data-sale policy. Offer corporate anonymized aggregate-only reporting. |

## Competitive Battle Cards

### vs. Traditional Lab (Quest, Labcorp equivalent in LatAm)
- **Their strength:** Insurance coverage, diagnostic authority.
- **Our angle:** Speed, convenience, lifestyle context, no referral needed.
- **Dodge:** Don't compete on diagnostic authority. Compete on access and actionability.

### vs. Wellness Apps (Noom, MyFitnessPal)
- **Their strength:** Daily engagement, habit tracking.
- **Our angle:** Bloodwork is the ground truth apps lack. "Track your macros. Now verify your metabolism."
- **Dodge:** We are not a diet app. We are the data layer.

### vs. Other Direct-to-Consumer Testing
- **Their strength:** Often cheaper or US-based with shipping.
- **Our angle:** LatAm-first logistics, Spanish-first reports, local customer service, culturally relevant ranges.
- **Dodge:** Don't compete on price alone. Compete on trust and locality.

## Upsell / Cross-sell Rules

- **Metabolic → Hormonal:** "Your glucose is stable. Want to see how your cortisol tracks with it?"
- **B2C → B2B:** "Your team has 80 people. Want to pilot a corporate wellness program?"
- **One-time → Subscription:** "Your markers shift every 90 days. A subscription locks in 20% off and keeps you on track."
- **Digital → Consult:** "Your results are in. A 15-minute consult helps you build a 30-day action plan."

## Sales Email Templates

### Cold Outreach (B2B)
Subject: `Wellness ROI for [Company] — a 3-minute read`
Body: Open with a relevant metric (e.g., "Companies with metabolic screening see 12% lower sick days"). Introduce bilan corporate. Offer a 10-minute call or a one-pager. CTA: calendar link.

### Follow-up (Post-Proposal)
Subject: `Quick question about the [Date] proposal`
Body: One paragraph. Reference a specific detail from the proposal. Ask a binary question ("Does the Q3 timeline work, or should we look at Q4?").

### Re-engagement (Closed Lost → Nurture)
Subject: `New: [Feature] — thought of [Company]`
Body: Short update on something new since the last conversation. No hard sell. Invite them to reply if timing is better now.

## References

- FAQ: `01_PROJECTS/BILAN/MARKETING/RAG/faq.json`
- Corporate wellness details: `01_PROJECTS/BILAN/OPERATIONS/`
- Past proposals: `01_PROJECTS/BILAN/SALES/`
