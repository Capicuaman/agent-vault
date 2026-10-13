# Pattern: Meta-Consultant Spawn (Climb One Level)

**Captured:** 2026-10-07
**Origin prompt:** *"I want you to go meta and create a nerd-forge-nerd.skill to help me forge the best nerds and forges for my nerds and forges."*

## When to reach for it
You have a *maker* (a forge, a template, a generator) that has produced ≥2 artifacts, and the artifacts are starting to drift in quality or shape. You want a steward, not another maker.

## Template
```
Go meta and create a <maker>-<domain-expert> to help me
<maker-verb> the best <artifacts> and <sibling-artifacts>
for my <artifacts> and <sibling-artifacts>.
```

## Required ingredients
1. **"Go meta"** — explicit permission to climb one abstraction level.
2. **Named artifact** — a concrete file to produce (`.skill`, `.md`, `.ts`), not a conversation.
3. **Maker verb** — reuse the existing maker's verb (forge, scaffold, generate, draft).
4. **Quality word** — "best", "cleanest", "most grounded" — signals audit, not volume.
5. **"My" possessive** — scopes to your existing corpus, not generic theory.
6. **Sibling plural** — "nerds **and** forges" — forces boundary clarification AND acts as the recursion stop-sign.

## Preconditions
- ≥ 2 of the artifact exist on disk (corpus to steward).
- A maker already exists.
- Quality variance is observable.

## Anti-triggers
- Only one artifact → premature meta.
- No maker → nothing to critique against.
- Writing "meta-meta" → cut back one level.

## Diagnostic before invoking
*"If this meta-expert existed, what would its first three audit findings be?"*
If you can't name three, the corpus isn't ripe. Keep making artifacts first.

## What it produces (invariants)
A persona that:
- **Does not** make new things (hand off to the maker).
- **Does** audit, split/merge/retire, sync registries, catch spec drift, teach the pattern.
- **Terminates** the recursion (one climb, no forge-forge-forges).

## Historical uses
- 2026-10-07 — `nerd-forge-nerd` (meta over `nerd-forge` + 6 existing `*-nerd`/`*-forge` skills).
