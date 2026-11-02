#!/usr/bin/env bash
# vault-import.sh — Promote a locally installed skill into the vault (the one-way door
# from "unmanaged" to "owned").
#
# Usage:
#   ./scripts/vault-import.sh anki-admin --category platform
#   ./scripts/vault-import.sh bonanno-game-theory --category knowledge
#   ./scripts/vault-import.sh my-skill --category general --from ~/.pi/agent/skills
#   ./scripts/vault-import.sh my-skill --category general --dry-run
#
# What it does:
#   1. Finds <skill> in an install root (flat, or <root>/<category>/<skill>).
#   2. Runs the gates from the Pygmalion doctrine: real directory (not a symlink),
#      SKILL.md loadable, name == directory, description present, not declared
#      external, no obvious secrets.
#   3. Copies it to skills/<category>/<skill>/ (never overwrites without --force).
#   4. Refreshes the live copy from the vault so Talos sees identical content.
#   5. Prints the registry lines to add (README + MANIFEST), then run
#      ./scripts/vault-manifest.sh --write.
#
# It does NOT push. Review, then ./scripts/vault-push.sh "import ...".
#
# Safe: refuses symlinks (package-managed content belongs in
# registries/_externals.md), refuses secret-looking files, never touches the
# live copy until the import is in place.

set -euo pipefail

VAULT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_DIR="$VAULT_DIR/skills"
EXTERNALS="$VAULT_DIR/registries/_externals.md"
CHANGED=0

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
RED='\033[0;31m'
RESET='\033[0m'

log()  { echo -e "${CYAN}▶${RESET} $*"; }
ok()   { echo -e "${GREEN}✅${RESET} $*"; }
warn() { echo -e "${YELLOW}⚠${RESET}  $*"; }
die()  { echo -e "${RED}✗${RESET} $*" >&2; exit 1; }

usage() {
  sed -n '2,30p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
  exit "${1:-0}"
}

NAME=""
CATEGORY=""
FROM_ROOT=""
DRY_RUN=false
FORCE=false
KEEP_LIVE=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --category|-c) CATEGORY="${2:?--category needs a value}"; shift 2 ;;
    --from)        FROM_ROOT="${2:?--from needs a value}"; shift 2 ;;
    --dry-run)     DRY_RUN=true; shift ;;
    --force)       FORCE=true; shift ;;
    --keep-live)   KEEP_LIVE=true; shift ;;
    -h|--help)     usage 0 ;;
    -*)            die "unknown flag: $1" ;;
    *)             [[ -z "$NAME" ]] || die "only one skill name at a time"; NAME="$1"; shift ;;
  esac
done

[[ -n "$NAME" ]] || usage 1
[[ -n "$CATEGORY" ]] || die "--category is required (bilan, general, genies, nerds, forges, platform, knowledge)"

ROOTS=()
if [[ -n "$FROM_ROOT" ]]; then
  ROOTS=("$FROM_ROOT")
else
  ROOTS=("$HOME/.agents/skills" "$HOME/.pi/agent/skills")
fi

