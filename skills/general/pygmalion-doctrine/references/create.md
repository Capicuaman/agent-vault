# Create

Sculpting procedure. This is the generic layer; family-specific shapes live in
the forges and registries (see [`taxonomy.md`](taxonomy.md)).

## Step 0 — Confirm the fit and the scope

Pick the family first ([`taxonomy.md`](taxonomy.md)). Then lock the three Ws:

1. **What** — one sentence: what it does, and what it refuses to do.
2. **Where** — vault category + scope (global or project).
3. **Why** — the behavior delta you expect. If you cannot name it, stop.

One scope question per entity. Do not start writing before it is answered.

## Step 1 — Declare the output shape

Write the exact file tree before writing any content. No "it depends."

```
<name>/
  SKILL.md
  references/
    <topic>.md
```

Family shapes you can inherit rather than invent:

| Family | Required shape | Source of truth |
|---|---|---|
| nerd | `SKILL.md` + `references/facts.md` + `references/commands.md` | `_tech-nerd-pattern.md` |
| forge | `SKILL.md` + `examples/<canonical>.md` | `_forge-pattern.md` |
| forge-nerd | `SKILL.md` + `references/` audit criteria | `_forge-pattern.md` |
| scout | `SKILL.md` + output card format | `_tech-nerd-pattern.md` |
| doctrine | `SKILL.md` + `references/` lenses | this file |
| genie | `SKILL.md` + `references/` artifacts | `skills/genies/README.md` |
| generic skill | `SKILL.md` + optional `references/`, `scripts/`, `assets/` | Agent Skills spec |

## Step 2 — Engineer the description

The description decides whether the statue ever wakes. Treat it as the product.

**Rules**

1. **Name the situation, not the topic.** "Use when the user asks about Hyprland
   keybindings" beats "Hyprland expertise".
2. **Include real activation phrases** — the words a user actually types, including
   symptoms from error messages.
3. **Include explicit invocation phrases** when the family has them
   (`<name>-nerd`, "nerd mode on", `git care`).
4. **State the non-goals inside the description** when a sibling could be confused.
   This is the cheapest routing fix that exists.
5. **Stay under 1024 characters.** The loader rejects longer descriptions.
6. **Write YAML that cannot break.** Prefer a folded block:
   ```yaml
   description: >-
     First line...
     second line...
   ```
   If you must use a quoted scalar, use single outer quotes and avoid inner
   quotes entirely. **Never** nest double quotes inside double quotes — that is
   how `bonanno-game-theory` silently stopped loading: its description was
   `"Knowledge base from "Game Theory: ..." by ..."`, the YAML parser failed, and
   the skill was absent from every session with no error shown to the user.

**The trigger test** (from [`evaluate.md`](evaluate.md)): five must-fire and five
must-not-fire utterances. Run it before you commit.

## Step 3 — Write the body in this order

1. **One-paragraph canon** — the thing this entity will not deviate from.
2. **When to use / when not to** — including explicit hand-offs.
3. **Procedure** — numbered; each step actionable; include failure branches and a
   verification step.
4. **Discipline rules** — the invariants specific to this entity.
5. **Anti-patterns** — what it refuses to do, with the reason.
6. **References** — relative links, resolved from the skill directory.

Do not put a procedure in prose. If a step cannot be checked, it is not a step.

## Step 4 — The six universal discipline rules

Generalized from `_forge-pattern.md`; they apply to every family.

1. **Named output shape.** Declared before building. No exceptions.
2. **Scope lock before build.** The three Ws answered.
3. **Serial writes inside a new folder.** Parallel writes into the same new
   directory race to 0-byte files.
4. **YAML that cannot break.** Folded scalar or single-quoted; never nested
   double quotes. Verify by parsing, not by eye.
5. **Register in the same build.** If registration is a follow-up chore, the
   corpus drifts within one session. Nerds and forges → pattern registry.
   Everything else → `README.md` and `MANIFEST.md`.
6. **Smoke test before claiming done.** State the activation triggers, confirm the
   files parse, and load the entity with the real loader.

## Step 5 — Verify, then claim done

```bash
# structural + corpus checks (read-only)
python3 scripts/vault-audit.py
```

The audit checks: frontmatter parses, name matches directory, description present
and within limits, no zero-byte files, relative links resolve, no ≥85% duplicate,
and that the catalogs' counts match reality.

Then confirm:

- [ ] All four gates pass; score ≥ 7/9
- [ ] Five must-fire and five must-not-fire utterances checked
- [ ] Output shape declared and matched
- [ ] Non-goals and hand-offs written
- [ ] Registry/catalog updated in the same change
- [ ] `metadata.version` set
- [ ] Audit reports no new zombie, ghost, duplicate, or orphan
- [ ] The behavior delta is stated in one sentence

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Creating a sibling because patching feels riskier | Forks the corpus; two half-entities route worse than one good one |
| Description written as a table of contents | Routes on topic, not situation; never fires on real phrasing |
| No non-goals | Becomes a catch-all and steals sibling routing |
| Procedure in prose | Not executable; the model improvises |
| Registering "later" | Drift begins immediately; the entity becomes an orphan |
| Claiming done from reading the file | Never tested the loader; zombies are invisible until absent |
| Copying a sibling wholesale | Produces a duplicate description and a routing collision |
