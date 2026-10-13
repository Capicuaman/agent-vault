#!/usr/bin/env bash
# vault-install.sh — Install vault skills into the current machine's pi config
#
# Usage:
#   ./scripts/vault-install.sh                 # interactive picker
#   ./scripts/vault-install.sh all             # install all skills
#   ./scripts/vault-install.sh general         # install a category
#   ./scripts/vault-install.sh herdr-nerd      # install a single skill by name
#   ./scripts/vault-install.sh bilan nerds     # install multiple categories
#
# Skills are installed into ~/.pi/agent/skills/ (global scope, available in all projects)
# Prompts are installed into ~/.pi/agent/prompts/
# Run with --dry-run to preview without making changes.

set -euo pipefail

VAULT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_DIR="$VAULT_DIR/skills"
PROMPTS_DIR="$VAULT_DIR/prompts"
TARGET_SKILLS="${PI_SKILLS_DIR:-$HOME/.pi/agent/skills}"
TARGET_PROMPTS="${PI_PROMPTS_DIR:-$HOME/.pi/agent/prompts}"
DRY_RUN=false
INSTALLED=0
SKIPPED=0

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
RED='\033[0;31m'
RESET='\033[0m'

log()  { echo -e "${CYAN}▶${RESET} $*"; }
ok()   { echo -e "${GREEN}✅${RESET} $*"; INSTALLED=$((INSTALLED+1)); }
skip() { echo -e "${YELLOW}⏭${RESET} $*"; SKIPPED=$((SKIPPED+1)); }
err()  { echo -e "${RED}✗${RESET} $*" >&2; }

# Parse flags
ARGS=()
for arg in "$@"; do
  if [[ "$arg" == "--dry-run" ]]; then
    DRY_RUN=true
    echo -e "${YELLOW}[DRY RUN] No changes will be made${RESET}"
  else
    ARGS+=("$arg")
  fi
done
set -- "${ARGS[@]:-}"

install_skill() {
  local skill_path="$1"
  local skill_name
  skill_name="$(basename "$skill_path")"
  local target="$TARGET_SKILLS/$skill_name"

  if [[ -d "$target" ]]; then
    skip "already installed: $skill_name (use --force to overwrite)"
    return
  fi

  log "installing skill: $skill_name"
  if [[ "$DRY_RUN" == "false" ]]; then
    mkdir -p "$TARGET_SKILLS"
    cp -r "$skill_path" "$target"
  fi
  ok "$skill_name → $target"
}

install_category() {
  local category="$1"
  local cat_dir="$SKILLS_DIR/$category"

  if [[ ! -d "$cat_dir" ]]; then
    err "category not found: $category (available: bilan, general, nerds, forges, platform)"
    return 1
  fi

  log "installing category: $category"
  for skill_dir in "$cat_dir"/*/; do
    [[ -d "$skill_dir" ]] && install_skill "$skill_dir"
  done
}

install_all() {
  log "installing ALL skills from vault..."
  for cat_dir in "$SKILLS_DIR"/*/; do
    local cat
    cat="$(basename "$cat_dir")"
    install_category "$cat"
  done

  log "installing prompts..."
  mkdir -p "$TARGET_PROMPTS"
  for prompt in "$PROMPTS_DIR"/*.md; do
    local name
    name="$(basename "$prompt")"
    if [[ -f "$TARGET_PROMPTS/$name" ]]; then
      skip "prompt already exists: $name"
    else
      [[ "$DRY_RUN" == "false" ]] && cp "$prompt" "$TARGET_PROMPTS/"
      ok "prompt: $name"
    fi
  done
}

install_single_skill() {
  local name="$1"
  local found=false

  for cat_dir in "$SKILLS_DIR"/*/; do
    if [[ -d "$cat_dir/$name" ]]; then
      install_skill "$cat_dir/$name"
      found=true
      break
    fi
  done

  if [[ "$found" == "false" ]]; then
    err "skill not found: $name"
    echo "Available skills:"
    find "$SKILLS_DIR" -maxdepth 2 -type d -name "*" | grep -v "^$SKILLS_DIR$" | \
      grep -v "/$" | xargs -I{} basename {} | sort | column
    return 1
  fi
}

interactive_picker() {
  echo ""
  echo -e "${CYAN}🏛️  Agent Vault — Skill Installer${RESET}"
  echo ""
  echo "Categories:"
  echo "  1) all      — install everything (40 skills + 15 prompts)"
  echo "  2) general  — universal workflow skills (15)"
  echo "  3) nerds    — expert persona skills (5)"
  echo "  4) forges   — production skills (6)"
  echo "  5) platform — tool integration skills (5)"
  echo "  6) bilan    — brand-specific skills (9)"
  echo "  7) prompts  — prompt templates only (15)"
  echo ""
  read -r -p "Enter category name(s) or skill name, or 'all': " choice

  case "$choice" in
    all|1)      install_all ;;
    general|2)  install_category general ;;
    nerds|3)    install_category nerds ;;
    forges|4)   install_category forges ;;
    platform|5) install_category platform ;;
    bilan|6)    install_category bilan ;;
    prompts|7)
      mkdir -p "$TARGET_PROMPTS"
      for p in "$PROMPTS_DIR"/*.md; do cp "$p" "$TARGET_PROMPTS/"; done
      ok "prompts installed"
      ;;
    *)
      install_single_skill "$choice"
      ;;
  esac
}

# Ensure target exists
mkdir -p "$TARGET_SKILLS"

# Route by args
if [[ ${#ARGS[@]} -eq 0 ]]; then
  interactive_picker
elif [[ "${ARGS[0]}" == "all" ]]; then
  install_all
else
  for arg in "${ARGS[@]}"; do
    case "$arg" in
      bilan|general|nerds|forges|platform)
        install_category "$arg"
        ;;
      *)
        install_single_skill "$arg"
        ;;
    esac
  done
fi

echo ""
echo -e "${GREEN}Done.${RESET} Installed: $INSTALLED  |  Skipped: $SKIPPED"
if [[ "$INSTALLED" -gt 0 ]]; then
  echo -e "Skills location: ${CYAN}$TARGET_SKILLS${RESET}"
fi
