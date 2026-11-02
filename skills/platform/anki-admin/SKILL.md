---
name: anki-admin
description: >
  REQUIRED whenever the user asks about Anki on this machine: reviewing,
  studying, retention, scheduling, deck options, FSRS, card quality, backups,
  syncing, importing decks, leeches, "drill me", "quiz me on my cards", or
  "what should I study". Owns the Anki collection at
  ~/.local/share/Anki2/User 1/collection.anki2. Triggers: Anki, flashcard,
  spaced repetition, SRS, FSRS, retention, review, deck, card, leech, drill,
  quiz me, irregular verbs, memorize, study plan.
---

# Anki Admin Skill

This skill makes you the maintainer of the user's Anki collection. Your job:
keep the scheduler healthy, keep cards high-quality, protect the data, and
actively drill the user when asked or when a review session is due.

## Hard safety rule

**Never write to the collection while the Anki GUI is open.** Anki holds the
collection open; concurrent writes can corrupt it. The helper script enforces
this. Read-only commands (`audit`, `stats`, `decks`, `drill`) work on a snapshot
copy and are always safe.

## Prerequisites

- Anki installed with its Python API importable (`anki` package), plus `python3`.
- The collection at `~/.local/share/Anki2/User 1/collection.anki2`. If the
  profile name differs on this machine, adjust it; the helper refuses writes
  while the GUI is open. All state lives in the collection, so this skill is
  portable to any machine that has Anki.
- The script lives next to this file. Resolve the skill directory from the
  install root in use, not from a hardcoded one.

## The tool

`scripts/anki_admin.py` — a safe CLI around Anki's own Python API.

```bash
for root in "${PI_SKILLS_DIR:-}" "$HOME/.agents/skills" "$HOME/.pi/agent/skills"; do
  [[ -n "$root" && -f "$root/anki-admin/scripts/anki_admin.py" ]] && SKILL_DIR="$root/anki-admin" && break
done

S="$SKILL_DIR/scripts/anki_admin.py"

python3 "$S" audit [--json]        # full state report (read-only, safe anytime)
python3 "$S" stats                 # due counts today
python3 "$S" decks                 # deck list with card counts
python3 "$S" drill --count 10 --json          # random Q/A pairs (safe anytime)
python3 "$S" drill --count 10 --new           # only unseen cards
python3 "$S" enable-fsrs           # turn FSRS on + short steps (Anki must be closed)
python3 "$S" set-options --retention 0.9 --new-per-day 15   # (Anki must be closed)
python3 "$S" backup --dest ~/Backups            # .colpkg incl. media (Anki closed)
```

Add `2>&1 | grep -v truststore` to silence a harmless Python warning.

## Default operating procedure

1. **Start every Anki request with `audit`.** Report the state before acting.
2. **Enforce the baseline settings** (see `references/best-practices.md`):
   - FSRS enabled, desired retention **0.9**, learning steps `1m 10m`,
     relearn `10m`, leech threshold 8.
   - New cards/day is the workload throttle — 10–20 for a beginner. Ask the
     user's daily time budget before raising it.
3. **Protect the data.** Confirm a recent backup exists and that the user
   syncs to AnkiWeb. Offer `backup` after meaningful changes.
4. **Guard card quality.** Apply the SuperMemo 20 rules (see reference). When
   reviewing a deck, flag: compound cards, lists, cards without context, and
   leeches. Propose concrete rewrites.
5. **Never press Hard for a forgotten card** — tell the user Again. Hard is a
   passing grade.
6. **If a review backlog exists, stop new cards** until it clears.

## Drilling the user

When the user says "drill me", "quiz me", or a session is due:

1. Run `drill --count N --json` to pull Q/A pairs (default N=10; use `--new`
   for unseen cards). Use `--deck "Name"` to focus.
2. Present **questions only**, numbered. Do not show answers yet.
3. Wait for the user's answers. Grade each: correct / wrong / partial.
4. Reveal the answers, mark what they missed, and explain the tricky ones.
5. Offer to turn repeated misses into better cards or a filtered drill.
6. Keep it to ~10 items per round unless asked otherwise.

## Applying settings changes

`enable-fsrs` and `set-options` need Anki closed. Workflow:

1. Tell the user to quit Anki (File > Quit) — or offer to do it via the
   computer-use skill if they want you to drive the GUI.
2. Run the command.
3. Run `audit` again to confirm the change took.

If the user prefers not to close Anki, guide them through the GUI instead:
Deck Options > FSRS (enable, retention 90%) and New Cards / Lapses.

## Reference

- `references/best-practices.md` — full SOP with sources (Anki manual +
  SuperMemo 20 rules). Read it before giving advice about scheduling or card
  formulation.
