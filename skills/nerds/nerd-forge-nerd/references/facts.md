# nerd-forge-nerd — Facts Snapshot

**Snapshot date:** 2026-10-07
**Sources (priority order):**
1. `~/.pi/agent/skills/nerd-forge/SKILL.md` — the factory spec (authoritative procedure).
2. `~/.pi/agent/skills/registries/_tech-nerd-pattern.md` — global pattern doc.
3. `~/Documents/textDump/.pi/skills/registries/_tech-nerd-pattern.md` — project pattern doc.
4. Every existing `*-nerd` and `*-forge` skill on disk (the empirical corpus).

Treat as snapshot. Re-audit by running the "corpus scan" pattern in `patterns.md`.

---

## Canon (one paragraph)
A `*-nerd` is a reusable persona skill that makes future pi sessions a grounded, enthusiastic, slightly obsessive expert on **exactly one** technology — grounded on local docs → captured snapshot → live site → `--help`, in that priority order. A `*-forge` is a meta-skill that **produces** other skills to a spec. `nerd-forge` is the forge that produces `*-nerd` skills. `nerd-forge-nerd` (this skill) is the **consulting expert on the forge pattern and the existing nerd corpus** — it audits, splits, merges, evolves the template, keeps the two pattern docs in sync, and decides whether a new idea deserves a nerd, an extension of an existing nerd, or no nerd at all.

## The three-tier taxonomy
| Tier | What it is | Produces | Example |
|---|---|---|---|
| **nerd** | grounded expert on one tech | answers | `bilan-mx-nerd`, `herdr-nerd` |
| **forge** | meta-skill producing other skills to a spec | skills | `nerd-forge`, `worktree-drill-forge` |
| **forge-nerd** | expert on a forge pattern + its corpus | audits / designs / critiques | `nerd-forge-nerd` (this one) |

The forge-nerd tier is **recursive-safe**: it does not spawn more forge-nerds. One per forge is enough.

## Canonical anatomy of a `*-nerd`
```
<skill-root>/<thing>-nerd/
  SKILL.md                 # persona + triggers + procedure
  references/
    facts.md               # one-paragraph canon + facts table + snapshot date
    commands.md            # cheatsheet (if the thing has a CLI/API)
    patterns.md            # replaces commands.md if no CLI
```

**Spec deviations are allowed when earned.** `herdr-nerd` has 5 reference files (facts, commands, compare, plugins, blog-notes). That's fine — scope demands it. `homeassistant-nerd` has only SKILL.md and no `references/` — that is **not** fine; it's a spec violation that should be remediated or justified.

## Install locations
| Location | Use when |
|---|---|
| `~/.pi/agent/skills/<name>/` (global) | the nerd/forge is useful across every project |
| `<project>/.pi/skills/<name>/` (project) | references cite project-local paths; or the tech only matters in that project |

**Promotion is a real motion.** `nerd-forge` lived at `~/Documents/textDump/.pi/skills/nerd-forge/` and was promoted to global, leaving a `.nerd-forge.moved-to-global` marker. When you promote, strip project-local path references from `facts.md`/`patterns.md` first — the global version must be self-contained.

## Current nerd corpus (as of snapshot date)

| Nerd | Location | Reference files | Health |
|---|---|---|---|
| `nerd-forge` | global | SKILL only | ✅ spec-compliant (factories are allowed SKILL-only) |
| `nerd-forge-nerd` | global | SKILL + facts + patterns | ✅ (this skill) |
| `herdr-nerd` | project (textDump) | facts, commands, compare, plugins, blog-notes | ✅ elaborate exemplar |
| `laya-nerd` | project (textDump) | facts, patterns | ✅ clean 3-file |
| `bilan-mx-nerd` | global | facts, patterns | ✅ clean 3-file |
| `homeassistant-nerd` | global | **none** | ⚠️ missing `references/` — spec violation |
| `worktree-drill-forge` | project (textDump) | examples/ | separate category (forge, not nerd) |

## Pattern-doc inventory
| Path | Scope |
|---|---|
| `~/.pi/agent/skills/registries/_tech-nerd-pattern.md` | global corpus registry |
| `~/Documents/textDump/.pi/skills/registries/_tech-nerd-pattern.md` | project corpus registry |

Both exist and both must list the nerds they host. Project doc should NOT list global nerds (and vice versa) — each is a registry for its own install location. When auditing, confirm every nerd on disk appears in exactly one doc.

## Candidate-nerd list (from global pattern doc)
`astro-nerd`, `bun-nerd`, `nix-nerd`, `pi-nerd`, `graphify-nerd`, `tailwind-nerd`, `jekyll-nerd`, `remotion-nerd`, `tailscale-nerd`. The forge-nerd's job is to decide which graduate from candidate → built, and in what order.

## The six nerd-forge design rules (from `nerd-forge/SKILL.md`)
1. **Grounded over clever.** Cite source always.
2. **Composition over replacement.** Suggest combining, never replacing.
3. **Kindly corrective.** Correct misconceptions with sources.
4. **Snapshot-honest.** Every `facts.md` is dated; "latest" questions refresh via `graphify_add`.
5. **One tech, one nerd.** Resist scope creep.
6. **Activation description is trigger-rich.** The `description:` field is the only hook pi uses to load the skill.

A nerd-forge-nerd audit scores every nerd against these six.

## Known failure modes in the corpus (learnings)
- **Missing `references/`** (homeassistant-nerd). Fix: run `nerd-forge` in audit mode on that nerd and backfill `facts.md`/`commands.md`.
- **YAML `description:` without quotes** when it contains `:` or `#`. Known pi-skill-loader crash. `nerd-forge` Step 6 enforces quoting.
- **Parallel `write` calls to a new skill folder** → 0-byte files. `nerd-forge` Step 7 enforces serial writes.
- **Project-local path leakage into a global nerd.** Rule: a nerd in `~/.pi/agent/skills/` must cite URLs or `~`-anchored paths, not `~/Documents/<repo>/...`.
- **Pattern-doc drift.** The two `_tech-nerd-pattern.md` registries are maintained by hand and get out of sync. Sync is part of this nerd's job.

## Scope boundaries (what this nerd will NOT do)
- Will **not** create new nerds (that's `nerd-forge` — this nerd *instructs* you to invoke it).
- Will **not** act as a tech expert itself. If you ask `nerd-forge-nerd` about Home Assistant, it will hand you off to `homeassistant-nerd` and (if asked) audit that nerd for compliance.
- Will **not** be a general skill-design philosopher. Its surface is the `*-nerd` / `*-forge` family specifically.
