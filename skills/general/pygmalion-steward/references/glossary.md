# Glossary — Formal Terms

These definitions are normative for the vault. When a word is capitalized in a
steward document, this file is the authority.

## The core nouns

### Entity
A file-backed, discoverable unit that changes agent behavior when routed to.

An Entity must have all five:

1. **Identity** — a unique lowercase kebab-case name matching its directory.
2. **Routing contract** — a description that decides invocation.
3. **Body** — a procedure, lens, or procedure-with-examples.
4. **Home** — exactly one scope (vault source + install target).
5. **Registry line** — one authoritative listing.

Anything missing one of the five is a *draft*, not an Entity.

### Corpus
The complete set of Entities in the vault, plus their registries and catalogs.
The Corpus has health (see *Health state*), not just content.

### Family
A named class of Entity sharing an anatomy, a role, and a Registry of record.

Current Families: `prompt`, `skill`, `nerd`, `forge`, `forge-nerd`, `scout`,
`doctrine`, `steward`, `genie`, `drill-pack`, `system-prompt`.

### Role
A Family's function in the organization chart, independent of its content:
**governance**, **production**, **detection**, **knowledge**, **audit**,
**corpus**. Roles explain *why* a Family exists; Families explain *what* it looks
like.

### Registry of record
The single file that authoritatively lists a Family's members and its spec.

| Family | Registry of record |
|---|---|
| nerd, scout | `registries/_tech-nerd-pattern.md` |
| forge, forge-nerd | `registries/_forge-pattern.md` |
| everything else | `README.md` + `MANIFEST.md` |

Two registries for one Family is a *Duplicate at the spec level* and is forbidden.

### Scope
Where an Entity is loaded. Part of its identity.

| Scope | Location |
|---|---|
| **vault** | `agent-vault/skills/<category>/<name>/` (source of truth) |
| **global** | `~/.pi/agent/skills/<name>/` or `~/.agents/skills/<name>/` |
| **project** | `<repo>/.pi/skills/<name>/` or `<repo>/.agents/skills/<name>/` |

An Entity has exactly one Scope. A global Entity that cites project-local docs is
mis-scoped.

### Echelon
The prompt → skill → agent level of a request, per `prompt-skill-agent-triage`.
Echelon is orthogonal to Family: a skill can be any Family.

## The roles

### Doctrine
An Entity whose only output is **judgment**. It is read by other Entities, not
executed for the operator.

A Doctrine must satisfy all four:

1. **No output shape.** It produces no artifact template and requires no
   `examples/`.
2. **Read by others.** At least one other Entity cites it as its lens.
3. **Terminal.** There is no doctrine-doctrine; a lens on a lens adds no judgment.
4. **Prescriptive, not procedural.** It tells you *how to decide*, not *what to do
   next*.

`genie-doctrine` is the canonical example. If an Entity has an intake flow, a
decision record, or produces artifacts, **it is not a Doctrine**.

> A Doctrine changes how you judge. A Steward changes what exists.

### Steward
An Entity that receives requests, decides whether and how many Entities are
needed, routes production, and keeps the portfolio coherent.

A Steward must:

1. **Accept requests** in natural language, not only explicit commands.
2. **Produce decision records** (intake cards) — its artifact is a decision, not
   the built Entity.
3. **Decompose** one request into the minimum set of Entities.
4. **Route** to the Family producer rather than duplicating its anatomy.
5. **Audit** the Corpus against reality (health states and drift).
6. **Never create a meta level above itself.**

`pygmalion-steward` is the canonical (and currently only) Steward.

### Forge
A production Entity: it creates other artifacts to a repeatable spec. Must have a
declared output shape and ≥1 canonical example. Never an expert, steward, or
detector.

### Forge-nerd
The audit Entity for one Forge's output corpus. Terminal: it amends the spec, it
does not forge another forge-nerd.

### Scout
A detection Entity: it flags opportunities and produces opportunity cards. It
does not build. Terminal.

### Nerd
An expert persona for exactly one technology, grounded in a priority chain. It
answers; it does not produce artifacts.

### Genie
A Family that goes meta into software change artifacts (fixes, changelogs, PRs,
issues, postmortems, design docs, tests, git history) to extract transferable
lessons.

## The properties

### Behavior delta
The difference in agent behavior with the Entity loaded versus without. The only
valid justification for an Entity's existence.

### Routing contract
The description field. Determines whether the Entity is invoked. It is the most
consequential text in the file and the only thing most sessions will read.

### Gate
A binary pass/fail check. Four gates: **Routable**, **Different**, **Bounded**,
**Registered**. A single failure blocks the Entity.

### Score
A 0–3 quality rating on **Grounding**, **Executability**, **Maintainability**.
Nine points total; ship at ≥7 with all Gates passed.

### Terminal climb
The maximum meta level a Family may reach. Above it, recursion adds cost without
judgment. Enforced by design, not by convention.

### Intake card
The Steward's decision record: restated request, expected delta, verdict,
decomposition, org placement, producer, gates, and next action.

### Decomposition
Splitting one request into the minimum set of Entities, one routing boundary each.

### Stewardship
The ongoing accountability for Corpus truth: health, drift, counts, and registry
coherence.

## The health states

| Term | Definition |
|---|---|
| **Zombie** | An Entity that fails to load (bad YAML, missing description, name ≠ dir) |
| **Ghost** | A reference to an Entity that does not exist |
| **Orphan** | An Entity that no registry or catalog lists |
| **Hollow** | An Entity with no procedure, references, or examples |
| **Stale** | An Entity whose dated grounding is past the threshold |
| **Duplicate** | Two Entities with ≥85% description similarity |
| **Statue** | An Entity with no evidence of ever being invoked |
| **Drift** | Divergence between an Entity's grounding and current upstream reality |

### Talos
The installed-copy guard: a check that compares vault skills against every install
root by content hash. Named for the bronze automaton that patrolled Crete. Talos
reports `drift` (repairable), `diverged` (holds extra files; needs a human),
`missing` (a choice, not an error), and `unmanaged` (installed, not from the
vault). It never guesses and never repairs a superset.

### Drift
Specifically: an Entity is internally consistent and loadable, but the world moved.
A nerd whose snapshot says `0.9.3` while upstream is `1.4.0` is **drifted**, not
stale — staleness is about the date, drift is about the facts.

Drift is detected by a **probe**: a declared, re-runnable command that yields the
current upstream version. See [`drift.md`](drift.md).

## Words to stop using loosely

| Do not say | Say instead |
|---|---|
| "skill" when you mean any Entity | Entity, or name the Family |
| "meta-skill" | name the Family and its climb level |
| "update the docs" | name the Registry of record |
| "it's stale" | Stale (dated) or Drifted (facts moved) |
| "let's make a thing" | state the Behavior delta first |