# ── locate the installed copy ────────────────────────────────────────────────
SOURCE=""
for root in "${ROOTS[@]}"; do
  for candidate in "$root/$NAME" "$root"/*/"$NAME"; do
    if [[ -e "$candidate" || -L "$candidate" ]]; then
      SOURCE="$candidate"
      break 2
    fi
  done
done
[[ -n "$SOURCE" ]] || die "skill not found in: ${ROOTS[*]}"

if [[ -L "$SOURCE" ]]; then
  die "'$NAME' is a symlink (${SOURCE} -> $(readlink "$SOURCE")).
   Package-managed content is not vendored. Add it to registries/_externals.md instead,
   or copy the target into a normal directory first if you really mean to fork it."
fi
[[ -d "$SOURCE" ]] || die "not a directory: $SOURCE"
[[ -f "$SOURCE/SKILL.md" ]] || die "no SKILL.md in $SOURCE"
[[ "$(basename "$SOURCE")" == "$NAME" ]] || die "directory name does not match: $SOURCE"

# ── gate: declared external? ─────────────────────────────────────────────────
if [[ -f "$EXTERNALS" ]] && grep -q "\`$NAME\`" "$EXTERNALS"; then
  die "'$NAME' is declared external in registries/_externals.md.
   Delete that row first if the ownership actually changed — do not create a fork by accident."
fi

# ── gate: frontmatter + secrets ──────────────────────────────────────────────
python3 - "$SOURCE" "$NAME" <<'PY' || exit 1
import re, sys
from pathlib import Path
try:
    import yaml
except ImportError:
    sys.exit("vault-import: PyYAML required (pip install pyyaml)")

src, name = Path(sys.argv[1]), sys.argv[2]
raw = (src / "SKILL.md").read_text(encoding="utf-8", errors="replace")
if not raw.startswith("---"):
    sys.exit("vault-import: SKILL.md has no frontmatter")
parts = raw.split("---", 2)
if len(parts) < 3:
    sys.exit("vault-import: unterminated frontmatter")
try:
    meta = yaml.safe_load(parts[1]) or {}
except yaml.YAMLError as exc:
    sys.exit(f"vault-import: bad YAML frontmatter: {exc}")
if meta.get("name") != name:
    sys.exit(f"vault-import: frontmatter name {meta.get('name')!r} != directory {name!r}")
desc = str(meta.get("description") or "").strip()
if len(desc) < 40:
    sys.exit("vault-import: description too short to route on (needs >= 40 chars)")

secret = re.compile(
    r"(-----BEGIN [A-Z ]*PRIVATE KEY-----|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}"
    r"|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9-]{10,}|password\s*[:=]\s*\S{6,})", re.I)
home = re.compile(r"(/home/(?!capicuaman/)[a-z0-9_.-]+/|/Users/[A-Za-z0-9_.-]+/)")
for path in sorted(src.rglob("*")):
    if not path.is_file() or path.is_symlink():
        continue
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        continue
    for match in secret.finditer(text):
        sys.exit(f"vault-import: possible secret in {path.relative_to(src)}: {match.group(0)[:40]}")
    for match in home.finditer(text):
        print(f"  warn: machine-local path in {path.relative_to(src)}: {match.group(0)}", file=sys.stderr)
PY

size_kb=$(du -sk "$SOURCE" | cut -f1)
if (( size_kb > 5120 )); then
  warn "source is $((size_kb/1024)) MB — consider trimming it (book-to-skill keeps only SKILL.md + references)"
fi
find "$SOURCE" \( -name .git -o -name node_modules -o -name __pycache__ \) -prune -print | while read -r junk; do
  warn "excluding $junk from the import"
done

DEST="$SKILLS_DIR/$CATEGORY/$NAME"
if [[ -e "$DEST" && "$FORCE" == "false" ]]; then
  die "destination already exists: ${DEST#"$VAULT_DIR"/} (use --force to overwrite)"
fi

log "import: $SOURCE → ${DEST#"$VAULT_DIR"/} (${size_kb} KB)"
if [[ "$DRY_RUN" == "true" ]]; then
  echo "  [dry-run] gates passed; nothing copied"
  exit 0
fi

mkdir -p "$SKILLS_DIR/$CATEGORY"
if [[ -e "$DEST" ]]; then
  rm -rf "$DEST"
fi
rsync -a --exclude .git --exclude node_modules --exclude __pycache__ "$SOURCE/" "$DEST/"
CHANGED=1
ok "copied into the vault"

# Refresh the live copy so the vault is the single source of truth and Talos
# reports identical content (not drift).
if [[ "$KEEP_LIVE" == "false" ]]; then
  if [[ "$SOURCE" != "$DEST" ]]; then
    rm -rf "$SOURCE"
    cp -r "$DEST" "$SOURCE"
    ok "live copy refreshed from vault: $SOURCE"
  fi
fi

echo ""
echo -e "${CYAN}Next steps${RESET}"
echo "  1. Add the name to README.md (category table + counts)."
echo "  2. Run ./scripts/vault-manifest.sh --write"
echo "  3. python3 scripts/vault-audit.py --short     # expect no zombie/orphan"
echo "  4. ./scripts/vault-push.sh \"import $NAME into $CATEGORY\""
echo ""
echo "If this skill should NOT be installed on every machine, say so in its"
echo "description and keep machine prerequisites in a 'Prerequisites' section."
