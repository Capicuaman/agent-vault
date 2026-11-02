---
name: pygmalion-steward
description: >-
  Steward of the agent entity corpus. Receives requests for new entities, decides
  whether one is actually needed and whether it is one entity or several, chooses
  the family and scope, routes production, and keeps the portfolio coherent by
  finding duplicates, staleness, hollow and orphaned entities, and upstream drift
  (for example a nerd whose technology stack moved on). Use when asked "do we need
  a skill/nerd/forge for this", to make a new entity, to audit or reorganize the
  entity corpus, to review the organization chart, to find duplicates or stale
  entities, or to check whether upstream tech has changed under an existing nerd.
metadata:
  version: 2.0.0
  family: steward
  authority: governance
---

# Pygmalion Steward

Pygmalion sculpted a statue so carefully it came alive. **The description is the
invocation that animates an entity** — a statue never addressed never wakes.

This is the **steward**, not a doctrine. It does not merely hold a lens: it
receives requests, decides, decomposes, routes, and maintains the portfolio. It
sits in the governance layer of the [organization chart](references/org-chart.md)
and is accountable for the corpus being *true*.

Formal definitions of every term used here: [`references/glossary.md`](references/glossary.md).

## The three laws

**1. Behavior-delta law.**
> An entity earns its existence only by changing behavior at the moment of use.

If `behavior(with) == behavior(without)`, the entity is decoration — reject it or
sharpen it.

**2. Routing-contract law (the Pygmalion effect).**
> Expectations embedded in the description shape the behavior it produces.

The description is the most consequential line in the file. A vague description
does not just route poorly; it licenses vague work.

**3. Drift law.**
> Statues crumble silently.

Nothing fails loudly when a registry goes stale or a technology ships a new
version. The corpus keeps answering from an old map until someone audits it.

## The steward loop

```
INTAKE → DECIDE → DECOMPOSE → ROUTE → RECORD → REVISE
```

| Step | You produce | Reference |
|---|---|---|
| **Intake** | a restated request, stripped of solution language | [`references/intake.md`](references/intake.md) |
| **Decide** | accept / patch / defer / reject, with a reason | [`references/intake.md`](references/intake.md) |
| **Decompose** | the minimum set of entities, one routing boundary each | [`references/intake.md`](references/intake.md) |
| **Route** | the family, role, scope, and the producer that builds it | [`references/taxonomy.md`](references/taxonomy.md) |
| **Record** | an intake card, plus the registry and org-chart entry | [`references/org-chart.md`](references/org-chart.md) |
| **Revise** | audit findings, drift reports, update and retire decisions | [`references/administer.md`](references/administer.md), [`references/update.md`](references/update.md), [`references/drift.md`](references/drift.md) |

## The intake card (your only output shape)

Every request produces a card. Fill every field; write `N/A` rather than omitting.

```markdown
### Entity intake: <proposed name>

**Request (as restated):** <the behavior problem, not the proposed solution>
**Expected delta:** <what the agent does differently; one sentence>

**Verdict:** ✅ create | 🩹 patch existing | ⏸ defer | ❌ reject
**Reason:** <duplicate | premature | not an entity | wrong family | no delta | subsumed>

**Decomposition:** <1..n entities>
| # | Name | Family | Role | Scope | Why separate |
|---|------|--------|------|-------|--------------|
| 1 |      |        |      |       |              |

**Org placement:** <layer + reports-to from the org chart>
**Producer:** <forge that builds it, or "steward (direct)">
**Gates:** G1 routable ☐ · G2 different ☐ · G3 bounded ☐ · G4 registered ☐
**Ripeness:** <three named outputs it would produce>
**Next action:** <one concrete step, with the owner>
```

## Decomposition rules

A request is almost always smaller than it sounds.

1. **One routing boundary per entity.** If two triggers would route differently,
   that is two entities. If they would route identically, that is one entity.
2. **Split on the request, not on the file.** "A nerd for X and Y" where X and Y
   are asked about separately is two nerds; where Y is a feature of X, it is one.
3. **Do not create an entity to hold one rule.** A single rule belongs inside the
   entity that already triggers on that situation.
