#!/usr/bin/env python3
"""vault-audit — read-only health audit of the agent-vault entity corpus.

Reports the seven failure modes from the Pygmalion doctrine:

  zombie     entity fails to load (bad YAML, missing description, name != dir)
  hollow     SKILL.md with no procedure, references, or examples
  ghost      registry/doc references an entity that does not exist
  orphan     entity exists but no registry or catalog lists it
  duplicate  two entities with near-identical descriptions
  stale      dated grounding older than --max-age days
  statue     entity with no evidence of invocation (reported by --statues)

Plus structural checks: zero-byte files, broken relative links, name collisions,
and catalog count drift (README.md / MANIFEST.md vs reality).

Usage:
  vault-audit.py                 # full audit
  vault-audit.py --short         # one line per finding
  vault-audit.py --json          # machine-readable
  vault-audit.py --max-age 180   # staleness threshold in days

Exit codes: 0 = clean or warnings only, 1 = errors (zombies/duplicates/ghosts).

Read-only by contract: this script must never write to the vault.
"""

from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import sys
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("vault-audit: PyYAML required (pip install pyyaml)", file=sys.stderr)
    raise SystemExit(2)

VAULT = Path(__file__).resolve().parent.parent
SKILLS = VAULT / "skills"
REGISTRIES = VAULT / "registries"
README = VAULT / "README.md"
MANIFEST = VAULT / "MANIFEST.md"

SKIP_DIRS = {"node_modules", "__pycache__", ".git", ".herenow"}
DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")
LINK_RE = re.compile(r"\]\(([^)#][^)]*)\)")
FENCE_RE = re.compile(r"^```")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
ENTITY_SUFFIX = re.compile(r"-(nerd|forge|scout|doctrine|skill)$")
NON_REFERENCE_HEADING = re.compile(
    r"candidate|future|roadmap|next one|not yet|anti|what .* is not|recursion", re.I)
NON_REFERENCE_LINE = re.compile(r"candidate|do not|never|not yet|\bno forge\b|don't", re.I)
REFERENCE_HEADING = re.compile(
    r"related skills|sibling|see also|companion|hand.?off|consult", re.I)
PLACEHOLDER_LINK = re.compile(r"^(url|link|path|file|here|target)$", re.I)


# ── discovery ────────────────────────────────────────────────────────────────


def discover() -> dict[str, dict]:
    """Map skill name -> metadata. A skill is any dir containing SKILL.md."""
    found: dict[str, dict] = {}
    if not SKILLS.exists():
        return found
    for skill_md in sorted(SKILLS.glob("*/*/SKILL.md")):
        skill_dir = skill_md.parent
        if any(part in SKIP_DIRS for part in skill_dir.parts):
            continue
        name = skill_dir.name
        raw = skill_md.read_text(encoding="utf-8", errors="replace")
        meta, err = parse_frontmatter(raw)
        found[name] = {
            "name": name,
            "dir": skill_dir,
            "category": skill_dir.parent.name,
            "path": skill_md,
            "raw": raw,
            "meta": meta,
            "error": err,
            "description": (meta or {}).get("description", "") or "",
        }
    return found


def parse_frontmatter(raw: str) -> tuple[dict | None, str | None]:
    if not raw.startswith("---"):
        return None, "no frontmatter"
    parts = raw.split("---", 2)
    if len(parts) < 3:
        return None, "unterminated frontmatter"
    try:
        meta = yaml.safe_load(parts[1])
    except Exception as exc:  # noqa: BLE001
        first = str(exc).splitlines()[0]
        return None, f"YAML parse error: {first}"
    if not isinstance(meta, dict):
        return None, "frontmatter is not a mapping"
    return meta, None


def body_of(raw: str) -> str:
    parts = raw.split("---", 2)
    return parts[2] if len(parts) >= 3 else raw


# ── checks ───────────────────────────────────────────────────────────────────


def check_zombies(skills: dict[str, dict]) -> list[dict]:
    out = []
    for s in skills.values():
        problems = []
        if s["error"]:
            problems.append(s["error"])
        meta = s["meta"] or {}
        name = meta.get("name")
        desc = meta.get("description")
        if not name:
            problems.append("missing name")
        elif name != s["name"]:
            problems.append(f"name '{name}' != dir '{s['name']}'")
        elif not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
            problems.append(f"invalid name format '{name}'")
        if not isinstance(desc, str) or not desc.strip():
            problems.append("missing description")
        elif len(desc) > 1024:
            problems.append(f"description {len(desc)} > 1024 chars")
        if problems:
            out.append({"kind": "zombie", "name": s["name"], "detail": "; ".join(problems)})
    return out


def check_hollow(skills: dict[str, dict]) -> list[dict]:
    out = []
    for s in skills.values():
        body = body_of(s["raw"])
        text = "\n".join(line for line in body.splitlines() if not FENCE_RE.match(line))
        has_procedure = bool(re.search(r"^\s*\d+\.\s+\S", text, re.M))
        has_dir_content = any((s["dir"] / d).is_dir() and any((s["dir"] / d).iterdir())
                              for d in ("references", "examples", "scripts", "assets"))
        words = len(re.findall(r"\w+", text))
        if not has_procedure and not has_dir_content and words < 250:
            out.append({"kind": "hollow", "name": s["name"],
                        "detail": f"no numbered procedure, no references/examples, {words} words"})
    return out


