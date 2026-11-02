# Entry Contract

Condensed from the authoritative `README.md` in the error-notes root. If they
disagree, the `README.md` wins.

Root: `~/Documents/textDump/03_RESOURCES/Software_Engineering/error-notes/`

## The eleven sections (fixed H2 contract)

Keep names and numbers, even when a section is short.

```markdown
## 1. Symptom
## 2. Impact
## 3. Reproduction
## 4. Evidence
## 5. Triage log
## 6. Root cause
## 7. Resolution
## 8. Verification
## 9. Prevention
## 10. Transferable lesson
## 11. Automation notes
```

### What each section is for

| # | Section | Rule |
|---|---|---|
| 1 | Symptom | What a user sees, in one or two sentences. **No cause here.** |
| 2 | Impact | Who/what is blocked; workaround; severity justification. |
| 3 | Reproduction | The command, and whether it is deterministic or environment-specific. |
| 4 | Evidence | **Verbatim.** Never paraphrase error text or stack frames. |
| 5 | Triage log | Numbered, in the order you actually checked. **Record dead ends.** This is the most valuable section for future-you. |
| 6 | Root cause | Split into **proximate** (the failing condition), **underlying** (why it exists), **aggravating** (what made it worse). |
| 7 | Resolution | Immediate fix; permanent fix if different; **what did NOT work**. |
| 8 | Verification | A **positive** check: the operation now succeeds, with command/output. |
| 9 | Prevention | Concrete: habit, environment change, tooling guardrail, upstream report. |
| 10 | Transferable lesson | One paragraph, generalizes beyond this tool, no project nouns. |
| 11 | Automation notes | What the hook recorded, what could be inferred, and **which false leads an automated classifier would take**. |

## Frontmatter fields

| Field | Type | Filled by | Meaning |
|---|---|---|---|
| `id` | string | manual/auto | `ERR-YYYY-MM-DD-NNN`, never reused |
| `slug` | string | auto | short kebab-case handle |
| `title` | string | manual | symptom in one line, not the cause |
| `date` | date | auto | first occurrence |
| `status` | enum | manual | `open`, `resolved`, `mitigated`, `upstream`, `wontfix` |
| `severity` | enum | manual | `blocker`, `high`, `medium`, `low`, `cosmetic` |
| `category` | enum | auto/manual | an error family from `diagnostic-moves.md` |
| `tags` | string[] | auto/manual | free-form retrieval keys; include a **boundary** tag |
| `component` | string | auto/manual | `package#function` that failed |
| `fingerprint` | string | auto | 16-hex hash of the normalized message |
| `repro` | enum | manual | `deterministic`, `intermittent`, `environment-specific`, `unknown` |
| `time_to_resolve_min` | int | manual | honest effort, not wall clock |
| `failed_assumption` | string | manual | the belief that made the error surprising |
| `environment` | object | auto | os, shell, tool, runtime, cwd |
| `trigger` | string | auto | exact command or action |
| `error_kind` | enum | auto | `thrown-error`, `exit-code`, `log-line`, `wrong-output`, `hang`, `crash` |
| `source` | enum | auto | `manual`, `capture-hook`, `agent`, `ci` |
| `confidence` | enum | manual | `verified`, `probable`, `hypothesis` |
| `related` | string[] | manual | other entry ids |
| `supersedes` | string/null | manual | replaced entry id |

## Writing quality bars

**A good `title`** is the symptom, not the cause:

- ✗ "wrong permissions on the config directory"
- ✓ "`tool start` fails: permission denied writing config"

**A good `## 5. Triage log`** reads like a lab notebook:

```markdown
1. Ran `tool start` → exit 1, "permission denied".
2. `ls -ld ~/.tool` → owned by root. Suspicious.
3. `stat ~/.tool/config.json` → mode 600, owner root.
4. `id` → uid 1000, not root.
5. `sudo -u root tool init` earlier in shell history → confirmed cause.
6. Dead end: assumed ACLs; `getfacl` showed none.
```

**A good `## 6. Root cause`** separates the layers:

- **Proximate:** the process lacked write permission on `~/.tool/config.json`.
- **Underlying:** a previous command was run under `sudo` and created the directory
  as root.
- **Aggravating:** the error message said "config invalid" instead of naming the
  permission bit.

**A good `## 10. Transferable lesson`** has no project nouns:

> "Never run a tool's initializer under `sudo` unless the tool documents that its
> state directory must be root-owned; mixed-ownership state directories produce
> errors that misreport themselves as validation failures."

## Redaction

`errlog.py` scrubs `sk-...`, `ghp_...`, AWS keys, bearer tokens, and
`password=`/`token:` values before writing. Best-effort: do not pipe production
credentials through it.

## Related-entry discipline

Set `related:` generously — the value of the library is in the edges between
entries. When two entries share a fingerprint, they are the *same* entry; bump the
index instead.

When an entry is replaced rather than amended, keep the old one and set
`supersedes:` on the new one. Never reuse an ID.
