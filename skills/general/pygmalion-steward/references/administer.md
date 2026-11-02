# Administer

Keeping the corpus coherent. Administration is maintenance, not filing.

## Source of truth

```
agent-vault/skills/<category>/<name>/     ← canonical source
        ↓ vault-install.sh (copies flat)
~/.pi/agent/skills/<name>/                ← global install
```

Rules:

- **The vault is canonical.** Edit in the vault, install outward. Editing an
  installed copy creates a fork that the next `vault-sync.sh --install` overwrites.
- **The installer is flat.** Each skill is copied to `~/.pi/agent/skills/<name>/`.
  Therefore a skill must never depend on a sibling directory *outside* its own
  folder unless that sibling is also a skill at the same level. This is why the
  genies' shared lens is a real skill (`genie-doctrine`) rather than a `_doctrine/`
  folder: `../genie-doctrine/references/` survives a flat install, `../_doctrine/`
  does not.
- **Scope is identity.** A global entity must not cite project-local docs. If it
  does, either move it to project scope or re-ground it.
- **Every instance clone must be discoverable.** Note the vault may live at a
  different path per machine (here: `~/remote-manjaro/Documents/agent-vault`, an
  SSHFS mount; elsewhere: `~/Documents/agent-vault`). Scripts that hardcode the
  path break silently on the other machine — check before trusting them.

## Talos — installed-copy drift

The vault is the source of truth; installed skills are a **cache**. **Talos** is
the guard that walks the perimeter: it compares every vault skill against every
install root by content hash.

Named for the bronze automaton that patrolled Crete — he did not build, decide, or
judge. He noticed when something inside the walls was wrong.

```bash
python3 scripts/vault-audit.py --installed
python3 scripts/vault-audit.py --installed --repair            # fix drifted copies
python3 scripts/vault-audit.py --installed --repair-missing    # also install absent ones
```

Roots default to `~/.agents/skills` and `~/.pi/agent/skills`. Override with
`--install-roots DIR...` or `$PI_SKILLS_DIRS` (a path-separator list). Nested
layouts (`<root>/<category>/<name>`) are found as well as flat ones.

| Status | Meaning | Action |
|---|---|---|
| `ok` | identical to the vault | none |
| `linked` | symlink whose target matches | none |
| `drift` | exists and differs | `--repair` |
| `diverged` | holds files the vault does not | human decision; `--force` replaces |
| `missing` | not installed on this machine | a choice, not an error |
| `unmanaged` | installed, not from the vault | informational |

**The superset guard.** Talos refuses to repair a copy that contains files the
vault does not have. A local checkout of the full upstream project (a 2 MB repo
installed beside a 20 KB skill) is a *fork*, not a stale copy — replacing it would
destroy work. It is reported as `diverged` and needs `--force`.

**Semantics that matter across machines.** A missing skill is not drift. Each
machine installs a subset; only an *existing but wrong* copy is an error. This is
why Talos exits 1 on drift and 0 on missing.

### Keeping machines in step

```
this machine          git                other machine
──────────────────────────────────────────────────────────
edit vault   ──push──▶  GitHub  ──pull──▶  vault clone
                                              │
                                     talos --installed
                                              │
                                    --repair if drifted
```

Talos owns the last mile. Git owns distribution.

## Registries of record

Registry coverage in this vault is **partial by design**:

| Family | Registry of record |
|---|---|
| nerds, forges, scouts | `registries/_tech-nerd-pattern.md`, `registries/_forge-pattern.md` |
| everything else | `README.md` category tables + `MANIFEST.md` |

The audit reconciles both. When coverage becomes painful, the fix is a single
generated index — but do not hand-maintain a third copy in the meantime.

**Registry discipline**

- Every entity appears in exactly one registry of record.
- The registry is the spec; the forge is the executable. When they disagree, the
  registry wins and the forge is corrected.
- Candidate lists are not entries. Naming an entity you have not built is
  planning; the audit ignores candidate sections on purpose.

## The seven health states

Run `python3 scripts/vault-audit.py`. Then work in this order.

### 1. Zombie — fails to load

**Symptom:** the skill is absent from sessions; no error surfaced to the user.
**Causes:** YAML parse error (most often nested double quotes), missing
description, `name` ≠ directory, description > 1024 chars, invalid name format.
**Fix:** correct the frontmatter, then re-run the audit. Never "fix" it by
renaming the directory unless you also update the registry.