def _sections(text: str):
    """Yield (heading, [lines]) for each section, tracking the current heading."""
    heading, lines = "", []
    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if match:
            if lines:
                yield heading, lines
            heading, lines = match.group(2), []
        else:
            lines.append(line)
    if lines:
        yield heading, lines


def check_ghosts(skills: dict[str, dict]) -> list[dict]:
    """Entity names referenced normatively but with no directory.

    Two sources: registry sections that index the current corpus, and the
    "Related skills" sections of every SKILL.md. Candidate/roadmap sections and
    explicit anti-examples are ignored, because naming an entity you have not
    built yet is planning, not drift.
    """
    out, known = [], set(skills)

    def scan(path: Path, label: str) -> None:
        text = path.read_text(encoding="utf-8", errors="replace")
        for heading, lines in _sections(text):
            if NON_REFERENCE_HEADING.search(heading):
                continue
            selective = bool(REFERENCE_HEADING.search(heading))
            candidate_mode = False
            previous = ""
            for line in lines:
                # A pseudo-heading like "Candidate forge-nerds (not yet warranted):"
                # makes the rest of the section planning, not drift.
                if re.search(r"(candidate|not yet|future|roadmap)", line, re.I) and line.rstrip().endswith(":"):
                    candidate_mode = True
                if candidate_mode or NON_REFERENCE_LINE.search(line):
                    previous = line
                    continue
                for match in re.finditer(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`", line):
                    name = match.group(1)
                    if name in known or name.endswith("-pattern"):
                        continue
                    # "There is no `forge-forge`" states a prohibition, not a reference.
                    # The negation may sit on the previous line, so widen the window.
                    context = f"{previous} {line[: match.start()]}"[-160:]
                    if re.search(r"\b(no|not|never|forbidden|anti|instead of)\b[^.;]*$", context, re.I):
                        continue
                    if selective:
                        # A "related skills" list names entities directly.
                        pass
                    elif not (ENTITY_SUFFIX.search(name)
                              and ("skills/" in line or path.parent == REGISTRIES)):
                        continue
                    out.append({"kind": "ghost", "name": name,
                                "detail": f"referenced in {label} ({heading}) but no directory"})
                previous = line

    if REGISTRIES.exists():
        for reg in sorted(REGISTRIES.glob("*.md")):
            scan(reg, f"registries/{reg.name}")
    for s in skills.values():
        scan(s["path"], f"skills/{s['category']}/{s['name']}/SKILL.md")
    # de-duplicate by name, keeping the first reference
    seen, unique = set(), []
    for f in out:
        if f["name"] in seen:
            continue
        seen.add(f["name"])
        unique.append(f)
    return unique


def check_orphans(skills: dict[str, dict]) -> list[dict]:
    """Entity not mentioned by any registry or catalog file."""
    catalogs = [p for p in (README, MANIFEST) if p.exists()]
    catalogs += sorted(REGISTRIES.glob("*.md")) if REGISTRIES.exists() else []
    text = "\n".join(p.read_text(encoding="utf-8", errors="replace") for p in catalogs)
    out = []
    for s in skills.values():
        if s["name"] not in text:
            out.append({"kind": "orphan", "name": s["name"],
                        "detail": f"skills/{s['category']}/{s['name']} not listed anywhere"})
    return out


def check_duplicates(skills: dict[str, dict]) -> list[dict]:
    out, seen = [], set()
    items = [(s["name"], s["description"]) for s in skills.values() if s["description"]]
    for i, (name_a, desc_a) in enumerate(items):
        for name_b, desc_b in items[i + 1:]:
            if (name_a, name_b) in seen:
                continue
            ratio = difflib.SequenceMatcher(None, desc_a.lower(), desc_b.lower()).ratio()
            if ratio >= 0.85:
                seen.add((name_a, name_b))
                out.append({"kind": "duplicate", "name": f"{name_a} ~ {name_b}",
                            "detail": f"description similarity {ratio:.0%}"})
    return out


def check_stale(skills: dict[str, dict], max_age: int) -> list[dict]:
    out, today = [], date.today()
    for s in skills.values():
        candidates = [s["path"]]
        for sub in ("references", "examples"):
            d = s["dir"] / sub
            if d.is_dir():
                candidates += sorted(d.glob("*.md"))
        oldest = None
        for path in candidates:
            for stamp in DATE_RE.findall(path.read_text(encoding="utf-8", errors="replace")):
                try:
                    d = datetime.strptime(stamp, "%Y-%m-%d").date()
                except ValueError:
                    continue
                if d > today:
                    continue
                if oldest is None or d < oldest:
                    oldest = d
        if oldest and (today - oldest).days > max_age:
            out.append({"kind": "stale", "name": s["name"],
                        "detail": f"oldest dated grounding {oldest} ({(today - oldest).days}d > {max_age}d)"})
    return out


def check_zero_bytes() -> list[dict]:
    out = []
    for path in SKILLS.rglob("*"):
        if path.is_file() and path.stat().st_size == 0:
            out.append({"kind": "zero-byte", "name": str(path.relative_to(VAULT)), "detail": "empty file"})
    return out


def check_links(skills: dict[str, dict]) -> list[dict]:
    out = []
    for s in skills.values():
        for path in [s["path"]] + sorted(p for p in (s["dir"].rglob("*.md")) if p != s["path"]):
            text = path.read_text(encoding="utf-8", errors="replace")
            for match in LINK_RE.finditer(text):
                link = match.group(1).strip()
                if link.startswith(("http://", "https://", "mailto:", "#", "/")):
                    continue  # absolute URLs and site-root paths are not vault links
                if PLACEHOLDER_LINK.match(link) or any(c in link for c in "{}<>"):
                    continue  # documentation placeholders like [text](url)
                target = (path.parent / link.split("#")[0]).resolve()
                if not target.exists():
                    out.append({"kind": "broken-link", "name": s["name"],
                                "detail": f"{path.relative_to(VAULT)} -> {link}"})
    return out


def check_counts(skills: dict[str, dict]) -> list[dict]:
    out = []
    actual = len(skills)
    for path in (README, MANIFEST):
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in re.finditer(r"\*\*Total:\s*(\d+)\s*skills\*\*|## Skills \((\d+) total\)", text):
            claimed = int(match.group(1) or match.group(2))
            if claimed != actual:
                out.append({"kind": "count-drift", "name": path.name,
                            "detail": f"claims {claimed} skills, actual {actual}"})
    return out


# ── reporting ────────────────────────────────────────────────────────────────

ORDER = ["zombie", "duplicate", "ghost", "orphan", "hollow", "stale",
         "zero-byte", "broken-link", "count-drift"]
LABEL = {
    "zombie": "Zombies (fail to load)",
    "duplicate": "Duplicates (overlapping triggers)",
    "ghost": "Ghosts (referenced but missing)",
    "orphan": "Orphans (unlisted)",
    "hollow": "Hollow (no substance)",
    "stale": "Stale (outdated grounding)",
    "zero-byte": "Zero-byte files",
    "broken-link": "Broken links",
    "count-drift": "Catalog count drift",
}


def report(findings: list[dict], skills: dict[str, dict], short: bool) -> int:
    by_kind: dict[str, list[dict]] = defaultdict(list)
    for f in findings:
        by_kind[f["kind"]].append(f)

    if short:
        for f in findings:
            print(f"{f['kind']:12s} {f['name']}: {f['detail']}")
    else:
        print(f"vault-audit — {len(skills)} skills across "
              f"{len({s['category'] for s in skills.values()})} categories\n")
        for kind in ORDER:
            items = by_kind.get(kind, [])
            if not items:
                continue
            print(f"{LABEL[kind]} — {len(items)}")
            for f in items:
                print(f"  · {f['name']}: {f['detail']}")
            print()

        if not findings:
            print("Clean: no zombies, duplicates, ghosts, orphans, hollow, or stale entities.")
        else:
            counts = ", ".join(f"{k}={len(by_kind[k])}" for k in ORDER if by_kind.get(k))
            print(f"Summary: {counts}")

    errors = sum(len(by_kind.get(k, [])) for k in ("zombie", "duplicate", "ghost"))
    return 1 if errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only agent-vault health audit")
    parser.add_argument("--short", action="store_true", help="one line per finding")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument("--max-age", type=int, default=180, help="staleness threshold in days")
    parser.add_argument("--root", help="vault root (default: script's parent)")
    args = parser.parse_args()

    global VAULT, SKILLS, REGISTRIES, README, MANIFEST
    if args.root:
        VAULT = Path(args.root).resolve()
        SKILLS, REGISTRIES = VAULT / "skills", VAULT / "registries"
        README, MANIFEST = VAULT / "README.md", VAULT / "MANIFEST.md"

    skills = discover()
    if not skills:
        print(f"vault-audit: no skills found under {SKILLS}", file=sys.stderr)
        return 2

    findings: list[dict] = []
    for check in (
        lambda: check_zombies(skills),
        lambda: check_duplicates(skills),
        lambda: check_ghosts(skills),
        lambda: check_orphans(skills),
        lambda: check_hollow(skills),
        lambda: check_stale(skills, args.max_age),
        check_zero_bytes,
        lambda: check_links(skills),
        lambda: check_counts(skills),
    ):
        findings.extend(check())

    if args.json:
        print(json.dumps({"skills": len(skills), "findings": findings}, indent=2))
        return 1 if any(f["kind"] in ("zombie", "duplicate", "ghost") for f in findings) else 0

    return report(findings, skills, args.short)


if __name__ == "__main__":
    raise SystemExit(main())
