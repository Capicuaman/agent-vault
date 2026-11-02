# Artifact Lenses

Each artifact teaches something the others cannot. Read them as a set, not as
substitutes. For each: what it reveals, how to get it, and what to look for.

## 1. Changelog / release notes

**Reveals:** the visible failure modes — what someone noticed, reproduced, and
shipped a fix for. The cheapest starting index.

**How to get it:** `CHANGELOG.md` in the repo; `npm view <pkg>` then
`npm pack <pkg>@<version>` and read `package/CHANGELOG.md`; GitHub Releases.

**Look for:** the *Fixed* section (the good stuff). *Changed* and *Removed* teach
interface evolution and cost. One-sentence footnotes are usually the deepest bugs.

## 2. PR discussion / commit message

**Reveals:** *why* this fix and not the obvious one. Rejected approaches,
reviewer pushback, the tradeoff accepted.

**How to get it:** `gh pr view <n> --comments`, `git log -p --follow <file>`,
`git show <sha>`. The PR body and review comments are the gold.

**Look for:** "we tried X but it broke Y", "this is a band-aid because Z", links
to related issues. A fix that chose *queueing* over *spawning more workers* is a
decision, not a fact.

## 3. The raw diff

**Reveals:** cost asymmetry. A one-line fix for a subtle, high-impact bug; a huge
fix for a tiny symptom. Calibrates your intuition about where complexity lives.

**How to get it:** `git show <sha>`, `gh pr diff <n>`, `git log -p`.

**Look for:** the ratio of diff size to symptom size, then ask why. Often the
small diff is a *constraint* finally respected (`rg --no-config`); the big diff is
state that should never have been owned.

## 4. Issue thread before the fix

**Reveals:** how bugs are actually *discovered* and reproduced — often more
instructive than the fix. Reproduction steps are a description of real behavior.

**How to get it:** `gh issue view <n> --comments`. Read oldest-to-newest.

**Look for:** the moment the reporter's mental model and the system's behavior
diverge. "Works on my machine" threads teach environmental complexity.

## 5. Design docs / RFCs / ADRs

**Reveals:** the model of the system *before* reality contradicted it. Changelogs
show the after; design docs show the intended before and the constraints the
authors believed they had.

**How to get it:** `docs/`, `rfcs/`, `adr/`, `design/` dirs; GitHub Discussions;
the PR that introduced a subsystem.

**Look for:** assumptions later falsified. Pair a design doc with the bug fixes
that followed. This is the best single way to learn *design judgment*.

## 6. Tests

**Reveals:** a specification of known fragility. Every "must not happen" test is a
scar — a bug real enough to encode.

**How to get it:** the test suite; `git log -p -- <test-file>`.

**Look for:** tests named after bugs, regression tests with issue numbers,
commented-out tests (abandoned battles), and what is *not* tested (blind spots).

## 7. Postmortems / incident reports

**Reveals:** highest signal-per-word in the field. Catastrophes are almost always
*interactions* between subsystems, not single bugs.

**How to get it:** Google SRE book; Dan Luu's postmortem collection; engineering
blogs of Cloudflare, AWS, GitHub, GitLab, Stripe, Meta.

**Look for:** the timeline, the contributing factors (plural), and what *detection*
looked like. Ask: what boundary was crossed, and what monitoring would have caught it?

## 8. `git log` / `blame` on one file

**Reveals:** where reality keeps pushing back. High churn = contested design or a
moving boundary. The stable core is equally informative.

**How to get it:** `git log --oneline --follow <file>`, `git blame <file>`,
`git log --stat --since=...`.

**Look for:** files with huge history (important or badly designed — decide
which) and files untouched for years (settled problems). Both are lessons.

## 9. CI config, dependency pins, packaging

**Reveals:** reproducibility and supply-chain lessons — the unglamorous work that
decides whether software works for anyone but the author.

**How to get it:** `.github/workflows/`, `Dockerfile`, `flake.nix`, lockfiles,
`package.json` engines/pins, install scripts.

**Look for:** pins vs ranges, cached artifacts, platform matrices.

## 10. Deprecations & breaking changes

**Reveals:** the long-term cost of getting an interface wrong. Interface design is
mostly learned from the pain of changing one.

**How to get it:** changelog *Breaking Changes* sections, deprecation warnings in
source, migration guides, semver history.

**Look for:** what changed, what was preserved for compatibility, and how long the
window was. Every migration guide is a postmortem of an API.

## Ordering heuristic

1. **Changelog** → pick a fix.
2. **Issue** → reconstruct the failure.
3. **Diff** → see the cost and the constraint.
4. **PR discussion** → see the rejected paths.
5. **Tests** → see what is now protected.
6. **Design doc** → see the assumption that failed.

Six artifacts, one fix, about twenty minutes. That is the highest-yield reading
session in software engineering.