**Real case:** `bonanno-game-theory` had
`description: "Knowledge base from "Game Theory: ..." by ..."`. The parser failed,
and the skill was silently dead. Cost: invisible. Fix: one quoting change.

### 2. Ghost — referenced but missing

**Symptom:** an entity hands off to something that does not exist.
**Causes:** a skill was renamed or never built; a planner wrote the future tense.
**Fix:** build it, or rewrite the reference to a real owner. Prefer building only
if the reference is load-bearing.

**Real cases (both since fixed):** `skill-maker`, referenced by
`instruction-skill-forge` but never built — the reference was repointed to
`pygmalion-steward`. And `herdr-mission-control-app`, which was never a skill at
all but a project path written in backticks; the correct fix was punctuation, not
creation. The audit cannot tell a backticked path from a backticked name, so the
Steward must.

**Lesson:** a Ghost is a claim about existence. Before building the missing thing,
check whether the reference meant an Entity or a path.

### 3. Duplicate — overlapping triggers

**Symptom:** two entities compete; both fire unreliably.
**Detection:** description similarity ≥ 85%.
**Fix:** merge, or sharpen the boundary. Do **not** keep both and hope routing
sorts it out — the model will pick arbitrarily.

### 4. Hollow — claims without substance

**Symptom:** `SKILL.md` with no numbered procedure, no `references/`, no
`examples/`, and little body text.
**Fix:** fill it within one session, or delete it. A hollow entity costs context
and returns nothing.

### 5. Stale — grounding has aged out

**Symptom:** a dated snapshot or reference is older than the threshold
(default 180 days).
**Fix:** re-ground it (refresh the snapshot, re-verify commands), or explicitly
mark it as historical if the technology is frozen.

### 6. Orphan — invisible to the catalog

**Symptom:** the directory exists, but no registry or README lists it.
**Fix:** register it, or retire it. An orphan is invisible to the next audit and
to every human browsing the vault.

### 7. Statue — never invoked

**Symptom:** no evidence the entity ever fires: no log, no session mention, no
downstream artifact.
**Fix:** diagnose the trigger first — the description is usually the problem, not
the content. Only retire after the trigger test fails twice.

## Split, merge, retire

### Split when
- Description needs more than ~3 distinct situations to route correctly, **or**
- The procedure has two independent stopping conditions, **or**
- Body exceeds roughly 300 lines and the sections do not reference each other.

Split along the *routing* boundary, not the file boundary: each child must own a
distinct set of must-fire utterances.

### Merge when
- Description similarity ≥ 85%, **or**
- The same user request would reasonably match both, **or**
- One entity's hand-off to the other accounts for most of its value.

Merge into the one with the better description; delete the other and leave a
redirect line in the registry.

### Retire when
- The statue diagnosis failed twice (triggers are fine, still no use), **or**
- A successor supersedes it, **or**
- The underlying technology or project is gone.

Retirement is a two-step operation, not a delete: see
[`update.md`](update.md#deprecation).

## Count hygiene

`README.md` and `MANIFEST.md` both claim totals. They drift the moment someone
adds a skill without updating them — this vault had drifted to 40 claimed / 42
actual before the genies were added.

The audit's `count-drift` check exists for this. When you add or remove an entity,
update in the **same commit**:

1. The category table row in `README.md`
2. The category section list (if it exists)
3. The total in `README.md`
4. The total and section in `MANIFEST.md`
5. The installer's category counts in `scripts/vault-install.sh`

## Cadence

| When | What |
|---|---|
| **Every change** | Run the audit; fix any new zombie/ghost/duplicate/orphan |
| **After a `git pull`** | `--installed`, then `--repair` if it reports drift |
| **Weekly (10 min)** | `--short` audit + `--installed`; clear new findings |
| **Monthly (45 min)** | Full audit; review statues; split/merge decisions; count hygiene |
| **On upstream change** | Re-ground affected entities; see [`update.md`](update.md) |

## Administering a corpus you did not build

1. Run the audit. Trust it over your impression of the files.
2. Fix load failures first (zombies), then routing conflicts (duplicates, ghosts).
3. Only then evaluate content quality.
4. Record decisions in the registry or catalog — an undocumented decision is
   indistinguishable from an accident.
