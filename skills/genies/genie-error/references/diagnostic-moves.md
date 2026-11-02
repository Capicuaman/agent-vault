# Diagnostic Moves

A playbook for turning an error message into a cause. Tag entries with the moves
you actually used, so future-you can see which moves pay off.

## Move 1 — split claim from remedy

Every good error message contains two things:

```
dsh: profile "tui" does not exist; create it with 'dsh plugin --profile tui add <package>'
     └────────── claim ──────────┘  └──────────────── remedy ─────────────────────────┘
```

The claim tells you the failing condition. The remedy is the author's *guess* at
what you meant to do. **Verify both.** Remedies are frequently wrong or
incomplete — in the example above, following the remedy leads to a different
failure (a missing package manager, then a compatibility gate).

**Tag:** `split-claim-remedy`

## Move 2 — read the stack top-down

The **top frame** is the decision that rejected you. Frames below are callers; you
rarely need them.

```text
Error: xyz
    at loadProfile (profile.js:42:11)   ← start here
    at main (cli.js:88:3)
    at processTicksAndRejections (...)
```

For a long stack, read the top and the bottom, then only the middle frames whose
module names match the subsystem. **Tag:** `read-stack-top-down`

## Move 3 — locate the throw site

Grep the literal message in the installed package. This converts prose into code
and reveals the real condition, which is often broader or narrower than the message.

```sh
pkg=$(npm root -g)/some-pkg
rg -n "does not exist" "$pkg/dist" -C 5
```

Now read the branch:

```js
if (state missing) {
  if (name unknown) throw new Error(`profile "${name}" does not exist`);
  else autoCreate(name);   // ← the other branch
}
```

Ask: **which branch fired?** Is the file gone, or is the name not recognized?
Those are different bugs with the same message.

**Tag:** `locate-throw-site`, `read-condition`

## Move 4 — dump the state the code consults

Do not reason about what the state "should" be. Look at it.

```sh
ls -la ~/.tool/profiles/          # the profile directory
cat ~/.tool/config.json | jq .    # the composed config
tool config list                  # the tool's own view
tool --help | rg -n profile       # what it advertises
```

**Tag:** `dump-state`, `dump-config`

## Move 5 — trust artifacts over docs

Docs describe intent; the installed version describes reality.

```sh
ls "$(npm root -g)/pkg/dist"          # what actually shipped
rg -n "flagName" "$(npm root -g)/pkg" # is the flag implemented?
```

If the docs describe a flag the code never reads, that is a **docs-drift** entry
worth writing. **Tag:** `read-artifact-not-docs`

## Move 6 — check version drift early

Before debugging, establish whether the bug is even present in this version.

```sh
tool --version
npm view <pkg> dist-tags
npm view <pkg> versions --json | jq '.[-5:]'
```

A limitation may already be fixed upstream — or may exist in every version, which
changes your strategy from "upgrade" to "work around". **Tag:** `verify-version`

## Move 7 — differential

Compare a working case to the failing case and diff everything.

```sh
# works here
cd /tmp && tool subcommand
# fails here
cd ~/project && tool subcommand
```

Vary one dimension at a time: cwd, env var, config file, version, user, shell,
terminal. The first dimension whose variation flips the outcome is the cause.
**Tag:** `differential`

```sh
env -i PATH="$PATH" tool subcommand   # strip the environment
```

## Move 8 — bisect

For regressions and unknown causes.

```sh
git bisect start
git bisect bad HEAD
git bisect good v1.2.0
# then: git bisect run ./check.sh
```

For binary/package versions, bisect the version list instead.
**Tag:** `bisect`

## Move 9 — minimal reproduction

Reduce to the smallest command that still fails. Every element you can remove
without changing the outcome is a false lead you will not chase again — and the
reproduction belongs verbatim in the entry.

**Tag:** `minimal-repro`

## Move 10 — check upstream

Search the project's issues with the *exact* message, not your paraphrase.

```sh
gh search issues --repo <owner>/<repo> "profile does not exist"
```

Search by the message the code emits, since that is what others will have pasted.
**Tag:** `check-upstream`

## Move 11 — classify the failure kind

Before fixing, name what kind of failure this is. The kind determines the fix
strategy.

| Kind | Tell | Strategy |
|---|---|---|
| `precondition` | required file/state/flag missing | inspect state dir, read the guard |
| `registry` | unknown name/id/command | dump the table it looked up |
| `config` | invalid/unknown setting | dump composed config |
| `dependency` | package/binary/version missing | `which`, `npm ls`, lockfile |
| `permission` | EACCES, 401/403, sandbox denial | check identity + policy |
| `network` | timeout, DNS, TLS, 5xx | curl the endpoint, check proxy |
| `resource` | ENOSPC, OOM, fd limits | `df`, `free`, `ulimit` |
| `type/schema` | cannot read property, parse error | inspect the actual data |
| `build` | compiler/linker/bundler failure | read the *first* error, not the last |
| `logic` | runs but wrong answer | diff expected vs actual, bisect |
| `environment` | works elsewhere | diff versions, env vars, paths |

**Tag:** the category name.

## Move 12 — name the failed assumption

This is the move that compounds. The error was surprising because you believed
something. Write the belief down in one sentence:

> "I believed the newest plugin would work with the newest runtime, and that a
> successful `pnpm add` meant a successful install."

If you cannot state the failed assumption, you have not understood the error yet —
you have only made it stop.

**Tag:** `failed-assumption`

## Choosing moves under time pressure

- **Unknown message, known tool** → 1, 3, 4.
- **Works elsewhere** → 6, 7.
- **Worked yesterday** → 6, 8.
- **Intermittent** → 7, then lifecycle/concurrency in
  [`../../genie-doctrine/references/boundaries.md`](../../genie-doctrine/references/boundaries.md).
- **Message lies** → 3, 5.
