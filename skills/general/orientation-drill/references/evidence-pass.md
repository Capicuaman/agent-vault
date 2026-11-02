# Evidence Pass

Collect facts before forming any sentence. The order matters: repository state
first, then artifacts, then tools, then claims.

## 1. Repository truth

```bash
git fetch origin
git status --short --branch
git rev-list --left-right --count origin/main...HEAD   # behind / ahead
git log --oneline -8
git rev-parse --short origin/main
```

Reads as:

- **Clean + behind=0 ahead=0** → everything claimed is pushed; nothing new to commit.
- **Ahead>0** → there is unpushed work. Say so before anything else.
- **Dirty** → name the uncommitted paths; they are the most likely source of ambiguity.
- **Behind>0** → the local view of the work is stale; re-check before briefing.

Never assume "I committed it" means "it is pushed". Verify both.

## 2. What each commit actually did

```bash
git log --oneline -5
git show --stat --oneline <sha> | tail -n +2 | tail -5
git show --stat --oneline <sha> | head -1
```

For a rename, `git log --follow` and `git show --name-status` distinguish a rename
from a delete+add. A rename is an ambiguity event; record it.

## 3. Artifact existence

Check the concrete paths the summary claims, one by one:

```bash
for f in <claimed paths>; do [ -e "$f" ] && echo "OK $f" || echo "MISS $f"; done
```

Then check the inverse: does the **old** name still exist anywhere?

```bash
rg -l "<old-name>" . --glob '!.git'
```

A hit in a reference file means the docs are stale; a hit only in `.git` means the
history is correct and the tree is clean.

## 4. Tool-reported state

Prefer the project's own instrument over your reading of the files:

```bash
python3 scripts/vault-audit.py            # corpus health
python3 scripts/vault-audit.py --drift --run-probes
```

Record the **exit code** and the **findings separately**. They often disagree:
exit 0 can coexist with hollow and stale warnings.

## 5. Loader truth

A file that exists is not a file that loads. If the project has a loader, use it:

```bash
node -e "import('./dist/core/skills.js').then(m=>{const r=m.loadSkillsFromDir({dir:'<dir>',source:'user'});console.log(r.skills.length,r.diagnostics.length)})"
```

Count skills and diagnostics separately, and record the pair you measured.

**Never quote a remembered pair.** This document itself once said `49 / 0` and
`16 / 0`, and both were stale within a single commit. A number inside a skill
about staleness is still a number that can go stale — measure it.

## 6. Counts

```bash
grep -n "Total:" README.md
grep -n "## Skills (" MANIFEST.md
find skills -maxdepth 2 -mindepth 2 -type d | wc -l
```

Three numbers, three independent sources. If any disagree, that is a `count-drift`
finding, not a rounding error.

## 7. Claim extraction

Before checking anything, split the summary into atomic claims. One sentence can
contain three.

> "The audit now reports zero zombies, ghosts, duplicates, or orphans and exits 0."

Claims: (a) zero zombies; (b) zero ghosts; (c) zero duplicates; (d) zero orphans;
(e) exit code 0. Each gets its own row. A summary that is right about four and
wrong about one must not be graded as "true".

## 8. Evidence quality ladder

For each claim, record the *strongest* evidence you obtained:

| Level | Evidence | Verdict ceiling |
|---|---|---|
| 5 | Command output reproduced now | ✅ Verified |
| 4 | Current file contents | ✅ Verified (if the claim is about the file) |
| 3 | Git history | 🕰️ Historical at best |
| 2 | Your memory of doing it | ❓ Unverifiable |
| 1 | The summary itself | ❌ Not evidence |

Level 2 and below never produce ✅. If you only have memory, say "unverifiable"
and name the command that would settle it.

## Report shape

Keep the evidence pass **raw and short**. The user does not need the transcript;
they need the conclusions and the one command that proves each one.

```markdown
| Claim | Verdict | Evidence |
|---|---|---|
| 49 skills | ✅ | `find … | wc -l` → 49; README 49; MANIFEST 49 |
| pushed | ✅ | `status -sb` → `## main...origin/main`, ahead=0 |
```
