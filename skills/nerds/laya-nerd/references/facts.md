# laya facts

Snapshot date: 2026-10-06  
Primary source: https://github.com/NandhaKishorM/laya  
Local bilan summary: `01_PROJECTS/BILAN/OPERATIONS/laya-ops-non-ops-summary.md`

Treat this as a snapshot. For latest releases, APIs, package names, model limits, or benchmark claims, refresh from the live GitHub repo and docs before answering.

## Identity

laya is a multilingual, non-autoregressive System 1 decision engine. It answers typed decision questions over text or JSON-like state in a single forward pass. Its job is not to write prose; its job is to choose, score, gate, route, and abstain with a structured result.

## One-paragraph canon

laya is best understood as a fast typed-decision layer that sits beside generative agents. Claude/pi should still do synthesis, writing, research, and multi-step repair work. laya should handle repeatable judgments: `choice` among fixed options, ordinal `score`, and `noul` yes/no probability. In bilan, that makes laya most useful as a workflow router, claim-safety gate, content triage layer, RAG categorizer, packaging-change classifier, and eventually operations stop/go gate.

## Key facts

| Thing | Value |
|---|---|
| Repo | `https://github.com/NandhaKishorM/laya` |
| Core pitch | Typed choice, score, and yes/no decisions over text in one forward pass |
| Decision primitives | `choice`, `score`, `noul` |
| Python install | `python -m pip install laya` |
| Python quickstart object | `from laya import Router`; `router = Router()` |
| TypeScript surface | `laya-ts/` in the repo; npm package described as `laya-ts` |
| HTTP serving | `laya-serve` through `laya[serve]` / Docker |
| Model routing | `Router` chooses English, multilingual, or typed-decisions checkpoints |
| Long input note | multilingual checkpoint can be called with larger `max_len`, but validate accuracy on local data |
| Confidence gate | Gate on `answer_confidence`, not prose vibes |
| Structured decisions | JSON schema / pydantic model can be projected into typed questions |
| Best bilan fit | Decision governance over existing files, not content generation |

## What laya is not

- Not a replacement for Claude, pi, or other generative agents.
- Not a free-form writer.
- Not a database validator by itself; deterministic validation should still be regular code.
- Not an autonomous operator unless wrapped by workflow code and human approval gates.
- Not automatically trustworthy on every domain; schemas and thresholds need local evaluation.

## Bilan ops vs non-ops definitions

**Ops use cases** affect execution, revenue, stock, customer outreach, fulfillment, or team accountability. Wrong decisions can block sales, trigger bad outreach, distort reports, or create operational debt.

**Non-ops use cases** affect knowledge, content, routing, quality control, and creative workflow decisions without directly moving inventory, money, orders, or customer commitments. These are safer first pilots.

## Recommended first pilot

Start with **Prompt Router + Claim-Safety Gate**.

Why:
- It improves collaboration immediately.
- It is lower-risk than sales or inventory.
- It uses bilingual text decisions, where laya is designed to help.
- It creates reusable schema patterns for later ops gates.
- Claude/pi can still do the writing and revisions after laya decides route or risk level.

## Source priority for answers

1. `references/` in this skill.
2. `01_PROJECTS/BILAN/OPERATIONS/laya-ops-non-ops-summary.md`.
3. Local bilan files for the target workflow.
4. Live laya repo/docs for current APIs and release details.
5. Actual `python -m pip show laya`, `laya --help`, or local install behavior if present.

If sources disagree, prefer live docs/API behavior for laya mechanics and local bilan docs for bilan workflow boundaries.
