# forge-scout — Facts Snapshot

**Snapshot date:** 2026-10-07
**Sources (priority order):**
1. `~/.pi/agent/skills/registries/_forge-pattern.md` — canonical forge spec + forge registry.
2. `~/.pi/agent/skills/registries/_tech-nerd-pattern.md` — nerd registry + prompt-pattern registry + scope definitions.
3. On-disk `~/.pi/agent/skills/` + `~/Documents/textDump/.pi/skills/` folders.

Refresh by re-reading those files and running the corpus-wide scan in `patterns.md`.

---

## Canon (one paragraph)
Forge-scout is a **detector** skill. It watches the user's work for the signal that an artifact being produced should be forged (encoded into a reusable maker) instead of hand-rolled again. It applies the 5-signal forge-ripeness checklist, produces a forge-candidate card, and hands off to the appropriate forge or to the user. It is not a forge, not a nerd, and not a forge-nerd — it is the first skill in a new role: **scout**.

## Role taxonomy (where scouts fit)
| Role | Produces | Terminal climb? | Example |
|---|---|---|---|
| **nerd** | answers about one tech | no | `bilan-mx-nerd` |
| **forge** | artifacts to a spec | no | `nerd-forge` |
| **forge-nerd** | audits of a forge's corpus | yes (one per forge) | `nerd-forge-nerd` |
| **scout** | opportunity cards | yes (one per domain) | `forge-scout` (this skill) |

Scouts are orthogonal to the forge/nerd stack — they *watch* for openings to invoke makers. One scout per domain is enough; no scout-scouts.

## Current forge corpus (as of snapshot date)

| Forge | Scope | Output | Example | Forge-nerd? |
|---|---|---|---|---|
| `nerd-forge` | global | `*-nerd` skills | `bilan-mx-nerd` | ✅ `nerd-forge-nerd` |
| `worktree-drill-forge` | project (textDump) | drill packs | `herdr-ssh-worktree-pack.md` | ❌ |
| `prompt-pattern-forge` | global | `_<name>-pattern.md` | `_meta-consultant-spawn.md` | ❌ |

Scout can propose new forges; it must not propose duplicates of these three.

## The 5-signal forge-ripeness checklist
1. **Repeatable artifact shape** — can the output structure be described in one sentence?
2. **≥ 2 instances OR ≥ 2 named candidates** — scan on-disk corpus + session context.
3. **Explicit procedure** — the maker verb can be numbered as 5–9 steps.
4. **Observable quality variance** — existing instances differ in completeness/consistency.
5. **No existing forge covers it** — check `_forge-pattern.md` registry.

Thresholds:
- **5 of 5 → 🟢 forge now.**
- **4 of 5 → 🟡 draft spec, wait for the missing signal.**
- **≤ 3 → 🔴 not forge-shaped (yet). Explain which signals are missing.**

## Candidate forges (from `_forge-pattern.md`, with current evidence)

| Candidate | Signals passing | Reasoning |
|---|---|---|
| `drill-forge` | 1, 3, 5 (3/5) | 🟡 shape exists (worktree-drill-forge is one), but corpus = 1 drill, no quality variance to audit yet |
| `audit-forge` | 1, 3, 5 (3/5) | 🟡 `bilan-seo-conversion` writes dated audits, but only one shape so far — needs ≥ 2 audit types |
| `metaprompt-forge` | 1, 2, 5 (3/5) | 🟡 `01_PROJECTS/BILAN/METAPROMPTS/` has multiple instances; procedure not yet explicit |

**None currently 🟢.** All three are 🟡 — draft specs if the next instance appears.

## Known false-positive patterns (what scout learns NOT to flag)
- **Repeated inspections** (grepping, scanning, auditing) — these are actions, not artifact production.
- **One-off research tasks** that happen to resemble each other — need the "explicit procedure" signal, not just surface similarity.
- **Project-specific one-shots** — a scaffold used once for a single project doesn't become a forge until it's reused across projects.
- **Code refactors** — these produce code, not skills/docs. Different ecosystem.

## Scope boundaries
- Scout does NOT build forges. It cards them.
- Scout does NOT audit existing forges (that's a forge-nerd job).
- Scout does NOT maintain registries. Forges land in `_forge-pattern.md`; nerds in `_tech-nerd-pattern.md`; cards are session-ephemeral.
- Scout does NOT scout outside the pi-skills ecosystem (no scouting for business opportunities, code refactor opportunities, etc.). If that's needed, it's a different scout.

## Known failure modes
- **False positives from surface pattern-matching.** Mitigation: always run all 5 signals, not just signals 1–2.
- **Missed opportunities because the artifact is spoken-only** (user described the pattern in chat but no files exist). Mitigation: scan session context for "another X", "same as last time", "like we did with…".
- **Scope creep into forge-building.** Mitigation: hand-off section in SKILL.md is enforced; recommendation card always ends with a hand-off target.
