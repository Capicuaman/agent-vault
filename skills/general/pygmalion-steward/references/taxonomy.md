# Entity Taxonomy

What each Family is for, what it produces, and where the ladder stops.
Normative definitions: [`glossary.md`](glossary.md). Map: [`org-chart.md`](org-chart.md).

## The families

| Family | Naming | Role | Produces | Terminal? | Registry of record |
|---|---|---|---|---|---|
| **Steward** | `*-steward` | **governance** — decides what exists | intake cards, decisions, portfolio health | **yes** | `README.md` + `MANIFEST.md` |
| **Doctrine** | `*-doctrine` | **knowledge** — how to judge | judgment (no artifact) | **yes** | `README.md` + `MANIFEST.md` |
| **Forge** | `*-forge` | **production** — makes artifacts | artifacts of a declared shape | no | `_forge-pattern.md` |
| **Forge-nerd** | `*-forge-nerd` | **audit** — keeps a corpus true | audits, spec amendments | **yes** | `_forge-pattern.md` |
| **Scout** | `*-scout` | **detection** — nominates | opportunity cards | **yes** | `_tech-nerd-pattern.md` |
| **Nerd** | `*-nerd` | **corpus** — expert persona | grounded answers | no | `_tech-nerd-pattern.md` |
| **Genie** | `genie-*` | **corpus** — mines change | transferable lessons | no (`genie-doctrine` terminal) | `skills/genies/README.md` |
| **Skill** | `skills/<cat>/<name>/` | **corpus** — procedure | changed behavior | no | `README.md` + `MANIFEST.md` |
| **Registry** | `registries/_*-pattern.md` | **governance** — the law | conformance | **yes** | itself |
| **Drill pack** | `examples/*.md` | **corpus** — training | practice | yes | producer's forge |
| **Prompt** | `prompts/*.md` | **corpus** — one-shot | a better first turn | yes | `README.md` |
| **System prompt** | `system-prompts/*.md` | **knowledge** — standing posture | consistent identity | yes | `README.md` |

## Doctrine vs Steward — the distinction

This is the most important boundary in the governance layer.

| | **Doctrine** | **Steward** |
|---|---|---|
| Question it answers | *How should I judge this?* | *Should this exist, and as what?* |
| Input | a situation to evaluate | a request for an Entity |
| Output | judgment | a decision record (intake card) |
| Has an intake flow | no | **yes** |
| Produces artifacts | never | decisions, not Entities |
| Authority over inventory | none | **full** |
| Terminal | yes | yes |

A Doctrine with an intake flow has become a Steward. A Steward without intake is
just a checklist.

**Test:** if the Entity's main verb is *judge*, it is a Doctrine. If its main verb
is *decide*, it is a Steward.

## Fit decision tree

Stop at the first yes.

1. **Is it a request to decide whether/what to create?** → steward (or the
   Steward's own intake, if it is a one-off).
2. **Is it a one-off instruction you will not reuse?** → prompt.
3. **Is it pure data** (JSON, CSV, a table)? → a generator output, not an Entity.
4. **Does it need multiple turns, files, or a procedure?** → skill.
5. **Does it produce *other artifacts to a declared shape*?** → forge.
6. **Does it produce grounded answers about exactly one technology?** → nerd.
7. **Does it detect when something should be made?** → scout.
8. **Does it audit a corpus and amend specs?** → forge-nerd (above the threshold
   in `_forge-pattern.md`).
9. **Is it a shared lens read by several Entities, with no output?** → doctrine.
10. **Does it mine change artifacts for lessons?** → genie.

For steps 2–4, defer to `prompt-skill-agent-triage` — it owns the echelon decision.
This tree extends it with the Families it does not cover.

## Terminal climb levels

Recursion must stop. Each Family may climb exactly one level above its producers:

```
prompt ─┐
skill ──┼─→ forge ─→ forge-nerd (terminal)
nerd ───┘              │
                       └─→ registry (terminal)

request ─→ steward (terminal — one governance role, not a hierarchy)
genie ───→ genie-doctrine (terminal)
doctrine ─→ (nothing — a Doctrine is already the top)
scout ────→ (nothing — a Scout is already the top)
```

**Forbidden by construction:**

- `forge-forge` — a forge producing forges is just a forge
- `nerd-forge-nerd-nerd` — the climb stops at the auditor
- `doctrine-doctrine` — a lens on a lens adds no judgment
- `steward-steward` — governance of governance is just governance
- `scout-forge` — detection and production are different roles

If you feel the need to climb again, the level below is under-specified. Fix the
spec.

## Composition rules

- **A Doctrine is read, not executed.** No output shape, no `examples/`.
- **A Steward decides, not builds Family anatomies.** It routes nerd and forge
  shapes to their producers.
- **A Forge must declare its output shape.** No shape, no forge.
- **A Nerd must not produce artifacts.** If it starts generating files to a
  template, it has become a Forge — split it.
- **A Scout must not build.** The moment it does, its findings stop being
  independent.
- **A Registry outranks an executable.** When `_tech-nerd-pattern.md` and
  `nerd-forge` disagree, the registry wins and the forge is corrected.
- **One canonical spec per Family.** Two specs is a Duplicate at the spec level
  and will produce divergent artifacts.

## What is *not* an Entity

- A session note or personal preference.
- A one-off command you ran once.
- A data file, index, or generated report.
- A checklist embedded in another Entity (a section, not a Family).
- A `README.md` inside a skill directory — documentation, not an Entity.
- A row in this table — a Family is not an Entity.

Naming these explicitly prevents the most common corpus bloat: turning every
useful paragraph into an Entity.

## Scope

Every Entity lives in exactly one Scope. Scope is part of its identity.

| Scope | Location | Loaded |
|---|---|---|
| **vault (source of truth)** | `agent-vault/skills/<category>/<name>/` | by install |
| **global** | `~/.pi/agent/skills/<name>/` or `~/.agents/skills/<name>/` | every session |
| **project** | `<repo>/.pi/skills/<name>/` or `<repo>/.agents/skills/<name>/` | when pi starts in that repo |

A global nerd whose references cite project-local docs is mis-scoped; move it to
project scope or re-ground its references. See [`administer.md`](administer.md).
