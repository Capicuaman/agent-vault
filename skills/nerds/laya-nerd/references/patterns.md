# laya decision patterns for bilan

Use these patterns when designing laya schemas, deciding whether laya fits a task, or translating a messy workflow into typed decisions.

## The laya decision loop

1. Define the **state**: the text, JSON, report, brief, or conversation laya will judge.
2. Define the **typed questions**: fixed `choice`, bounded `score`, or `noul` yes/no.
3. Define **criteria**: explicit option meanings; do not rely on label names alone.
4. Define **confidence behavior**: accept, abstain, or route to human review.
5. Define the **action policy**: what downstream agent or human does with the decision.
6. Log a **decision record** so the same decision can be audited later.

## Primitive selection

| Need | Primitive | Example |
|---|---|---|
| Pick one workflow | `choice` | `workflow = labels | posters | blog | RAG | packaging | ops` |
| Rank severity or fit | `score` | `claim_risk = 0..4` |
| Gate an action | `noul` | `needs_human_review = yes/no probability` |
| Mixed triage | multiple questions | route + risk + urgency + allowed action |

## Pattern 1: prompt router

Use when the user asks for work and the assistant needs to choose the right bilan workflow before acting.

State:
- User request.
- Relevant path if provided.
- Current repo context if obvious.

Questions:
- `workflow`: `choice` among `bilan_base`, `marketing`, `content_pipeline`, `poster`, `label_system`, `RAG`, `blog`, `operations`, `web`, `knowledge_garden`, `unknown`.
- `risk_level`: `score` 0-4.
- `needs_clarification`: `noul`.

Policy:
- High confidence route → load/use the matching skill or context.
- Low confidence or `needs_clarification` → ask one short question.
- `risk_level >= 3` → require human approval before edits.

## Pattern 2: claim-safety gate

Use before publishing health, electrolyte, product, or packaging copy.

State:
- Draft copy.
- Channel.
- Intended audience.
- Optional source facts from `MARKETING/RAG/`.

Questions:
- `claim_status`: `choice` among `safe`, `needs_source`, `medical_risk`, `too_strong`, `off_brand`, `human_review`.
- `medical_advice_risk`: `noul`.
- `purchase_cta_present`: `noul`.
- `rewrite_severity`: `score` 0-4.

Policy:
- `safe` → proceed.
- `needs_source` → cite or rewrite.
- `medical_risk`, `too_strong`, or low confidence → Claude/pi rewrites, human reviews if still risky.

## Pattern 3: content triage

Use when there are many content ideas or generated drafts and the question is where they belong.

State:
- Idea or draft.
- Campaign goal.
- Audience.
- Current content calendar if available.

Questions:
- `best_format`: `choice` among `instagram`, `tiktok`, `blog`, `whatsapp`, `x`, `email`, `sales_objection`, `FAQ`, `discard`.
- `audience_fit`: `score` 0-4.
- `brand_fit`: `score` 0-4.
- `claim_risk`: `score` 0-4.

Policy:
- Route to generator only if `brand_fit` and `audience_fit` are acceptable.
- If `claim_risk >= 3`, run claim-safety gate before generation.

## Pattern 4: RAG/FAQ maintenance

Use when new facts, claims, questions, or glossary terms appear.

State:
- Candidate fact/Q&A/term.
- Language.
- Source path or citation.

Questions:
- `destination`: `choice` among `faq_json`, `faq_es_json`, `glossary`, `product_docs`, `blog`, `do_not_add`, `human_review`.
- `duplicate_likelihood`: `score` 0-4.
- `source_required`: `noul`.

Policy:
- Never write directly to canonical RAG on laya alone.
- Use laya to route; use deterministic search plus human/agent review to update.

## Pattern 5: packaging-change triage

Use before touching label copy, HTML, SVG, JSON, or deliverable docs.

State:
- Requested change.
- Affected SKU/container.
- Existing source-of-truth snippets.

Questions:
- `change_type`: `choice` among `copy_only`, `layout_sensitive`, `regulatory_sensitive`, `source_of_truth_update`, `print_file_update`, `human_review`.
- `regulatory_risk`: `score` 0-4.
- `requires_bilan_label_system`: `noul`.

Policy:
- If `requires_bilan_label_system`, load/use the label-system skill.
- `regulatory_risk >= 2` → human approval before production file changes.

## Pattern 6: later ops gate

Use only after non-ops pilots prove useful.

State:
- Latest daily brief.
- Products CSV summary.
- Pipeline CSV health summary.
- Sales/report blockers.

Questions:
- `ops_mode`: `choice` among `normal`, `watch`, `critical`, `blocked`.
- `primary_blocker`: `choice` among `none`, `zero_inventory`, `pipeline_corruption`, `sales_data_corruption`, `human_overdue`, `regulatory_risk`, `unknown`.
- `allowed_action`: `choice` among `full_sales`, `research_only`, `education_content_only`, `cleanup_only`, `human_review_only`.
- `escalation_required`: `noul`.

Policy:
- Deterministic code should detect facts like duplicate headers and zero stock.
- laya should decide what those facts mean for workflow routing and escalation.

## Decision record template

```json
{
  "date": "YYYY-MM-DD",
  "workflow": "prompt_router",
  "state_ref": "path-or-description",
  "questions": ["workflow", "risk_level", "needs_clarification"],
  "answers": {
    "workflow": "content_pipeline",
    "risk_level": 2,
    "needs_clarification": false
  },
  "confidence": {
    "workflow": 0.86,
    "risk_level": 0.71,
    "needs_clarification": 0.91
  },
  "policy_action": "load bilan-marketing and content pipeline context",
  "human_review": false,
  "notes": "Low stakes; proceed."
}
```

## Fit test

Use laya when:
- The output is a fixed decision, not prose.
- The same judgment repeats often.
- There are clear criteria.
- Confidence/abstention can safely route to a human or generative agent.

Do not use laya when:
- The task is deterministic validation better done in code.
- The output requires long-form explanation or creative writing.
- The labels are vague or constantly changing.
- A wrong answer would silently trigger high-stakes business action.
