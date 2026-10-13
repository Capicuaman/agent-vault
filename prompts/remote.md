---
description: Reaffirm I am SSH'd in — treat remote-first (this is the default; use when context seems confused)
---
Reaffirm the default Operating Context from AGENTS.md.

I am SSH'd into this machine from another one, via Tailscale. The local DISPLAY on this box is NOT mine — anything you launch on it (browser, GUI app, `xdg-open`) will not reach me.

Route artifacts I can actually see:
- Terminal output (I'm looking at pi over SSH right now)
- File paths I can read via my local editor over SSH mount / VS Code Remote
- HTML files served on a `localhost:<port>` that I can reach via Tailscale on this box's hostname
- Markdown files committed to the repo so I can read them from either side

Verify:
```sh
echo "SSH_CONNECTION=$SSH_CONNECTION"   # should be populated (expected)
echo "DISPLAY=$DISPLAY"                 # should be empty on SSH pts
```
