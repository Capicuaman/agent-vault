# Entity Taxonomy

What each family is for, what it produces, and where the ladder stops.

## The families

| Family | Naming | Role | Produces | Terminal? | Registry of record |
|---|---|---|---|---|---|
| **Prompt** | `prompts/*.md` | one-shot instruction | a better first turn | yes | `README.md` |
| **Skill** | `skills/<cat>/<name>/` | context-loaded procedure | changed behavior | no | `README.md` + `MANIFEST.md` |
| **Nerd** | `*-nerd` | expert persona on one technology | grounded answers | no | `_tech-nerd-pattern.md` |
| **Forge** | `*-forge` | maker to a repeatable spec | artifacts of a declared shape | no | `_forge-pattern.md` |
| **Forge-nerd** | `*-forge-nerd` | steward/auditor of one forge's corpus | audits, template amendments | **yes** | `_forge-pattern.md` |
| **Scout** | `*-scout` | detector of opportunities | opportunity cards | **yes** | `_tech-nerd-pattern.md` |
| **Registry** | `registries/_*-pattern.md` | canonical spec + corpus index | conformance | **yes** | itself |
| **Doctrine** | `*-doctrine` | shared lens used by several entities | judgment | **yes** | `README.md` |
| **Genie** | `genie-*` | meta over software change artifacts | transferable lessons | no (`genie-doctrine` is terminal) | `skills/genies/README.md` |
| **Drill pack** | `examples/*.md` | training exercise | practice | yes | producer's forge |
| **System prompt** | `system-prompts/*.md` | standing identity/context | consistent posture | yes | `README.md` |

## Fit decision tree

Stop at the first yes.

1. **Is it a one-off instruction you will not reuse?** → prompt. Keep it out of the
   skill tree.
2. **Is it pure data** (JSON, CSV, a table)? → a generator output, not an entity.
3. **Does it need multiple turns, files, or a procedure?** → skill.
4. **Does it produce *other artifacts to a declared shape*?** → forge.
5. **Does it produce grounded answers about exactly one technology?** → nerd.
6. **Does it detect when something should be made?** → scout.
7. **Does it audit a corpus and amend specs?** → forge-nerd (only above the
   threshold in `_forge-pattern.md`).
8. **Is it a shared lens read by several entities?** → doctrine.
9. **Does it mine change artifacts for lessons?** → genie.

For steps 1–3 specifically, defer to `prompt-skill-agent-triage` — it owns the
echelon decision and the frequency/risk gates. This tree extends it with the
families it does not cover.

## Terminal climb levels

Recursion must stop. Each family may climb exactly one level above its producers:

```
prompt ─┐
skill ──┼─→ forge ─→ forge-nerd (terminal)
nerd ───┘              │
                       └─→ registry (terminal)

genie ─→ genie-doctrine (terminal)
doctrine ─→ (nothing — a doctrine is already the top)
scout ─→ (nothing — a scout is already the top)
```

**Forbidden by construction:**

- `forge-forge` (a forge producing forges is just a forge)
- `nerd-forge-nerd-nerd` (the climb stops at the auditor)
- `doctrine-doctrine` (a lens on a lens adds no judgment)
- `scout-forge` (detection and production are different roles)

If you feel the need to climb again, the real problem is that the level below is
under-specified. Fix the spec.

## Composition rules

- **A doctrine is read, not executed.** It has no output shape; it changes how
  other entities judge. That is why it needs no `examples/`.
- **A forge must declare its output shape.** No shape, no forge.
- **A nerd must not produce artifacts.** If it starts generating files to a
  template, it has become a forge — split it.
- **A scout must not build.** The moment it does, its findings stop being
  independent.
- **A registry outranks an executable.** When `_tech-nerd-pattern.md` and
  `nerd-forge` disagree, the registry wins and the forge is corrected. The forge
  cites the registry; it does not fork it.
- **One canonical spec per family.** Two specs for the same family is a Duplicate
  at the spec level, and it will produce divergent artifacts.

## What is *not* an entity

- A session note or personal preference.
- A one-off command you ran once.
- A data file, index, or generated report.
- A checklist embedded in another entity (that is a section, not a family).
- A `README.md` inside a skill directory — it is documentation, not an entity.

Naming these explicitly prevents the most common corpus bloat: turning every
useful paragraph into a skill.

## Scope

Every entity lives in exactly one scope. Scope is part of its identity.

| Scope | Location | Loaded |
|---|---|---|
| **Vault (source of truth)** | `agent-vault/skills/<category>/<name>/` | by install |
| **Global** | `~/.pi/agent/skills/<name>/` or `~/.agents/skills/<name>/` | every session |
| **Project** | `<repo>/.pi/skills/<name>/` or `<repo>/.agents/skills/<name>/` | when pi starts in that repo |

A global nerd whose references cite project-local docs is mis-scoped; move it to
project scope or re-ground its references. See
[`administer.md`](administer.md) for the install and drift rules.
