# Commit Messages, PR Bodies, Changelog Entries

## Commit message

### Structure

```text
<subsystem>: <imperative change in the present tense, <= 72 chars>

<Why the change was needed. What was false before. What the alternative was
and why it was rejected. Wrap at 72. This paragraph is what `git blame` shows
a future reader, so it must stand alone without the PR.>

<Optional: the constraint that forced this shape, or a follow-up that is
deliberately out of scope.>
```

### Good

```text
grep: run rg with --no-config

RIPGREP_CONFIG_PATH let users' ambient ripgrep config change the tool's
semantics: a `--fixed-strings` entry silently turned regex searches into
literal ones, with no error. Ambient config that changes meaning is worse
than a missing feature, so the tool now opts out of user config entirely.

Callers who relied on their own rg config can pass the flags explicitly.
```

Why it works: names the symptom class, states the failed assumption (ambient
config is safe), names the boundary (environment), and says what it gave up.

### Bad

```text
fix grep issue
```

Fails retrievability (no symptom), transferability (no lesson), and bisect (no
scope).

### The subject line

- Imperative mood: "fix", not "fixed" or "fixes".
- Name the subsystem first: `grep:`, `compaction:`, `auth:`.
- The subject should describe the *behavior change*, not the code motion.
- Never end with a period. Never exceed ~72 characters.

## PR body

### Skeleton

```markdown
## Problem

<User-visible symptom, verbatim error text, and who is affected.>

Closes #1234.

## Why now

<Severity, frequency, or the thing that made this worth doing.>

## Approach

<The change in one paragraph. What invariant it restores or establishes.>

## Alternatives considered

- **<Option A>** — rejected because <reason>.
- **<Option B>** — rejected because <reason>.

## Risk

<What could break, who depends on the old behavior, and how it is mitigated.>

## Verification

<Positive check with command and output. Screenshots or logs for UI.>

## Rollback

<How to revert safely, including any data or config migration.>
```

### Notes

- **Problem before solution.** Reviewers need the failure model before the diff.
- **Alternatives are not optional.** A PR that considered nothing is a PR that
  has not been thought about. This section is the highest-value part for future
  readers.
- **Risk section drives review depth.** "No risk" is almost always false.
- **Verification must be positive.** "Tests pass" is weak; "ran `tool --version`
  and it printed 1.4.0" is strong.
- **Attach evidence, do not describe it.** Paste the actual output.

## Changelog entry

### Structure

```markdown
- Fixed <user-visible symptom> when <condition> (<#issue>)
- Changed <default/behavior> from <old> to <new> (<#issue>)
- Removed <thing>, which <what it was> (<#issue>)
```

### Rules

1. **Symptom first.** The user is searching for what they saw, not what you did.
2. **Quote the error** when the error is the symptom.
3. **Name the version.** In a sectioned changelog the heading does this; in a
   flat one, say it.
4. **Link the issue or PR.** One link, not three.
5. **Credit contributors** for external reports, per project convention.
6. **Group by user concern**, not by file: Fixed / Changed / Added / Removed /
   Breaking Changes.
7. **Never describe internal refactors** in a user-facing changelog.
8. **Say what the user must do** if anything (migration, config change,
   re-login).

### Good

```markdown
### Fixed

- Fixed `grep` following `RIPGREP_CONFIG_PATH`, where options such as
  `--fixed-strings` silently changed regex searches into literal ones. The tool
  now runs `rg --no-config` (#11203).
```

Why it works: a user who saw "my regex is broken" will find it; the mechanism is
secondary; the fix is stated as a behavior.

### Bad

```markdown
- Refactored the grep tool to pass --no-config to the subprocess
```

Describes the implementation. Unfindable by a user.

## Breaking changes

A breaking change entry needs three things beyond a normal entry:

1. **What changes**, concretely — old vs new.
2. **What the user must do** — the migration step, with a command if possible.
3. **Why it was necessary**, and what was preserved for compatibility.

```markdown
### Breaking Changes

- Changed the theme schema URL to `https://pi.dev/schemas/theme.schema.json` and
  added validation at startup. Themes with an old `$schema` value still load, but
  editors will not validate them until the URL is updated. Unsupported metadata
  keys are now removed from the theme at load time; move them under `vars`.
```

## Responding to review

- Reply to the **concern**, not the line.
- If you disagree, state the constraint you are optimizing for; do not just repeat
  the original rationale.
- If a comment reveals a wrong assumption, say so — it is the same failed-assumption
  discipline as a bugfix note.
- Resolve only after the change is pushed or the thread reaches a decision.
