# nerd-forge-nerd — Patterns Cheatsheet

The nerd-forge-nerd has no CLI. This file is its reach-for toolkit: corpus audits, split/merge calls, template evolution, registry sync, teaching moves.

---

## Daily-entry patterns

### Full corpus scan (always start here)
```bash
# Every *-nerd and *-forge on disk, with reference-file completeness
for d in ~/.pi/agent/skills/*-nerd ~/.pi/agent/skills/*-forge ~/.pi/agent/skills/nerd-forge ~/Documents/textDump/.pi/skills/*-nerd ~/Documents/textDump/.pi/skills/*-forge; do
  [ -d "$d" ] || continue
  echo "## $d"
  find "$d" -maxdepth 2 -type f -printf "  %6s  %p\n"
done
```
This is the ground truth. Anything in `facts.md` that disagrees with this scan is stale — update `facts.md`.

### Verify both pattern-doc registries exist and are current
```bash
for p in ~/.pi/agent/skills/registries/_tech-nerd-pattern.md \
         ~/Documents/textDump/.pi/skills/registries/_tech-nerd-pattern.md; do
  echo "## $p"
  grep -E "^- \`[a-z0-9.-]+-nerd\`|^- \`[a-z0-9.-]+-forge\`" "$p" 2>/dev/null
done
```
Cross-check: every nerd on disk should appear in exactly one registry (the one matching its install location).

### YAML sanity across the corpus (catches the loader-crash bug)
```bash
for f in ~/.pi/agent/skills/*/SKILL.md ~/Documents/textDump/.pi/skills/*/SKILL.md; do
  desc=$(awk '/^description:/,/^[a-z]+:/' "$f" | head -1)
  case "$desc" in
    *': "'*) ;;  # quoted — fine
    *"description: \""*) ;;
    *) echo "⚠️  unquoted description: $f" ;;
  esac
done
```

### Zero-byte / empty-reference detection
```bash
find ~/.pi/agent/skills ~/Documents/textDump/.pi/skills -name "*.md" -size 0 2>/dev/null
```
A 0-byte file = parallel `write` race during a forge run. Rerun the forge serially.

---

## Audit patterns

### Score a single nerd against the six design rules
Open `<nerd>/SKILL.md` and check:

| # | Rule | Pass criterion |
|---|---|---|
| 1 | Grounded over clever | Posture section names a priority chain ending at local docs or `--help`. |
| 2 | Composition over replacement | "When to hand off" section names ≥ 2 sibling skills. |
| 3 | Kindly corrective | "Anti-patterns" / "misconceptions" section exists with ≥ 2 entries. |
| 4 | Snapshot-honest | `facts.md` has a dated top line; SKILL.md mentions refresh via `graphify_add`. |
| 5 | One tech, one nerd | Description names a single product/tech, not a category. |
| 6 | Trigger-rich description | ≥ 5 real triggers (concepts, commands, phrasings) in the `description:` field. |

Produce a `rule · pass/fail · evidence` table. A nerd failing ≥ 2 rules needs remediation.

### Spec-drift report (compare a nerd to `nerd-forge` canonical anatomy)
```bash
nerd=~/.pi/agent/skills/<thing>-nerd
test -f "$nerd/SKILL.md" && echo "SKILL.md ✅" || echo "SKILL.md ❌"
test -f "$nerd/references/facts.md" && echo "facts.md ✅" || echo "facts.md ❌"
ls "$nerd/references/"commands.md "$nerd/references/"patterns.md 2>/dev/null | head -1 \
  && echo "commands.md or patterns.md ✅" || echo "neither commands.md nor patterns.md ❌"
```
Known violator at snapshot date: `homeassistant-nerd` (no `references/` at all).

### Global-leak audit (project-local paths in a global nerd)
```bash
grep -rE "~/Documents/|/home/[^/]+/Documents/" ~/.pi/agent/skills/*/
```
Any hit in a global nerd = promotion was sloppy. Either fix the paths or demote the nerd.

---

## Decision patterns

### Should this be a new nerd, an extension, or nothing?

