---
description: Flip operating context — I AM physically at this machine for this session
---
For this session, override the Operating Context default in AGENTS.md.

I am physically sitting at this machine right now, not SSH'd in. That means:
- The local DISPLAY / WAYLAND_DISPLAY is mine — opening files in the browser, launching GUI apps, drag-and-drop, and any X11/Wayland action works and I will see it.
- Any `xdg-open` call will land in front of me.
- No need to route artifacts to `localhost:port` + Tailscale or emit "view this on your local machine" workarounds.

Verify once if useful:
```sh
echo "SSH_CONNECTION=$SSH_CONNECTION"   # should be empty if I'm correct
echo "DISPLAY=$DISPLAY"                 # should be populated
```

Proceed with local-first assumptions until I say otherwise, I close this session, or `$SSH_CONNECTION` becomes populated.
