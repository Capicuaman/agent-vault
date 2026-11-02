# Local Skill Integration — Decision Record and Runbook

Status: **accepted** · Applies to: every machine that installs vault skills.

## The problem

A machine accumulates three kinds of skill directories, and before this decision
the vault only knew how to handle the first:

1. **Vault-owned** — cloned and installed from `agent-vault`. Talos reports `ok`.
2. **Locally authored, never adopted** — real work sitting only in an install
   root (`~/.agents/skills/<name>`). Talos calls it `unmanaged`. No backup, no
   portability, one disk failure from gone.
3. **Package-managed** — Orca's version-matched stubs, the Omarchy skills,
   skills.sh packages. Talos also calls these `unmanaged`, so real local work and
   furniture look identical in the report.

Two smaller problems compounded it:

- `MANIFEST.md` was hand-maintained ("TODO: build that script"), so every
  adoption risked an unregistered skill — an **orphan**, per the doctrine.
- There was no written rule for *whether* to vendor something. The default move —
  copy it in — is wrong for any skill whose content is owned upstream.

## The decision

Every installed skill falls into exactly one bucket. The bucket determines the
operation, and the operation is mechanical.

| Bucket | Test | Where it lives | Guard |
|---|---|---|---|
| **Owned** | We author it, or it is a durable local artifact (knowledge pack, SOP, script) | `skills/<category>/<name>/` | Talos `ok` |
| **External** | Content is generated/shipped by a package we install (Orca, Omarchy, skills.sh) | Install root only | Row in `registries/_externals.md`; Talos `external` |
| **Machine exception** | Owned, but this machine intentionally holds a different copy | Install root only | `~/.config/agent-vault/talos-allowlist.txt`; Talos `allowed` |

The test for **external** is: *would a copy in the vault be wrong within one
upgrade?* Orca's `orca-cli`, `orchestration`, and `computer-use` are discovery
stubs that fetch a version-matched guide from the running binary — a vault copy
would pin prose to the wrong build. Omarchy ships `omarchy` and `diagnose-crash`
inside `/usr/share/omarchy` and symlinks them in. `find-skills` exists to drive
`npx skills`, the package manager that already owns it. All six are external.

The test for **machine exception** is narrower: the content is ours, but this
machine deliberately carries a fuller or forked copy. Today there is exactly one:
`book-to-skill` is the full upstream checkout here, not the trimmed vault skill.

Anything else that is authored here is **owned** and gets adopted.

## Categories used by this pass

| Skill | Bucket | Home | Why |
|---|---|---|---|
| `anki-admin` | owned | `skills/platform/` | Local SOP + script + collection ownership. A tool integration. |
| `bonanno-game-theory` | owned | `skills/knowledge/` | Book-derived reference corpus. A **knowledge pack**. |
| `orca-cli`, `orchestration`, `computer-use` | external | — | Version-matched Orca stubs. |
| `find-skills` | external | — | skills.sh package. |
| `omarchy`, `diagnose-crash` | external | — | Omarchy distro package (symlinked). |

`knowledge/` is a new category, not a new mechanism: `book-to-skill` already
produces exactly this artifact shape, so the Family is `knowledge-pack` with
README + MANIFEST as its Registry of Record (no separate registry required).

## What changed in the workflow

### New: `scripts/vault-import.sh`

The one-way door from *unmanaged* to *owned*. It refuses to guess:

- refuses a symlinked skill (package-managed → declare it external instead);
- refuses a name already declared in `registries/_externals.md`;
- requires loadable frontmatter (`name` == directory, description ≥ 40 chars);
- scans for private keys, cloud tokens, and other users' absolute home paths;
- refuses to overwrite an existing vault skill without `--force`;
- copies with `.git`, `node_modules`, `__pycache__` excluded;
- refreshes the live copy **from the vault** afterwards, so the vault is the
  source of truth and Talos reports identical content rather than drift;
- prints the remaining steps (catalog, audit, push).

`--dry-run` runs every gate without writing.

### New: `scripts/vault-manifest.sh`

Catalogs are now derived, not remembered:

