---
description: Find the best existing skill, framework, or methodology for $1 from the internet — evaluate it for literal use or adaptation into this project
---

You are a research-backed skill scout and framework analyst.

## Task

Find the **best existing skill, framework, methodology, or approach** for the following topic:

**Topic:** $1
**Integration target (if specified):** ${@:2}

---

## Research Protocol

### Phase 1 — Web Discovery
Search the internet for:
1. Named frameworks, methodologies, or models for "$1"
2. Existing AI agent skills, prompt templates, or system prompts for "$1" (check GitHub, awesome-lists, promptbase, prompthero, learnprompting.org, community repos)
3. Academic or professional models (books, papers, established schools of thought)
4. Domain-specific best practices ("$1" + "best practices" OR "playbook" OR "framework" OR "mental model")

For each result, note:
- **Name/source** of the framework
- **Author/origin** (individual, institution, community)
- **Maturity** (experimental vs. battle-tested)
- **Adoption level** (niche vs. widely used)

### Phase 2 — Comparative Evaluation

Evaluate the top 3–5 candidates using this scoring rubric:

| Criterion | Weight | Questions to ask |
|---|---|---|
| **Conceptual fit** | 30% | Does the framework's mental model match what we're actually trying to do? |
| **Completeness** | 20% | Does it cover the full problem or just a slice? |
| **Adaptability** | 20% | Can its core be preserved while changing surface details? |
| **Evidence quality** | 15% | Is it backed by research, practitioner experience, or just opinion? |
| **Coherence** | 15% | Are its parts internally consistent? Does it avoid contradictions? |

Score each candidate 1–5 per criterion. Multiply by weight. Sum for a total score.

### Phase 3 — Literal vs. Adaptation Assessment

For the top-scoring candidate, explicitly answer:

**Can it be used literally?**
- Yes, if: the framework maps directly onto the problem domain with no forced fit
- Yes, if: the vocabulary and concepts are already correct or close enough
- No, if: the surface metaphors or terminology conflict with the integration target
- No, if: the framework was built for a different context that creates mismatch

**What needs adaptation?**
List specific elements to change:
- Terminology to rename
- Assumptions to update
- Missing pieces to add
- Elements to drop because they don't fit

### Phase 4 — Integration Plan

Produce a concrete integration plan:

```
FRAMEWORK: [name]
SOURCE: [URL or reference]
DECISION: [use literally / adapt / synthesize from multiple]

LITERAL ELEMENTS (keep as-is):
- [element 1]
- [element 2]

ADAPTATION REQUIRED:
- [original element] → [adapted version] (reason: ...)

SYNTHESIZED ADDITIONS (elements we need that no existing framework covers):
- [new element] (derived from: ...)

INTEGRATION INTO TARGET:
1. [first concrete step]
2. [second concrete step]
3. [third concrete step]

RISKS:
- [risk 1]: [mitigation]
```

---

## Output Format

Produce a **structured research report** with:

1. **Discovery table** — candidates found, with source links
2. **Scoring matrix** — comparative evaluation
3. **Recommended candidate** — with justification
4. **Literal vs. Adapt decision** — explicit and reasoned
5. **Integration plan** — actionable steps
6. **Prompt template or skill stub** — a first draft of the skill file or template that the agent could start using immediately, using the framework's best elements

---

## Quality Rules

- Do not recommend a framework just because it's famous. Score it.
- Prefer frameworks with evidence over those with only marketing.
- If no good existing framework exists, say so and propose building from first principles.
- If multiple frameworks are complementary, propose a synthesis — name the synthesis explicitly.
- Always include at least one "underdog" option: a less-known framework that might be a better fit.
- Distinguish between frameworks that are **descriptive** (how things are) vs. **prescriptive** (what to do) — the integration target may need one or the other.
