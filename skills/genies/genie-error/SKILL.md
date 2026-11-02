---
name: genie-error
description: Capture, fingerprint, triage, and write up errors into the error-notes library at ~/Documents/textDump/03_RESOURCES/Software_Engineering/error-notes. Use when a command fails, when the user pastes an error or stack trace, when they ask why something is not working, when they want to write or update an error entry, or when they want to review recurring errors and promote them into guardrails.
metadata:
  family: genies
  version: 2.0.0
---

# genie-error

**Go meta into your own errors.** An error is not an event to dismiss; it is a
claim about the world that was false, plus evidence about where the falsehood
lives.

This skill operates the existing error-notes system. The system's `README.md` is
the authoritative contract — read it before changing anything:

```
~/Documents/textDump/03_RESOURCES/Software_Engineering/error-notes/README.md
```

Override the root with `$ERRL_HOME` if it ever moves.

## When to use this skill

- A command just failed and you want it recorded.
- The user pastes an error or stack trace and asks what it means.
- The user wants an entry written, updated, or reviewed.
- The user wants to find recurring errors and turn them into guardrails.
- The user asks "why is this not working" and the cause is non-obvious.

Use `genie-read` for **other people's** fixes, `genie-review` for a pending diff,
and `genie-write` for the prose that accompanies a fix you ship.

## What earns an entry

Write an entry when **any** of these is true:

- it cost more than ~5 minutes, or
- the cause was non-obvious, or
- it is likely to recur (same tool, same environment), or
- it revealed a wrong assumption (docs drift, misleading message, hidden state), or
- it teaches a pattern that transfers to other tools.

**Do not** write entries for typos the message already pinpoints, one-off network
blips you fully understand, or failures you deliberately caused while testing.

The goal is a library of *patterns*, not a diary. Ten good entries beat two
hundred transcribed stack traces.

## Workflow

### 1. Capture

Preferred, non-TUI commands:

```sh
source ~/Documents/textDump/03_RESOURCES/Software_Engineering/error-notes/tools/capture.sh
ecap some-command --flag
```

`ecap` preserves the exit code and, on non-zero, calls `errlog.py add`, which
appends to `index.jsonl` and stubs an entry if the fingerprint is new.

For **TUI or full-screen programs**, `ecap` will break them (it redirects stderr
to a temp file). Use the tee form instead:

```sh
some-tui-command 2>&1 | tee /tmp/err.log
errlog.py add --cmd "some-tui-command" --rc "${PIPESTATUS[0]}" --stderr-file /tmp/err.log
```

### 2. Triage

Follow the diagnostic moves in [`references/diagnostic-moves.md`](references/diagnostic-moves.md).
The order that pays off fastest:

1. Split the message into **claim + remedy**; verify both.
2. Read the stack **top-down** — the top frame is the decision that rejected you.
3. **Locate the throw site**: grep the literal message in the installed package.
4. **Dump the state** the code consults (registry, config, directory listing).
5. **Check version drift** early: `tool --version`, `npm view <pkg> dist-tags`.
6. **Reduce to one command.**

Trust artifacts over docs. Docs describe intent; the installed version describes
reality.

### 3. Fix and verify

Apply the smallest change that removes the cause. Record the workaround
separately from the fix. Then **verify positively**: the operation now succeeds —
not merely "no error appeared".

### 4. Write the entry

Fill the stub within 24 hours, while the failed assumption is still fresh.

The entry contract is fixed: YAML frontmatter plus eleven H2 sections, in order,
names and numbers unchanged (it is a parser contract). See
[`references/entry-contract.md`](references/entry-contract.md) for the field
dictionary and section guidance.

The two sections that make an entry worth keeping:

- **`failed_assumption`** — the belief that made the error surprising. This is
  what compounds.
- **`## 10. Transferable lesson`** — the rule with no project nouns.

### 5. Classify

Set `category` to one of the error families (`precondition`, `registry`,
`config`, `dependency`, `permission`, `network`, `resource`, `type/schema`,
`build`, `logic`, `environment`).

Also map the entry to a **boundary** from
[`../genie-doctrine/references/boundaries.md`](../genie-doctrine/references/boundaries.md) in `tags`. That is the
bridge to the rest of the genie family: error families say *where it broke*,
boundaries say *why it was hard*.

### 6. Review

Weekly (15 minutes):

1. `errlog.py list` — what repeated?
2. Take the top entry: does its transferable lesson still hold?
3. Did any fix regress? Add the date to the triage log.
4. **Promote one pattern into a guardrail** — alias, preflight check, checklist
   line, or upstream bug report.
5. Delete entries that taught nothing (keep the index line).

The system is working when you recognize an error before you finish reading it,
because you have seen its fingerprint.

## Rules that are easy to violate

- **One fingerprint per entry.** Identical fingerprints are the same error
  recurring. Bump `index.jsonl`; do not create a new entry.
- **IDs are immutable.** Use `supersedes: ERR-...` if an entry is replaced.
- **Verbatim evidence is sacred.** Never paraphrase an error message or stack
  frame; put interpretation in the prose sections.
- **Mark confidence.** `verified` (reproduced and cause proven), `probable`
  (strong evidence, one gap), `hypothesis` (best current theory).
- **Redact before saving.** Keys, tokens, passwords, private URLs. Best-effort
  only — do not pipe production credentials through it.
- **Filenames are cosmetic.** Entries are discovered by the `fingerprint:` field.

## Known gaps in the tooling

Flag these; do not silently "fix" them, because changing normalization changes
fingerprints and orphans existing entries.

1. **`ERROR_LINE` misses `tool: message` formats.** A line like
   `dsh: pnpm was not found` does not match the error regex, so `error_type`
   falls back to `"output"`. This is visible in `ERR-2026-11-02-002` and `-003`.
   Consequence: weaker fingerprints and less precise recurrence detection. A fix
   needs a deliberate re-fingerprint migration.
2. **`ecap` breaks TUIs.** Documented in `capture.sh`; use the tee form.
3. **Entry numbering counts files for the date.** Deleting an entry can cause an
   ID to be reused later the same day.
4. **`find_entry` scans every entry** on each `add`. Fine at personal scale;
   an index lookup would be needed beyond a few hundred.

## Bundled references

- [`references/diagnostic-moves.md`](references/diagnostic-moves.md) — the diagnostic playbook with concrete commands
- [`references/entry-contract.md`](references/entry-contract.md) — field dictionary and the eleven sections