- `--write` regenerates the `<!-- BEGIN SKILLS -->` block in `MANIFEST.md`
  (total, per-category counts, one row per skill with a trigger phrase) and fixes
  the derived counts in `README.md` (category counts, `Total: N skills`, prompt /
  registry / config / script counts). Prose is never touched.
- `--check` reports drift and exits non-zero, so it can gate a push.

This is what makes adoption safe: a newly imported skill cannot become an orphan
by forgetfulness.

### Changed: `scripts/vault-audit.py`

- Reads `registries/_externals.md` (Registry of Record for the `external` Family).
- Talos now reports declared externals as `external`, separately from
  `unmanaged`. `unmanaged` now means only one thing: *this machine has an owned
  skill the vault has never seen — adopt it or declare it*.
- Ghost detection ignores declared externals, so documenting them is not drift.
- `registries/` is treated as a container, not an unmanaged skill.

### Changed: one other rule

A skill installed on a machine is never the copy of record. Every edit goes to
the vault clone and flows outward (push → pull/install). The live copy is
overwritten by `vault-import.sh`, `vault-sync.sh --install`, or
`vault-audit.py --installed --repair`.

## Runbook

### Adopt a locally authored skill

```bash
cd ~/Documents/agent-vault
./scripts/vault-import.sh <name> --category <cat> --dry-run   # gates only
./scripts/vault-import.sh <name> --category <cat>             # copy + refresh live
$EDITOR README.md                                             # add the row/prose
./scripts/vault-manifest.sh --write
python3 scripts/vault-audit.py --short                        # no zombie/ghost/orphan/hollow
python3 scripts/vault-audit.py --installed                    # <name> is now ok
./scripts/vault-push.sh "import <name> into <cat>"
```

### Declare an upstream-owned skill external

```bash
$EDITOR registries/_externals.md     # name + owner + installed-by + re-runnable verify
python3 scripts/vault-audit.py --installed   # now reported as external
./scripts/vault-push.sh "externals: add <name>"
```

If the package stops shipping the skill, delete the row. Never adopt a fork of a
version-matched stub.

### Pull on another machine

```bash
cd ~/Documents/agent-vault
PI_SKILLS_DIR=~/.agents/skills ./scripts/vault-sync.sh --install
python3 scripts/vault-audit.py --installed
```

New skills that were never installed there show as `missing` — a choice, not an
error. Install on demand with
`PI_SKILLS_DIR=~/.agents/skills ./scripts/vault-install.sh <name>`.

### Before every push

```bash
./scripts/vault-manifest.sh --check && python3 scripts/vault-audit.py --short
```

## Adoption gates

An adopted skill must pass the doctrine gates **and** the mechanical ones:

| Gate | Question | Enforced by |
|---|---|---|
| Routable | Does the description decide invocation? | `vault-import.sh` (≥ 40 chars) |
| Different | Is there a real behavior delta? | human — the steward's intake card |
| Bounded | One responsibility, one scope? | human |
| Registered | Is it in a Registry of Record? | `vault-manifest.sh --check` + audit orphan check |
| Loadable | `name` == directory, valid YAML? | `vault-import.sh` + audit zombie check |
| Portable | No secrets, no other users' absolute paths? | `vault-import.sh` scan |
| Owned | Is it actually ours to own? | `_externals.md` refusal |

Machine prerequisites (a local database, a CLI on PATH) belong in a
`## Prerequisites` section of the skill itself, not in a per-machine variant.

## Rollback

- An imported skill: `git rm -r skills/<cat>/<name>` and reinstall it into the
  live root if you want to keep using it locally; remove its README row and run
  `./scripts/vault-manifest.sh --write`.
- An external declaration: delete the row; the copy becomes `unmanaged` again.
- The pre-change state of any machine's skill roots was backed up to
  `~/.local/state/agent-vault-backups/skills-<timestamp>.tar.gz` before the first
  adoption.

## Open follow-ups

- `bilan-label-system` is **hollow**; `bilan-blog-ops`, `bilan-seo-conversion`,
  and `here-now` are **stale** past 180 days (see `vault-audit.py --short`).
- `book-to-skill` stays machine-allowlisted until the full checkout is either
  upstreamed or trimmed; the allowlist file says exactly that.
