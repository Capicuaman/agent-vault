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

## 5. Push Your Changes Back

When you edit a skill, update a prompt, or create something new:

```bash
cd ~/Documents/agent-vault

# Copy the updated/new skill into vault first
cp -r ~/.pi/agent/skills/my-new-skill skills/platform/

# Then push
./scripts/vault-push.sh "add my-new-skill to platform"
```

---

## Directory Reference

```
~/.pi/agent/skills/      ← where vault-install.sh drops skills
~/.pi/agent/prompts/     ← where prompts get installed
~/Documents/agent-vault/ ← the vault repo (this)
```

## Environment Variable Overrides

```bash
# Install to a different location (project-scoped)
PI_SKILLS_DIR=/path/to/project/.pi/skills ./scripts/vault-install.sh general
```

---

## Herdr Session Bootstrap

If you want vault-sync to run every time a Herdr session starts, add to your shell profile:

```bash
# ~/.bashrc or ~/.zshrc
if [[ -d ~/Documents/agent-vault ]]; then
  (cd ~/Documents/agent-vault && git pull --rebase origin main -q 2>/dev/null &)
fi
```

This runs the sync in the background on shell init — silent, non-blocking.
