# External Skills — Registry of Record

Skills that are **deliberately not vendored** into the vault. Their content is
owned and versioned upstream; copying them here would fork them, drift, and cost
us every upstream fix.

This file is the Registry of Record for the `external` Family.

## The rule

1. A skill listed here must **not** be imported into `skills/`. `vault-import.sh`
   refuses it by name.
2. Talos (`vault-audit.py --installed`) reports an installed copy as `external`,
   not `unmanaged`. That is the difference between "we know about this and do not
   own it" and "something appeared on this machine".
3. Externals still have a **routing contract**: they show up in the agent's skill
   list. That is why this registry tracks them at all.
4. If an external stops shipping the skill (package removed, renamed, or the
   `skills get` subcommand disappears), delete the row — do not adopt a fork.

## Known externals

| Name | Owner | Installed by | Verify |
|------|-------|--------------|--------|
| `orca-cli` | Orca (`orca-ide`) | Orca skill sharing; content ships in the binary | `orca-ide skills get orca-cli --json` |
| `orchestration` | Orca (`orca-ide`) | Orca skill sharing; content ships in the binary | `orca-ide skills get orchestration --json` |
| `computer-use` | Orca (`orca-ide`) | Orca skill sharing; content ships in the binary | `orca-ide skills get computer-use --json` |
| `find-skills` | skills.sh ecosystem | `npx skills add find-skills` | `npx skills find find-skills` |
| `omarchy` | Omarchy (distro package) | installed to `/usr/share/omarchy/default/agents/skills`, symlinked into the install root | `readlink -f ~/.pi/agent/skills/omarchy` |
| `diagnose-crash` | Omarchy (distro package) | installed to `/usr/share/omarchy/default/agents/skills`, symlinked into the install root | `readlink -f ~/.pi/agent/skills/diagnose-crash` |

## Why each one is external

| Name | Reason |
|------|--------|
| `orca-cli`, `orchestration`, `computer-use` | Thin discovery stubs. The actual guide is fetched per session from the running Orca build (`ORCA skills get <name>`), so it is always version-matched. A copy in the vault would pin prose to the wrong binary version. |
| `find-skills` | Generic upstream skill whose whole job is to install other upstream skills (`npx skills`). Vendoring it duplicates the package manager it documents. |
| `omarchy`, `diagnose-crash` | Shipped and updated by the Omarchy distribution. The install root holds symlinks into `/usr/share/omarchy/...`; the OS owns the content. |

## Adding a new external

Append a row with the exact skill directory name (it must match the installed
directory, kebab-case) and a **re-runnable verify command**. Prefer a read-only
command. Then run:

```bash
python3 scripts/vault-audit.py --installed   # the copy should now report as external
```

Machine-specific exceptions that are *not* generalizable stay in
`~/.config/agent-vault/talos-allowlist.txt`, not here.
