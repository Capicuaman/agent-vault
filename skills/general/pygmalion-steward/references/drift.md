# Drift — When the World Moves Under an Entity

Staleness and drift are different failures and need different fixes.

| | Stale | Drifted |
|---|---|---|
| **Cause** | Time passed | The facts changed |
| **Test** | Snapshot date > threshold | Declared version ≠ current upstream |
| **Symptom** | "this is old" | "this is confidently wrong" |
| **Fix** | Re-ground, or mark historical | Re-ground **and** bump version |
| **Detected by** | `vault-audit.py` date check | `vault-audit.py --drift` |

An Entity can be fresh (recently edited) and still drifted, because someone
updated the prose without re-checking the version. Always test the facts, not the
file date.

## The probe convention

A **probe** is a declared, re-runnable command that returns the current upstream
version. Probes live in a nerd's `references/facts.md`, next to the snapshot date:

```markdown
**Snapshot date:** 2026-10-06
**Source URL:** https://herdr.dev/docs/
**Declared version:** 0.9.3
**Probe:** `herdr --version`
```

The audit reads three fields:

| Field | Required | Purpose |
|---|---|---|
| `Snapshot date` | yes | staleness |
| `Declared version` | recommended | the version the Entity believes it documents |
| `Probe` | recommended | the command that reveals the current version |

Without a probe, the Entity can only be tested for staleness, never for drift.

## Probe safety rules

Probes are authored by you, in your own Entity, so they are trusted — but they
must still be safe to run repeatedly and unattended.

**Allowed**

- `<tool> --version` / `-v`
- `npm view <pkg> version`
- `gh release view <owner>/<repo> --json tagName -q .tagName`
- `docker image inspect <image> --format '{{index .Config.Labels "version"}}'`
- `git ls-remote --tags <url>` (read-only)
- `curl -sI <url>` (headers only)

**Forbidden**

- Anything that installs, upgrades, writes, or deletes.
- Anything that authenticates to a third party.
- Anything that depends on a project working directory.
- Anything that prints secrets. If the output could contain a token, the probe is
  wrong — use a version subcommand instead.

## Adding a probe, by technology class

| The technology is… | Probe |
|---|---|
| an installed CLI | `mytool --version` |
| an npm package | `npm view package version` |
| a GitHub project | `gh release view owner/repo --json tagName -q .tagName` |
| a Docker image | `docker image inspect image --format '{{index .Config.Labels "version"}}'` |
| a docs-only product | no probe; rely on staleness + a manual refresh |
| a language/framework | the toolchain version command, not the framework's |

If the technology has no probe, write `**Probe:** N/A — manual refresh via
graphify_add <url>` so the audience knows the gap is deliberate.

## The sweep

```bash
cd ~/Documents/agent-vault

# 1. See the plan — prints every nerd's declared version and its probe
python3 scripts/vault-audit.py --drift

# 2. Execute the probes (opt-in, read-only commands only)
python3 scripts/vault-audit.py --drift --run-probes

# 3. Machine-readable, for a cron job or dashboard
python3 scripts/vault-audit.py --drift --run-probes --json
```

The report classifies each nerd:

| Result | Meaning | Action |
|---|---|---|
| `current` | probe version == declared | nothing |
| `drift` | probe version != declared | re-ground, then bump |
| `no-probe` | no probe declared | add one, or mark manual |
| `probe-failed` | command errored or timed out | investigate the probe, not the Entity |
| `stale` | snapshot older than threshold | re-ground even if versions match |

## Re-grounding a drifted nerd

1. **Confirm the drift is real.** Run the probe twice; check the release notes for
   the intervening versions, not just the latest tag.
2. **Enumerate the breaking changes** between declared and current. Install
   commands, config keys, flags, defaults, file paths.
3. **Update `references/facts.md`** — snapshot date, declared version, versions
   table, and any changed facts.
4. **Update `references/commands.md`** — a command that no longer exists is worse
   than a missing one, because the nerd will assert it confidently.
5. **Re-check the anti-patterns section.** Common misconceptions change with
   major versions; the thing you were correcting may now be correct.
6. **Run the trigger test** if any concept names changed (a renamed concept means
   the description may no longer fire on the right questions).
7. **Bump `metadata.version`**:
   - facts only → **patch**
   - commands/procedure changed → **minor**
   - description or scope changed → **major**
8. **Run `python3 scripts/vault-audit.py --drift --run-probes`** and confirm
   `current`.

## Drift beyond nerds

The same logic applies to any Entity that grounds on external state:

| Entity | Drift signal | Probe |
|---|---|---|
| nerd | tool/framework version | version command |
| forge | the output spec its ecosystem now expects | check the canonical example against current upstream docs |
| doctrine | the discipline it encodes (rare) | manual review |
| genie | the artifact formats it mines (e.g. changelog conventions) | manual review |
| platform skill | the host agent's own version and APIs | `<agent> --version` + docs |

For non-nerd Entities without a probe, use the **staleness** check and a manual
review at the monthly cadence.

## Cadence

| When | What |
|---|---|
| **Weekly** | `--drift` without probes — surfaces stale and unprobed Entities |
| **Monthly** | `--drift --run-probes` — actual facts check |
| **On upgrade** | any tool upgrade in the stack → sweep the matching nerds |
| **On release** | a probe reporting a new major → schedule re-grounding |

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Updating the snapshot date without re-checking facts | Creates the illusion of freshness; drift persists |
| Probing a major version and missing breaking changes in between | The nerd is current on the number and wrong on the commands |
| Letting the probe install or upgrade | Turns an audit into a mutation |
| Skipping `commands.md` when facts change | The most damaging drift is a confidently wrong command |
| Treating a failed probe as drift | Investigate the probe first — usually the binary moved |
| No probe and no manual note | The gap is invisible forever |
