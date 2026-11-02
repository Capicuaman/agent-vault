# Anki operating procedures — evidence-based SOP

Sources: Anki manual (docs.ankiweb.net — Studying, Deck Options, Leeches, Backups,
Syncing) and Dr Piotr Woźniak's *20 rules of knowledge formulation* (SuperMemo).
Compiled for the anki-admin skill.

## 1. Scheduler: turn FSRS on, and keep it simple

- **Enable FSRS** (Free Spaced Repetition Scheduler). It models forgetting more
  accurately than legacy SM-2 and "can help you remember more material in the
  same amount of time". It is a global setting.
- **Desired retention: 0.9** (90%) is the default and the best starting point.
  >90% makes workload climb steeply; never exceed 97%. Only raise it if you
  explicitly want to trade more daily reviews for higher recall.
- **Learning/relearning steps must be under 1 day** and minimal. FSRS schedules
  the optimum; long steps fight it. Good: `1m 10m`, relearn `10m`.
  Repeating a card many times in one day does not build long-term memory.
- **Optimise later.** The optimiser needs a few hundred reviews to learn your
  memory. Run *Optimize* about once a month once you have history.
- **Do not press Hard when you forgot.** Hard = correct-but-hesitant. Pressing
  Hard on a failure makes FSRS schedule intervals that are far too long.
  Again = failure. Good = correct with effort. Easy = instant.
- Avoid add-ons that change intervals — they conflict with FSRS.

## 2. Formulating cards (the 20 rules, condensed)

The single biggest lever on retention is card quality, not settings.

1. **Do not learn what you do not understand.** Understand first, then memorise.
2. **Minimum information principle** — one fact per card. Split compound facts.
3. **Avoid lists/sets/enumerations.** Use cloze deletion on each item instead.
4. **Use cloze deletion** — fast and mnemonically powerful.
5. **Add context / personalise** — examples, your own story, why it matters.
6. **Use images and mnemonics** where they help.
7. **Use redundancy** — ask the same idea from different angles.
8. **Use references** — keep the source so you can rebuild context.
9. **Start from basics** before complexity.
10. **Pleasure test**: if reviewing feels bad, a rule above is being violated.

Meta-rules: prefer *rules* over facts (more applicable); use knowledge in real
life; review in the morning at your creative peak.

## 3. Daily study discipline

- **New cards/day is the throttle.** 20 new/day roughly becomes ~200
  reviews/day. Start at 10–20; lower it if reviews pile up. More than one Anki
  user has "excitedly studied hundreds of new cards" then drowned in reviews.
- If you have a review backlog, **stop introducing new cards** until caught up.
- **~10 second rule**: if you can't recall within ~10s, show the answer and
  grade honestly.
- Button mix guideline: Again 5–20%, Good 80–95%, Hard/Easy sparingly.
  Be strict: a fail in real life is a fail in Anki.
- Review in one or two focused sessions; don't study tired right before sleep.

## 4. Leeches (cards you keep forgetting)

- Default: at **8 lapses** the note is tagged `leech` and (optionally) suspended.
- Handle by, in order of preference: **rewrite** the card (apply the 20 rules),
  **delete** it if not important, or **suspend** and let interference fade.
- Interference example: confusing *disappoint* / *disappear* — learn one, park
  the other, then unsuspend.

## 5. Backups — never rely on one copy

- Automatic backups run every ~30 min and on major operations, but are **local
  only** and exclude media. They do not survive disk failure or theft.
- Create a **manual .colpkg including media** periodically (File > Export) and
  store it off-device (cloud/USB). `File > Create Backup` is quick but excludes
  media.
- **Sync to AnkiWeb** daily — it also protects against device loss.
- Don't study the same collection on two devices without syncing first
  (conflict resolution is lossy).

## 6. Collection hygiene

- Decks should hold **broad categories**, not micro-topics. Use the browser,
  tags, and search instead of making a deck per lesson.
- **Bury siblings** is on by default so related cards don't appear together.
- Use **flags** for "look this up later", tags for structure.
- Check `Tools > Check Database` after crashes or sync issues.

## 7. This machine — known facts

- Anki 26.08.1, Arch package, profile "User 1".
- Collection: `~/.local/share/Anki2/User 1/collection.anki2`.
- Deck `Irregular Verbs` imported from `~/Downloads/irregular_verbs_anki.txt`
  (base form → simple past). 116 notes, all new, zero reviews at last audit.
- No add-ons installed. FSRS must be enabled.
- Anki must be **closed** before any write to the collection.
