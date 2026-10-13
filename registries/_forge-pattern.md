---
name: forge-pattern
description: "Hidden registry/meta-doc for the forge pattern and current forge corpus. Not an invocable skill; kept loadable only to satisfy pi root Markdown validation."
disable-model-invocation: true
---

# forge pattern

Meta-doc. Not a forge itself — the canonical spec every `*-forge` skill should conform to. Sibling of `_tech-nerd-pattern.md` (which specs nerds).

## What a forge is

A **forge** is a skill that **produces other artifacts to a repeatable spec**. It is a maker. It is not an expert, not a steward, and not a scout — those are different roles.

| Forge | Produces | Canonical example |
|---|---|---|
| `nerd-forge` | `*-nerd` skills | `bilan-mx-nerd` |
| `worktree-drill-forge` | drill packs | `herdr-ssh-worktree-pack.md` |
| `prompt-pattern-forge` | `_<name>-pattern.md` prompt-pattern docs | `_meta-consultant-spawn.md` |

## Required anatomy

Every forge **must** have:

```
<skill-root>/<thing>-forge/
  SKILL.md                 # activation triggers + procedure + anti-patterns
  examples/                # ≥ 1 canonical worked example (output the forge would produce)
    <example>.md
```

Optional (add when the forge grows):

```
  references/
    facts.md               # taxonomy, dated snapshot of the output ecosystem
    patterns.md            # heuristics, decision tables
```

A forge with **no examples/** is a half-forge: nothing proves the procedure actually produces the claimed shape. Fix before shipping.

## Required SKILL.md sections

1. **Frontmatter description** — trigger-rich, quoted. Must name:
   - The output artifact type (e.g. "`*-nerd` skills", "prompt-pattern docs").
   - Explicit activation phrases ("make a X", "forge a X", "<thing>-forge").
   - What the forge will NOT do (hand-offs).
2. **Posture** — grounded, kindly corrective, prefers composition.
3. **One-paragraph canon** — what this forge produces and why.
4. **Build procedure** — ordered, numbered steps. Must include:
   - Scope confirmation (ask or infer).
   - Source gathering (snapshot via `graphify_add` if the artifact grounds on external state).
   - **Serial write discipline** (one file at a time inside the new skill folder — parallel writes race to 0-byte).
   - **YAML quoting rule** (frontmatter `description:` wrapped in double quotes when it contains `:`, `#`, or starts with a special char).
   - Registry update (append to the appropriate `_<x>-pattern.md`).
   - Smoke test (state activation triggers out loud, confirm with user).
5. **Design rules** — the invariants every output must satisfy (3–6 rules). Specific to this forge.
6. **Anti-patterns** — what the forge refuses to do or avoids producing.
7. **Canonical example reference** — path to the exemplar in `examples/`.

## The six universal forge discipline rules

These apply to **every** forge regardless of what it produces:

1. **Named output shape.** The forge declares the exact file structure it produces. No "it depends."
2. **Scope lock before build.** Confirm the three Ws (what / where / why) before writing. One canonical scope question per forge.
3. **Serial writes inside the new folder.** Parallel `write` to the same new directory races to 0-byte files. Hard rule.
4. **YAML description always quoted.** Prevents silent skill-loader crashes. No exceptions.
5. **Registry update is part of the build.** Not a follow-up chore. If the forge doesn't register its output, the corpus drifts within one session.
6. **Smoke test before claiming done.** State activation triggers; verify files; confirm 0 zero-byte files.

## Scope boundaries (what forges are NOT)

- **Not nerds.** A forge does not become an expert on its output category — that's what a forge-nerd is for (e.g. `nerd-forge-nerd`).
- **Not scouts.** A forge does not detect when to invoke itself — that's a scout's job (e.g. `forge-scout`). Forges may *embed* small detection logic (e.g. "refuse if scope too fuzzy"), but they don't actively watch.
- **Not libraries.** A forge produces skills/docs with a persona or activation surface. If the output is pure data (JSON, CSV), it's a generator, not a forge.

## When to spawn a forge-nerd

Only when the forge's **output corpus crosses ~3–4 artifacts** AND quality is observably varying. Below that threshold, the forge author can self-audit. Above it, maintain a dedicated `*-forge-nerd` to audit the corpus, keep registries honest, and propose template amendments.

Current forge-nerds on disk:
- `nerd-forge-nerd` → stewards `nerd-forge`'s corpus (6+ nerds).

Candidate forge-nerds (not yet warranted):
- `prompt-pattern-forge-nerd` — spawn when ≥ 4 prompt patterns exist.
- `drill-forge-nerd` — spawn when ≥ 4 drill packs exist.

## Registry

Every forge lives in exactly one scope (global or project — see `_tech-nerd-pattern.md` for scope definitions) and belongs in that scope's registry.

### Current forges

| Forge | Scope | Output | Example | Forge-nerd? |
|---|---|---|---|---|
| `nerd-forge` | global | `*-nerd` skills | `bilan-mx-nerd` | ✅ `nerd-forge-nerd` |
| `worktree-drill-forge` | project (textDump) | drill packs | `herdr-ssh-worktree-pack.md` | ❌ (corpus = 1) |
| `prompt-pattern-forge` | global | `_<name>-pattern.md` | `_meta-consultant-spawn.md` | ❌ (corpus = 1) |

### Candidate forges (open the next one when the need shows up)

- `drill-forge` — generalize `worktree-drill-forge` to any topic domain
- `audit-forge` — produce dated audit reports to a repeatable shape (would steward `bilan-seo-conversion`-style outputs)
- `metaprompt-forge` — produce `01_PROJECTS/BILAN/METAPROMPTS/`-style agent instruction docs

## Forge discipline checklist (use before shipping a new forge)

- [ ] SKILL.md frontmatter description is quoted and trigger-rich
- [ ] `examples/` folder has ≥ 1 canonical worked example
- [ ] Build procedure includes serial-write + YAML-quoting + registry-update steps
- [ ] Design rules (≥ 3) are specific to this forge, not generic
- [ ] Anti-patterns section exists with ≥ 2 entries
- [ ] This file (`_forge-pattern.md`) has been updated to list the new forge
- [ ] 0-byte check passed
- [ ] Activation triggers stated and user-confirmed

## Related docs

- `~/.pi/agent/skills/registries/_tech-nerd-pattern.md` — nerd spec + nerd registry + scope definitions.
- `~/.pi/agent/skills/registries/_meta-consultant-spawn.md` — prompt pattern that spawns forge-nerds.