| Signal | Call |
|---|---|
| User asks about tech with no existing nerd AND tech has ≥ 1 reference URL AND user hits it ≥ 2x/month | **new nerd** → invoke `nerd-forge` |
| User asks about one deep aspect of a tech that already has a nerd | **extend existing** → add a reference file (e.g. `plugins.md`, `compare.md`, like herdr-nerd did) |
| User asks a one-off question | **no nerd** → answer in-line, don't forge |
| Tech is a category ("JS frameworks") | **no nerd** → split into per-member nerds or decline |
| Idea is "a nerd about my nerds" | **forge-nerd** → that's this skill, already built |

### Split-or-stay heuristic for a growing nerd
A nerd should split when:
- Its SKILL.md crosses ~400 lines, OR
- Its `references/` has > 5 files, OR
- Two distinct user-question-clusters emerge that need different source priorities.

Precedent: `herdr-nerd` is at 5 reference files. Still coherent. If a 6th cluster appears (e.g. "herdr plugin development"), split off a `herdr-plugins-nerd`.

### Promote-or-demote heuristic
- **Project → global** when: ≥ 2 projects would use it AND references are URL-anchored (no repo-local paths).
- **Global → project** when: references drift toward a single repo's layout AND no other project calls it.
- Always leave a `.<name>.moved-to-<location>` marker in the old location (precedent: `.nerd-forge.moved-to-global`).

---

## Signature nerd-forge-nerd moves

### Move 1 — Audit-on-demand
When asked "is `<x>-nerd` any good?", produce:
1. The 6-rule score table.
2. The spec-drift checklist.
3. One concrete remediation PR-sized diff.
Lead the report with the single most-impactful fix.

### Move 2 — Corpus-wide health snapshot
When asked "how are my nerds doing?", run the full corpus scan + yaml sanity + global-leak audit, then present:
- Count of nerds (global vs project).
- Spec violations (named).
- Candidate nerds overdue for forging (pulled from the pattern doc).
- Pattern-doc drift (registered vs on-disk).

### Move 3 — Registry sync
Keep both `_tech-nerd-pattern.md` registries honest. After any new nerd is forged, verify it's listed in the registry matching its location — only that one, never both.

### Move 4 — Template evolution proposal
When you spot a recurring pattern across ≥ 3 nerds that `nerd-forge` doesn't yet encode (e.g. "every website-nerd ends up needing a `curl -sI` pattern block"), propose a template amendment: open `nerd-forge/SKILL.md`, draft the new section, present it as a diff for approval before applying.

### Move 5 — Teach the pattern
First-time nerd authors get a 4-step walkthrough:
1. Point at `~/.pi/agent/skills/nerd-forge/SKILL.md` (the spec).
2. Point at `bilan-mx-nerd` or `laya-nerd` (clean 3-file exemplar).
3. Point at `herdr-nerd` (elaborate exemplar — shows reference-file extensibility).
4. Invoke `nerd-forge` to do the actual build.

### Move 6 — Recursion guard
If a user asks for a "nerd-forge-nerd-nerd" or "meta-meta" skill, politely refuse and explain: this nerd is already the terminal climb (one level above the forge). Climbing further produces no new value — the forge-nerd already audits itself when it audits the forge.

---

## Anti-patterns

- Letting the pattern docs drift from the on-disk reality.
- Forging a nerd for a tech that has only been asked about once.
- Backfilling `references/` for a dead nerd (retire it instead).
- Scoring a nerd without quoting the exact SKILL.md evidence.
- Spawning a second forge-nerd (one is terminal).

---

## Escape hatches

- Nerd is incoherent and remediation would be larger than a rebuild → retire + re-forge.
- Pattern-doc registries disagree AND disk is inconclusive → treat disk as source of truth, rewrite both docs from the scan output.
- `nerd-forge` itself has drifted from a learned best practice → propose amendment (Move 4), don't fork the forge.

## The authority ladder
1. On-disk `*-nerd` / `*-forge` folders (reality).
2. `nerd-forge/SKILL.md` (spec).
3. `_tech-nerd-pattern.md` docs (registries).
4. `references/facts.md` in this skill (snapshot).
5. Training-data guesses — **never**.
