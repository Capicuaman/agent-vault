#!/usr/bin/env python3
"""anki_admin.py - safe Anki collection administration for this machine.

Read-only commands (audit, stats, decks, drill) operate on a *snapshot copy* of
the collection and are safe to run while the Anki GUI is open.

Write commands (enable-fsrs, set-options, backup) refuse to run while Anki is
open, because Anki holds the collection open and concurrent writes can corrupt it.

Usage:
  anki_admin.py audit [--json]
  anki_admin.py decks
  anki_admin.py stats
  anki_admin.py drill [--count N] [--seed S] [--deck NAME] [--json]
  anki_admin.py enable-fsrs
  anki_admin.py set-options [--retention 0.9] [--new-per-day 15] [--reviews-per-day 200]
                             [--learn-steps "1 10"] [--relearn-steps "10"] [--leech 8]
  anki_admin.py backup [--dest DIR]

Environment:
  ANKI_PROFILE   profile name (default: first profile found, usually "User 1")
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ANKI_BASE = Path(
    os.environ.get("ANKI_BASE", Path.home() / ".local" / "share" / "Anki2")
)


# ---------------------------------------------------------------- safety ----
def anki_running() -> bool:
    """True if the Anki GUI process is running."""
    try:
        out = subprocess.run(
            ["pgrep", "-af", r"/usr/bin/anki"],
            capture_output=True,
            text=True,
        ).stdout
    except FileNotFoundError:
        out = ""
    # exclude this very script's cmdline if it happens to match
    return any("/usr/bin/anki" in line for line in out.splitlines())


def profile_dir() -> Path:
    prof = os.environ.get("ANKI_PROFILE")
    if prof:
        p = ANKI_BASE / prof
        if not (p / "collection.anki2").exists():
            sys.exit(f"error: no collection in {p}")
        return p
    candidates = sorted(
        p for p in ANKI_BASE.iterdir() if (p / "collection.anki2").exists()
    )
    if not candidates:
        sys.exit(f"error: no Anki profile found under {ANKI_BASE}")
    return candidates[0]


def snapshot() -> tuple[Path, tempfile.TemporaryDirectory]:
    """Copy the live collection (including WAL) to a temp dir and return the path."""
    src = profile_dir()
    tmp = tempfile.TemporaryDirectory(prefix="anki_snap_")
    dst = Path(tmp.name)
    for name in ("collection.anki2", "collection.anki2-wal", "collection.anki2-shm"):
        f = src / name
        if f.exists():
            shutil.copy2(f, dst / name)
    media = src / "collection.media"
    if media.exists():
        shutil.copytree(media, dst / "collection.media", dirs_exist_ok=True)
    return dst / "collection.anki2", tmp


def open_col(path: Path):
    from anki.collection import Collection  # imported lazily

    return Collection(str(path))


def require_closed() -> None:
    # A custom ANKI_BASE points at a collection the running GUI is not using,
    # so the check only applies to the real profile location.
    default_base = Path.home() / ".local" / "share" / "Anki2"
    if ANKI_BASE == default_base and anki_running():
        sys.exit(
            "error: Anki is currently running. Close it first (File > Quit), then re-run.\n"
            "       Read-only commands (audit/stats/decks/drill) work while Anki is open."
        )


# ---------------------------------------------------------------- commands ---
def cmd_audit(args: argparse.Namespace) -> None:
    colpath, tmp = snapshot()
    col = open_col(colpath)
    try:
        notes = col.note_count()
        cards = col.card_count()
        decks = [(d.id, d.name) for d in col.decks.all_names_and_ids()]

        # card state breakdown
        states = {"new": 0, "learning": 0, "review": 0, "relearn": 0, "suspended": 0}
        for c in col.find_cards(""):
            card = col.get_card(c)
            if card.queue == -1:
                states["suspended"] += 1
            elif card.type == 0:
                states["new"] += 1
            elif card.type == 1:
                states["learning"] += 1
            elif card.type == 2:
                states["review"] += 1
            elif card.type == 3:
                states["relearn"] += 1

        # deck -> card counts
        per_deck = {}
        for did, name in decks:
            per_deck[name] = col.db.scalar(
                "select count() from cards where did=?", did
            ) or 0

        fsrs_on = bool(col.get_config("fsrs", False))
        cfg = col.decks.config_dict_for_deck_id(decks[0][0]) if decks else {}
        revlog = col.db.scalar("select count() from revlog") or 0
        info = {
            "profile": profile_dir().name,
            "collection": str(profile_dir() / "collection.anki2"),
            "notes": notes,
            "cards": cards,
            "reviews_logged": revlog,
            "decks": per_deck,
            "card_states": states,
            "fsrs_enabled": fsrs_on,
            "desired_retention": cfg.get("desiredRetention"),
            "new_per_day": (cfg.get("new") or {}).get("perDay"),
            "reviews_per_day": (cfg.get("rev") or {}).get("perDay"),
            "learning_steps_min": (cfg.get("new") or {}).get("delays"),
            "relearning_steps_min": (cfg.get("lapse") or {}).get("delays"),
            "leech_threshold": (cfg.get("lapse") or {}).get("leechFails"),
            "backups": sorted(
                p.name for p in (profile_dir() / "backups").glob("*")
            )
            if (profile_dir() / "backups").exists()
            else [],
            "addons": [p.name for p in (ANKI_BASE / "addons21").iterdir()]
            if (ANKI_BASE / "addons21").exists()
            else [],
        }
        if args.json:
            print(json.dumps(info, indent=2))
            return
        print(f"Profile:            {info['profile']}")
        print(f"Collection:         {info['collection']}")
        print(f"Notes / cards:      {info['notes']} / {info['cards']}")
        print(f"Reviews ever:       {info['reviews_logged']}")
        print(f"FSRS enabled:       {info['fsrs_enabled']}")
        print(f"Desired retention:  {info['desired_retention']}")
        print(f"New/day:            {info['new_per_day']}")
        print(f"Reviews/day cap:    {info['reviews_per_day']}")
        print(f"Learn steps (min):  {info['learning_steps_min']}")
        print(f"Relearn steps (min):{info['relearning_steps_min']}")
        print(f"Leech threshold:    {info['leech_threshold']}")
        print(f"Card states:        {info['card_states']}")
        print("Decks:")
        for name, n in info["decks"].items():
            print(f"  - {name}: {n} cards")
        print(f"Backups:            {info['backups'] or 'NONE'}")
        print(f"Add-ons:            {info['addons'] or 'none'}")
    finally:
        col.close()
        tmp.cleanup()


def cmd_decks(args: argparse.Namespace) -> None:
    colpath, tmp = snapshot()
    col = open_col(colpath)
    try:
        for d in col.decks.all_names_and_ids():
            n = col.db.scalar("select count() from cards where did=?", d.id) or 0
            print(f"{d.id}\t{d.name}\t{n}")
    finally:
        col.close()
        tmp.cleanup()


def cmd_stats(args: argparse.Namespace) -> None:
    colpath, tmp = snapshot()
    col = open_col(colpath)
    try:
        print("Due today:")
        for label, query in (
            ("new", "is:new"),
            ("learning", "is:learn"),
            ("due review", "is:due"),
            ("suspended", "is:suspended"),
        ):
            print(f"  {label:12} {len(col.find_cards(query))}")
    finally:
        col.close()
        tmp.cleanup()


def cmd_drill(args: argparse.Namespace) -> None:
    colpath, tmp = snapshot()
    col = open_col(colpath)
    try:
        query = "is:new" if args.new else ""
        if args.deck:
            query = f'deck:"{args.deck}" ' + query
        ids = col.find_notes(query.strip())
        pairs = []
        for nid in ids:
            note = col.get_note(nid)
            fields = [f for f in note.fields]
            if len(fields) >= 2:
                pairs.append({"front": fields[0], "back": fields[1]})
        if not pairs:
            sys.exit("no notes matched")
        import random

        rng = random.Random(args.seed)
        rng.shuffle(pairs)
        pairs = pairs[: args.count]
        if args.json:
            print(json.dumps(pairs, indent=2, ensure_ascii=False))
        else:
            for i, p in enumerate(pairs, 1):
                print(f"{i}. {p['front']}")
                if args.reveal:
                    print(f"   -> {p['back']}")
    finally:
        col.close()
        tmp.cleanup()


def cmd_enable_fsrs(args: argparse.Namespace) -> None:
    require_closed()
    path = profile_dir() / "collection.anki2"
    col = open_col(path)
    try:
        col.set_config("fsrs", True)
        # FSRS wants short, same-day (re)learning steps
        cfg = col.decks.config_dict_for_deck_id(
            col.decks.all_names_and_ids()[0].id
        )
        cfg["new"]["delays"] = [1.0, 10.0]
        cfg["lapse"]["delays"] = [10.0]
        cfg.setdefault("desiredRetention", 0.9)
        col.decks.update_config(cfg)
        print("FSRS enabled; learning steps set to 1m/10m, relearn 10m.")
    finally:
        col.close()


def cmd_set_options(args: argparse.Namespace) -> None:
    require_closed()
    path = profile_dir() / "collection.anki2"
    col = open_col(path)
    try:
        for did, name in [(d.id, d.name) for d in col.decks.all_names_and_ids()]:
            cfg = col.decks.config_dict_for_deck_id(did)
            if args.retention is not None:
                cfg["desiredRetention"] = args.retention
            if args.new_per_day is not None:
                cfg["new"]["perDay"] = args.new_per_day
            if args.reviews_per_day is not None:
                cfg["rev"]["perDay"] = args.reviews_per_day
            if args.learn_steps is not None:
                cfg["new"]["delays"] = [float(x) for x in args.learn_steps.split()]
            if args.relearn_steps is not None:
                cfg["lapse"]["delays"] = [
                    float(x) for x in args.relearn_steps.split()
                ]
            if args.leech is not None:
                cfg["lapse"]["leechFails"] = args.leech
            col.decks.update_config(cfg)
            print(f"updated preset for deck: {name}")
    finally:
        col.close()


def cmd_backup(args: argparse.Namespace) -> None:
    require_closed()
    src = profile_dir()
    dest = Path(args.dest).expanduser() if args.dest else src / "backups"
    dest.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y-%m-%d-%H.%M.%S")
    out = dest / f"manual-{stamp}.colpkg"
    # .colpkg is a zip; build a minimal one from collection + media via the API
    col = open_col(src / "collection.anki2")
    try:
        tmp_zip = dest / f"manual-{stamp}.tmp"
        col.export_collection_package(
            out_path=str(tmp_zip),
            include_media=True,
            legacy=False,
        )
        if tmp_zip.exists():
            tmp_zip.replace(out)
        print(f"backup written: {out}")
    except Exception as e:  # fall back to a raw copy
        shutil.copy2(src / "collection.anki2", dest / f"manual-{stamp}.anki2")
        print(f"raw copy written (export failed: {e})")
    finally:
        try:
            col.close()
        except Exception:
            pass


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("audit")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_audit)

    p = sub.add_parser("decks")
    p.set_defaults(func=cmd_decks)

    p = sub.add_parser("stats")
    p.set_defaults(func=cmd_stats)

    p = sub.add_parser("drill")
    p.add_argument("--count", type=int, default=10)
    p.add_argument("--seed", type=int, default=None)
    p.add_argument("--deck", default=None)
    p.add_argument("--new", action="store_true", help="only new cards")
    p.add_argument("--reveal", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_drill)

    p = sub.add_parser("enable-fsrs")
    p.set_defaults(func=cmd_enable_fsrs)

    p = sub.add_parser("set-options")
    p.add_argument("--retention", type=float, default=None)
    p.add_argument("--new-per-day", type=int, default=None)
    p.add_argument("--reviews-per-day", type=int, default=None)
    p.add_argument("--learn-steps", default=None, help='e.g. "1 10" (minutes)')
    p.add_argument("--relearn-steps", default=None, help='e.g. "10" (minutes)')
    p.add_argument("--leech", type=int, default=None)
    p.set_defaults(func=cmd_set_options)

    p = sub.add_parser("backup")
    p.add_argument("--dest", default=None)
    p.set_defaults(func=cmd_backup)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
