#!/usr/bin/env bash
# vault-link-zapata.sh — Replace scattered skill dirs on zapata with symlinks into the vault.
#
# After this runs, every live skill location points into agent-vault/.
# Editing a skill in ANY location edits the vault file directly.
# Run vault-push.sh afterward to commit everything to GitHub.
#
# Safe: backs up each dir to <dir>.bak before replacing with symlink.
# Idempotent: skips dirs that are already symlinks.

set -euo pipefail

VAULT="$HOME/Documents/agent-vault"
ERRORS=0
LINKED=0
SKIPPED=0

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
RED='\033[0;31m'
RESET='\033[0m'

link_skill() {
  local live_dir="$1"     # e.g. ~/.pi/agent/skills/herdr-nerd
  local vault_dir="$2"    # e.g. ~/Documents/agent-vault/skills/nerds/herdr-nerd
  local name
  name="$(basename "$live_dir")"

  # Already a symlink — skip
  if [[ -L "$live_dir" ]]; then
    echo -e "${YELLOW}⏭  already symlinked:${RESET} $name"
    SKIPPED=$((SKIPPED+1))
    return
  fi

  # Vault target must exist
  if [[ ! -d "$vault_dir" ]]; then
    echo -e "${RED}✗  vault dir missing:${RESET} $vault_dir"
    ERRORS=$((ERRORS+1))
    return
  fi

  # Backup the live dir
  mv "$live_dir" "${live_dir}.bak"
  # Create symlink
  ln -s "$vault_dir" "$live_dir"
  echo -e "${GREEN}✅ linked:${RESET} $live_dir → $vault_dir"
  LINKED=$((LINKED+1))
}

find_vault() {
  local name="$1"
  find "$VAULT/skills" -maxdepth 2 -type d -name "$name" | head -1
}

echo -e "${CYAN}🔗 Linking zapata skill dirs → agent-vault${RESET}"
echo ""

# ── ~/.pi/agent/skills/ ──────────────────────────────────────────────
echo -e "${CYAN}── ~/.pi/agent/skills/${RESET}"
for skill_dir in "$HOME/.pi/agent/skills"/*/; do
  name="$(basename "$skill_dir")"
  [[ "$name" == "registries" ]] && continue
  vault_path="$(find_vault "$name")"
  link_skill "$skill_dir" "$vault_path"
done

echo ""

# ── textDump/.pi/skills/ ─────────────────────────────────────────────
echo -e "${CYAN}── textDump/.pi/skills/${RESET}"
TDUMP="$HOME/Documents/textDump"
for skill_dir in "$TDUMP/.pi/skills"/*/; do
  name="$(basename "$skill_dir")"
  [[ "$name" == "registries" ]] && continue
  vault_path="$(find_vault "$name")"
  link_skill "$skill_dir" "$vault_path"
done

echo ""

# ── textDump/.agents/skills/ ─────────────────────────────────────────
echo -e "${CYAN}── textDump/.agents/skills/${RESET}"
for skill_dir in "$TDUMP/.agents/skills"/*/; do
  name="$(basename "$skill_dir")"
  vault_path="$(find_vault "$name")"
  link_skill "$skill_dir" "$vault_path"
done

echo ""

# ── ~/.agents/skills/ ────────────────────────────────────────────────
echo -e "${CYAN}── ~/.agents/skills/${RESET}"
for skill_dir in "$HOME/.agents/skills"/*/; do
  name="$(basename "$skill_dir")"
  vault_path="$(find_vault "$name")"
  link_skill "$skill_dir" "$vault_path"
done

echo ""
echo "────────────────────────────────────"
echo -e "Linked: ${GREEN}$LINKED${RESET}  |  Skipped: ${YELLOW}$SKIPPED${RESET}  |  Errors: ${RED}$ERRORS${RESET}"
echo ""

if [[ "$LINKED" -gt 0 ]]; then
  echo -e "${CYAN}Next: push the .bak cleanup to keep the vault tidy${RESET}"
  echo "  cd $VAULT && ./scripts/vault-push.sh \"link: replace zapata scattered dirs with vault symlinks\""
fi

if [[ "$ERRORS" -gt 0 ]]; then
  echo -e "${RED}Some skills couldn't be linked — check output above.${RESET}"
fi
