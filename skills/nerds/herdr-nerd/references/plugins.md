# Herdr plugins

Grounded in https://herdr.dev/plugins/ (captured 2026-10-06) and https://herdr.dev/docs/ plugin + marketplace sections.

## Marketplace model
- **Discovery:** any public GitHub repo tagged with the topic `herdr-plugin`.
- **Manifest:** `herdr-plugin.toml` at the repo root defines actions and event hooks.
- **No submission, no review queue.** The index auto-refreshes.
- **Install:** `herdr plugin install <...>`
- **Trust posture:** "Listings aren't reviewed by Herdr, so install at your own discretion." Point users to the Trust guidance link on the plugins page before mass-installing.

## Publishing (for authors)
1. Create a public GitHub repo.
2. Add a `herdr-plugin.toml` manifest with your actions and event hooks.
3. Add the GitHub topic `herdr-plugin`.
4. Wait for the next index refresh. Done — no PR, no approval.

Full authoring guide: https://herdr.dev/docs/ → Plugins section ("Author a plugin" / "Write a plugin").

## Discovery sorts (on herdr.dev/plugins/)
- **Trending this week** — fastest-growing repos relative to their own size.
- **New to the herd** — recently joined.
- **Popular / Trending / Recently updated / Newest** — full index sort controls.

## Scale (homepage snapshot)
- Aug 2026: 762 community plugins.
- Expect that number to be stale — the marketplace is in open-publish mode.

## Nerd advice when the user asks about plugins
1. **Need discovery?** Point them at https://herdr.dev/plugins/ with a sort tip (Trending for momentum, Popular for stability, Newest for exploration).
2. **Want to publish?** Walk the 4-step publish flow above. Mention there's no review queue — that's a feature AND a trust surface.
3. **Want to vet before installing?** Read the repo's `herdr-plugin.toml`, check the action list, check the event hooks it registers, skim recent commits. The runtime executes what the manifest declares.
4. **Author a plugin?** The docs' plugin authoring page covers manifest actions + event hooks. Local executable workflow plugins is the stated primitive.
