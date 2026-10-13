# forge-scout — Patterns Cheatsheet

Scouts have no CLI. This file is the reach-for toolkit: scans, heuristics, card templates, hand-off rules.

---

## Daily-entry patterns

### Corpus-wide suffix scan (where is the ecosystem clustering?)
```bash
ls ~/.pi/agent/skills/ ~/Documents/textDump/.pi/skills/ 2>/dev/null \
  | awk -F'-' '/-/{print $NF}' | sort | uniq -c | sort -rn
```
Suffixes like `nerd`, `forge`, `scout`, `pattern` are the role clusters. A cluster with ≥ 3 members + no forge for the shape = top candidate.

### Full forge + nerd inventory
```bash
for d in ~/.pi/agent/skills/*-forge ~/.pi/agent/skills/*-nerd ~/.pi/agent/skills/*-scout \
         ~/Documents/textDump/.pi/skills/*-forge ~/Documents/textDump/.pi/skills/*-nerd; do
  [ -d "$d" ] || continue
  echo "$d"
done
```

### Prompt-pattern inventory (count, to decide if a forge-nerd is warranted)
```bash
ls ~/.pi/agent/skills/_*-pattern.md 2>/dev/null | wc -l
```
≥ 4 prompt-pattern files + varying quality → recommend forging `prompt-pattern-forge-nerd`.

### Session-context scan (look for scout triggers in user prose)
Phrases to flag:
- "another X"
- "like we did with"
- "same shape as"
- "these keep coming out different"
- "I'm about to repeat myself"
- "haven't I done this before"

Each is a candidate signal 2 (≥ 2 instances or candidates).

---

## The 5-signal checklist (full form)

For every candidate, build this table and show it in the card:

| # | Signal | Pass? | Evidence |
|---|---|---|---|
| 1 | Repeatable artifact shape (one-sentence output structure) | ✅ / ❌ | describe or quote |
| 2 | ≥ 2 instances exist OR ≥ 2 named candidates | ✅ / ❌ | list file paths or candidate names |
| 3 | Explicit procedure (5–9 numbered steps possible) | ✅ / ❌ | sketch the steps |
| 4 | Observable quality variance across instances | ✅ / ❌ | name the delta |
| 5 | No existing forge covers it | ✅ / ❌ | check `_forge-pattern.md` registry |

### Score → recommendation mapping
| Score | Call |
|---|---|
| 5/5 | 🟢 **Forge now.** Hand off to the right maker (nerd-forge, prompt-pattern-forge, user). |
| 4/5 | 🟡 **Draft spec, wait.** Name the missing signal and the condition that satisfies it. |
| 3/5 or less | 🔴 **Not forge-shaped yet.** Explain which signals are missing and when to revisit. |

---

## Candidate-card template (always this format)

```markdown
### Forge candidate: `<proposed-name>-forge`

**Verb:** <scaffold / draft / generate / forge / produce / …>
**Output shape:** <file structure in one sentence>
**Existing instances:** <list file paths, or "0 — but N named candidates: …">
**Procedure sketch:**
1. <step>
2. <step>
...

**Design rules (specific to this forge):**
- <invariant>
- <invariant>

**Scope boundary (what this forge is NOT):** <hand-off candidates>

**Forge-ripeness score:** <X/5>
<the full checklist table>

**Recommendation:** <🟢 / 🟡 / 🔴> — <action>
**Hand off to:** <nerd-forge | prompt-pattern-forge | user | wait>
```

Every field required. "N/A" is a valid value but silence is not.

---

## Decision patterns

### Which forge is the right hand-off?
| If the artifact is… | Hand off to |
|---|---|
| A `*-nerd` skill | `nerd-forge` |
| A `_<name>-pattern.md` prompt pattern | `prompt-pattern-forge` |
| A drill pack / exercise | `worktree-drill-forge` (or recommend generalizing to `drill-forge`) |
| A new forge itself | **user** (no forge-forge exists; scout refuses to self-recurse) |
| An audit report | 🟡 candidate `audit-forge` doesn't exist yet; flag and ask |

### Second-time alarm (Move 1)
Fire when:
- The user asks you to produce something that matches an existing on-disk artifact's shape AND is not already covered by a forge.
- Open with: *"Scout check: this is instance #2 of a shape we've produced before. Want the candidate card now, or after instance #3?"*
- Don't lecture. Offer and move on if declined.

### Candidate-list reconciliation (Move 3)
Steps:
1. Read "Candidate forges" section from `~/.pi/agent/skills/registries/_forge-pattern.md`.
2. For each, apply the 5-signal checklist with current evidence (file listings + session context).
3. Produce a ranked table: candidate → score → recommendation.
4. Highlight any that changed status since last scan (would need a history file; currently session-ephemeral).

---

## Anti-patterns (what scout refuses to do)

- Flag an action as a forge opportunity (actions aren't artifacts).
- Propose a forge that duplicates one in `_forge-pattern.md` registry.
- Produce a card without the full 5-signal table.
- Build the forge instead of handing off.
- Scout other scouts (no `scout-scout`, terminal climb).
- Flag session-only shapes (patterns that happened once in chat with no file produced) without saying so explicitly.

---

## Escape hatches

- Candidate is borderline (3.5/5) → produce the card, mark it 🟡, and name the one signal that would flip it.
- No existing forge covers the shape AND the user wants to build one → hand off to the user with a complete procedure sketch; do not forge yourself.
- Scope is unclear → ask one sharpening question before running the checklist. Not more.
- Shape is actually a pattern (recurring prose move), not an artifact (file) → hand off to `prompt-pattern-forge` instead.

---

## The authority ladder
1. On-disk `*-forge` / `*-nerd` folders (reality).
2. `_forge-pattern.md` spec + registry.
3. `_tech-nerd-pattern.md` registry.
4. `references/facts.md` snapshot in this skill.
5. Session context (user prose).
6. Training-data guesses — **never**.