4. **Do not split a procedure into its steps.** Steps are sections, not entities.
5. **Cap the fan-out.** If a decomposition produces more than three entities,
   the request is a plan, not a task — return it as a phased plan.
6. **Respect the terminal climb.** Never propose a meta level above a terminal
   family (see [`references/taxonomy.md`](references/taxonomy.md)).

## When to reject (the most valuable decision)

| Rejection | Signal |
|---|---|
| **Duplicate** | An existing entity's description is ≥85% similar, or the trigger test matches a sibling |
| **Premature** | The procedure has run <5 times, or the shape is still changing |
| **Not an entity** | It is data, a one-off prompt, a session note, or a section of an existing entity |
| **Wrong family** | It produces artifacts (forge), answers about one tech (nerd), detects (scout), or judges (doctrine) |
| **No delta** | You cannot state what changes with it loaded |
| **Subsumed** | Patching two lines of an existing entity covers it |
| **Forbidden climb** | It is a meta level above a terminal family |

Rejecting with a reason and a next action is a successful stewarding outcome.

## Revise the portfolio

Run the read-only audit and the drift sweep. In this vault:

```bash
cd ~/Documents/agent-vault

python3 scripts/vault-audit.py              # corpus health
python3 scripts/vault-audit.py --short      # one line per finding
python3 scripts/vault-audit.py --drift      # stale upstream versions (probe plan)
python3 scripts/vault-audit.py --drift --run-probes   # execute declared probes
```

| Health state | Meaning | Action |
|---|---|---|
| **Zombie** | Fails to load | Fix frontmatter first — it is silently absent |
| **Ghost** | Referenced but missing | Create it or repoint the reference |
| **Duplicate** | ≥85% description overlap | Merge or sharpen the boundary |
| **Hollow** | No procedure, references, or examples | Fill it or retire it |
| **Stale** | Dated grounding past threshold | Re-ground it |
| **Orphan** | Unlisted anywhere | Register or retire |
| **Statue** | Never invoked | Diagnose triggers before deleting |
| **Drift** | Upstream version moved past the snapshot | Re-ground, then bump version |

Full procedures: [`references/administer.md`](references/administer.md) and
[`references/drift.md`](references/drift.md).

## Non-goals (what the steward does not do)

- **Does not build nerd or forge shapes itself.** It routes those to `nerd-forge`
  and the family forges, because those own the anatomy.
- **Does not invent entities to satisfy a request.** "No" is a valid deliverable.
- **Does not delete.** Retirement is deprecation → unregister → delete after an
  audit cycle ([`references/update.md`](references/update.md#deprecation)).
- **Does not overwrite a registry unilaterally.** Registry changes are
  corpus-wide migrations and get their own change class.
- **Does not judge software design.** For that, `genie-doctrine` and the genie
  family own the lens.

## Rendered reference

Two self-contained HTML renderings live under `assets/`:

- [`assets/taxonomy-site/index.html`](assets/taxonomy-site/index.html) — the
  reference: taxonomy, layers, families, producer rule, health states, glossary.
- [`assets/situation-report/index.html`](assets/situation-report/index.html) —
  the dated snapshot: corpus counts, ownership buckets, Talos statuses, machine
  inventory and migration runbook.

Update the situation report at the end of each audit pass (the date and the
numbers are part of it), and keep both consistent with the registries. Publish
either with the `here-now` skill; the vault copy is the source of truth.

## Hand-offs

| Need | Use |
|---|---|
| Prompt vs skill vs agent echelon | `prompt-skill-agent-triage` |
| Turn an instruction into an artifact | `instruction-skill-forge` |
| Build a `*-nerd` | `nerd-forge` + `registries/_tech-nerd-pattern.md` |
| Build a `*-forge` | `registries/_forge-pattern.md` |
| Detect a forge opportunity | `forge-scout` |
| Climb one level deliberately | `registries/_meta-consultant-spawn.md` |
| Judge software change | `genie-doctrine` |
| Formal terms | [`references/glossary.md`](references/glossary.md) |
| The map of the corpus | [`references/org-chart.md`](references/org-chart.md) |
