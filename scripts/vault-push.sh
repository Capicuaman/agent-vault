#!/usr/bin/env bash
# vault-push.sh — Stage, commit, and push vault changes to GitHub
#
# Usage:
#   ./scripts/vault-push.sh "add new skill: synology-nerd"
#   ./scripts/vault-push.sh                              # will prompt for message
#
# Also use this after editing a skill locally to propagate to all instances.
# Other instances should then run ./scripts/vault-sync.sh

set -euo pipefail

VAULT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
RESET='\033[0m'

cd "$VAULT_DIR"

# Check for changes
if git diff --quiet && git diff --staged --quiet && [[ -z "$(git ls-files --others --exclude-standard)" ]]; then
  echo -e "${YELLOW}Nothing to commit — vault is clean.${RESET}"
  exit 0
fi

# Show status
echo -e "${CYAN}📦 Agent Vault — Changes to commit:${RESET}"
echo ""
git status --short
echo ""

# Commit message
if [[ -n "${1:-}" ]]; then
  MSG="$1"
else
  read -r -p "Commit message: " MSG
  if [[ -z "$MSG" ]]; then
    echo -e "${RED}Aborting — empty commit message.${RESET}"
    exit 1
  fi
fi

# Stage all and push
git add -A
git commit -m "$MSG"

echo ""
echo -e "${CYAN}🚀 Pushing to GitHub...${RESET}"
git push origin main

echo ""
echo -e "${GREEN}✅ Pushed. Other instances can now run:${RESET}"
echo -e "   ${CYAN}cd ~/Documents/agent-vault && ./scripts/vault-sync.sh${RESET}"
