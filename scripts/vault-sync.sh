#!/usr/bin/env bash
# vault-sync.sh — Pull the latest vault from GitHub
#
# Usage:
#   ./scripts/vault-sync.sh            # pull + show what changed
#   ./scripts/vault-sync.sh --install  # pull then re-install updated skills
#
# Run this on any Herdr instance to get skill updates from GitHub.

set -euo pipefail

VAULT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_ROOT="${PI_SKILLS_DIR:-$HOME/.pi/agent/skills}"
INSTALL_FLAG=false

GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
RESET='\033[0m'

for arg in "$@"; do
  [[ "$arg" == "--install" ]] && INSTALL_FLAG=true
done

echo -e "${CYAN}🔄 Syncing agent-vault from GitHub...${RESET}"
cd "$VAULT_DIR"

# Show current state
BEFORE=$(git rev-parse HEAD)

git pull --rebase origin main

AFTER=$(git rev-parse HEAD)

if [[ "$BEFORE" == "$AFTER" ]]; then
  echo -e "${YELLOW}Already up to date.${RESET}"
else
  echo ""
  echo -e "${GREEN}✅ Updated. Changes:${RESET}"
  git log --oneline "$BEFORE".."$AFTER"
  echo ""
  echo "Changed files:"
  git diff --name-only "$BEFORE" "$AFTER" | sed 's/^/  /'
fi

if [[ "$INSTALL_FLAG" == "true" ]]; then
  echo ""
  echo -e "${CYAN}Installing updated skills...${RESET}"

  # Fail loudly rather than silently installing nothing.
  if [[ ! -d "$SKILLS_ROOT" ]]; then
    echo -e "${RED}✗ install root not found:${RESET} $SKILLS_ROOT" >&2
    echo "  pi loads skills from ~/.agents/skills and ~/.pi/agent/skills." >&2
    echo "  Set PI_SKILLS_DIR=/path/to/skills and re-run." >&2
    exit 1
  fi

  # Force-update any skills that changed. '|| true': grep exits 1 when nothing
  # matches, and pipefail would otherwise abort the script silently.
  CHANGED_SKILLS=$(git diff --name-only "$BEFORE" "$AFTER" | grep '^skills/' | \
    cut -d'/' -f1-3 | sort -u | awk -F'/' '{print $NF}' || true)
  if [[ -z "$CHANGED_SKILLS" ]]; then
    echo "No skill changes to install."
  else
    for skill in $CHANGED_SKILLS; do
      TARGET="$SKILLS_ROOT/$skill"
      SRC=$(find "$VAULT_DIR/skills" -maxdepth 2 -type d -name "$skill" | head -1)
      if [[ -z "$SRC" ]]; then
        echo -e "${YELLOW}⏭  source not found in vault:${RESET} $skill" >&2
        continue
      fi
      if [[ "$TARGET" != "$SKILLS_ROOT"/* || -z "$skill" ]]; then
        echo -e "${RED}✗ refusing to write outside install root:${RESET} $TARGET" >&2
        exit 1
      fi
      if [[ -d "$TARGET" ]]; then
        echo "  updating: $skill"
        rm -rf "$TARGET"
        cp -r "$SRC" "$TARGET"
      else
        echo -e "${YELLOW}⏭  not installed here:${RESET} $skill (use vault-install.sh)"
      fi
    done
    echo -e "${GREEN}✅ Skills updated.${RESET}"
  fi
fi
