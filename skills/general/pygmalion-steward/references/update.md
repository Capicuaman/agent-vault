# Update

How an entity changes without breaking the entities and habits that depend on it.

## Why updates are dangerous

Entities are not isolated documents:

- Registries index them.
- Other entities hand off to them.
- Installed copies exist on other machines.
- The description is a routing contract: changing it changes *when* the entity
  fires, which can silently steal or lose work from a sibling.

So an update is a small migration, not an edit.

## Versioning

Use `metadata.version` in frontmatter (semver-shaped):

```yaml
metadata:
  version: 1.2.0
```

| Change | Bump | Why |
|---|---|---|
| Description / triggers / scope | **major** | Routing contract changed; siblings may be affected |
| Procedure, rules, output shape | **minor** | Behavior changed for the same triggers |
| Grounding refresh, typos, links | **patch** | Same behavior, truer facts |

Keep a short changelog in the entity when it has external consumers:

```markdown
## Changelog
- 1.1.0 — added the shadow test to the evaluation gates
- 1.0.0 — initial
```

## Change classes

### Class A — Grounding refresh (safe)

Facts aged out; behavior should not change.

1. Re-verify commands, paths, versions against the real source.
2. Update the snapshot date.
3. Bump patch.
4. Run the audit.

No registry change. No announcement.

### Class B — Procedure change (coordinate)

The steps change but triggers do not.

1. Bump minor.
2. Update `examples/` if the family has them — an example that contradicts the
   procedure is worse than no example.
3. Check siblings that hand off to this one for now-incorrect claims.
4. Run the audit.

### Class C — Routing change (migrate)

The description, name, or scope changes. This is a breaking change.

1. Run the **trigger test** against the old and new description. Identify requests
   that would now route differently.
2. Find every entity that references the old trigger phrase:
   ```bash
   grep -rn "<old-name>\|<old-trigger>" skills/*/*/SKILL.md registries/*.md
   ```
3. Update the registry of record.
4. Update `README.md` / `MANIFEST.md` tables.
5. Bump major.
6. If the name changed: keep a redirect line in the registry
   (`old-name — renamed to new-name`), so ghosts do not appear later.

### Class D — Pattern registry change (corpus-wide migration)

Changing `_tech-nerd-pattern.md` or `_forge-pattern.md` changes the spec for
**every** artifact of that family.

1. Enumerate the affected entities:
   ```bash
   grep -rl "registries/_<family>-pattern.md" skills/*/*/SKILL.md
   ```
2. Decide per entity: conform now, conform later, or grandfather (and record why).
3. Amend the registry **and** the executable forge in the same change. Two specs
   for one family is a Duplicate at the spec level.
4. Run the audit; expect ghosts if any entity was renamed.
5. Bump the registry's own version.

This is the highest-risk class. Do it in its own commit.

## Supersede protocol

When an entity is replaced rather than edited:

1. Create the successor with the full new content.
2. In the old entity, add:
   ```yaml
   deprecated: true
   superseded_by: <successor-name>
   ```
   and a one-line banner at the top of the body.
3. Remove the old entity from the registry of record; add the successor.
4. Keep the file for one audit cycle. Deleting immediately creates ghosts in
   every reference you missed.
5. Delete after the audit reports no references.

**Never reuse a name.** A reused name makes every historical reference lie.

## Deprecation

Deprecation is not deletion. The sequence:

```
active → deprecated (still loads, warns, points to successor)
       → unregistered (no longer advertised; file remains)
       → deleted (after audit finds no references)
```

At the middle stage, the entity must still load — a deprecated entity that fails
to parse is a zombie, not a deprecation.

## Drift triggers

Re-evaluate an entity when any of these happen:

- The upstream tool or provider changes a version, default, or API.
- A new sibling is created with an adjacent trigger.
- The entity's own snapshot date passes the staleness threshold (180 days).
- The loader or host agent changes its skill spec.
- The vault moves to a different path or machine.
- The audit reports a new ghost pointing at this entity.

## The update checklist

- [ ] Bump `metadata.version` at the right level
- [ ] Re-run the trigger test if the description changed
- [ ] Update the registry of record
- [ ] Update `README.md` and `MANIFEST.md` counts if anything was added/removed
- [ ] Update sibling hand-offs that referenced the old behavior
- [ ] Refresh dated grounding and snapshot dates
- [ ] Run `python3 scripts/vault-audit.py`
- [ ] Confirm: no new zombie, ghost, duplicate, or orphan
- [ ] If superseding: banner + `superseded_by` + one audit cycle before deletion

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Silent rewrite of a doctrine others load | Every dependent entity now follows a spec nobody announced |
| Editing the installed copy instead of the vault | Fork; overwritten on next sync |
| Renaming without a redirect | Produces ghosts in every reference you did not grep |
| Deleting a superseded entity immediately | Breaks references you could not see |
| Changing a description without re-running the trigger test | Routing silently shifts work to a sibling |
| Updating the registry but not the executable forge | Two specs; artifacts diverge |
| Bumping patch for a routing change | Hides a breaking change from consumers |
