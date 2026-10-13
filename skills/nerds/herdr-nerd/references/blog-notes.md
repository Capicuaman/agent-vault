# Herdr release & direction notes

Dated chronology from https://herdr.dev/blog/ (captured 2026-10-06). Use these to answer "what's new?", "is it funded?", "where is it going?", and version-dating questions.

## 2026-09-08 — $6M seed led by Bessemer Venture Partners
Herdr raised a $6M seed led by Bessemer. **The runtime stays open (Apache 2.0).** Money goes to people. Pair this with the YC post (Aug 6) for the full funding picture.

## 2026-09-07 — "Connecting the machines" (Herdr 0.9)
Herdr 0.9's flagship: **local and remote machines in one TUI client.** Combined agent list, independent reconnects per machine. Also previews **Herdr Cloud** as the next direction. Framed as "why it took longer than expected" — infra piece, not UI piece.

## 2026-08-06 — Joining Y Combinator
Herdr joined YC. **Runtime stays Apache 2.0.** Post explains what the funding is actually for.

## 2026-08-03 — "Ten agents, three clients, 95% less CPU"
Performance writeup. Herdr stopped:
- animating the sidebar unnecessarily
- drawing hidden panes
- repainting unchanged frames during mouse movement

**Busiest sessions gained the most.** Good talking point for anyone worried about running many agents on a laptop.

## 2026-06-10 — "Coding agents are becoming runtimes"
Philosophy post. **Coding-agent CLIs are becoming developer infrastructure.** Project instructions, lifecycle state, hooks, and terminal runtimes need shared contracts. This is the "why Herdr exists" essay — reach for it when someone asks the big-picture question.

## 2026-05-27 — Herdr 0.6.3: session persistence, safer updates, workspace navigation
Shipped new persistence paths for updates, server restarts, and larger sessions.

## 2026-05-27 — "Live updates without killing your terminal processes"
Shipped **live binary handoff** (`herdr update --handoff`): Herdr replaces its own server during an update while keeping pane processes alive. The feature was experimental on homepage copy; the May 2026 post is where it landed.

## Direction summary (as of Oct 2026)
- **Where today:** 0.9.3 stable; local + remote unified in one TUI; 20+ agents detected; Apache 2.0 runtime; growing plugin marketplace.
- **Where next (publicly stated):**
  - **Herdr Cloud** — hosted runtime for "where agents run while you sleep" (homepage section 05 teaser + Sep 2026 post).
  - **More clients on the same runtime** — "TUI · CLI · plain SSH, more coming" per the compare page.
  - **Marketplace** — launching with tagged `herdr-plugin` repos.
- **What stays:** Apache 2.0 runtime. YC + Bessemer backing is explicitly framed around "runtime stays open."

## Nerd lines to deploy
- "Herdr's thesis: coding-agent CLIs are becoming developer infrastructure, and infrastructure needs a runtime."
- "95% less CPU came from not drawing what nobody is looking at — the client is truly thin."
- "Live binary handoff means `herdr update` can swap the server without killing your PTYs. That's the May 2026 shipped feature, not vaporware."
- "They raised $6M from Bessemer in Sept 2026, YC in August. Runtime stays Apache 2.0 — that's in both announcement posts."
