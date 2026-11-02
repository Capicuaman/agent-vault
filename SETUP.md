# Setting Up a New Herdr Instance

Copy-paste these commands on any new machine or Herdr session.

## 1. Clone the Vault

```bash
git clone git@github.com:Capicuaman/agent-vault.git ~/Documents/agent-vault
cd ~/Documents/agent-vault
chmod +x scripts/*.sh
```

## 2. Install Skills

```bash
# Install everything (recommended for a fresh machine)
./scripts/vault-install.sh all

# Or pick what you need
./scripts/vault-install.sh general nerds forges platform

# Or a single skill
./scripts/vault-install.sh herdr-nerd
```

Skills land in `~/.pi/agent/skills/` — globally available in all pi sessions.

## 3. Install Prompts (Optional)

Prompts are installed by `vault-install.sh all`. To install them standalone:

```bash
mkdir -p ~/.pi/agent/prompts
cp ~/Documents/agent-vault/prompts/*.md ~/.pi/agent/prompts/
```

## 4. Keep in Sync

```bash
# Get latest skills from GitHub
cd ~/Documents/agent-vault && ./scripts/vault-sync.sh

# Get latest AND reinstall updated skills
./scripts/vault-sync.sh --install
```

## 5. Adopt a Skill That Already Exists on This Machine

Do not copy by hand. The importer runs the gates (real directory, not a
symlink, loadable frontmatter, no secrets, not declared external), copies the
skill, and refreshes the live copy from the vault:

```bash
cd ~/Documents/agent-vault

./scripts/vault-import.sh my-skill --category platform --dry-run
./scripts/vault-import.sh my-skill --category platform
$EDITOR README.md                              # add the row/prose
./scripts/vault-manifest.sh --write            # regenerate catalogs
python3 scripts/vault-audit.py --installed     # no longer "unmanaged"
./scripts/vault-push.sh "import my-skill into platform"
```

If the skill is owned upstream (Orca, Omarchy, skills.sh), do **not** import it.
Add a row to `registries/_externals.md` instead. Full rationale:
[`docs/local-skill-integration.md`](docs/local-skill-integration.md).

## 6. Push Your Changes Back

When you edit a skill, update a prompt, or create something new:

```bash
cd ~/Documents/agent-vault

# Authored here: create skills/<category>/<name>/SKILL.md, then
./scripts/vault-manifest.sh --write
python3 scripts/vault-audit.py --short
./scripts/vault-push.sh "add my-new-skill to platform"
```

Before pushing, both guards should pass:

```bash
./scripts/vault-manifest.sh --check
python3 scripts/vault-audit.py --short
```

---

## Directory Reference

```
~/.pi/agent/skills/       ← vault-install.sh default install root
~/.agents/skills/         ← alternate install root (pi reads both)
~/.pi/agent/prompts/      ← where prompts get installed
~/Documents/agent-vault/  ← the vault repo (this)
```

`vault-sync.sh --install` and `vault-audit.py --installed` default to
`~/.agents/skills` + `~/.pi/agent/skills`. If this machine uses only one root,
set `PI_SKILLS_DIR=~/.agents/skills` (install/sync) or pass
`--install-roots ~/.agents/skills` (audit).

## Environment Variable Overrides

```bash
# Install to a different location (project-scoped)
PI_SKILLS_DIR=/path/to/project/.pi/skills ./scripts/vault-install.sh general
```

---

## External Skills

A package-managed skill (Orca stubs, Omarchy's own skills, skills.sh packages) is
never vendored. It is declared in `registries/_externals.md` with an owner and a
verify command; Talos then reports it as `external` instead of `unmanaged`.

```bash
$EDITOR registries/_externals.md
python3 scripts/vault-audit.py --installed
```

## Herdr Session Bootstrap

If you want vault-sync to run every time a Herdr session starts, add to your shell profile:

```bash
# ~/.bashrc or ~/.zshrc
if [[ -d ~/Documents/agent-vault ]]; then
  (cd ~/Documents/agent-vault && git pull --rebase origin main -q 2>/dev/null &)
fi
```

This runs the sync in the background on shell init — silent, non-blocking.
