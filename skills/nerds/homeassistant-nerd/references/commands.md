# Home Assistant — Commands Cheatsheet

Grounded on Home Assistant 2026.9.x docs + this user's install profile (**Container flavor on Docker, Synology DS220+**, per `02_AREAS/HOME-LAB/`). Supervised/HAOS commands are marked where they differ.

Ground truth when this file disagrees with reality: `hass --help`, `ha --help` (HAOS/Supervised only), and `docker exec homeassistant hass --help` (Container flavor).

---

## Daily-entry commands

### Validate config before restart (do this every time)
```bash
# Container flavor (this user's box):
docker exec -it homeassistant hass --script check_config -c /config

# HAOS / Supervised:
ha core check
```
**Never restart without this.** A broken `configuration.yaml` on restart gives you no UI to fix it in.

### Restart Home Assistant
```bash
# Container flavor:
docker restart homeassistant

# HAOS / Supervised:
ha core restart
```
Use `ha core reload-core-config` (HAOS/Supervised) for YAML-only changes that don't need a full restart.

### Tail the live log
```bash
# Container flavor:
docker logs -f --tail=200 homeassistant

# HAOS / Supervised:
ha core logs --follow
```
Also available in UI: Settings → System → Logs.

### Reload a specific config domain without restart
In the UI: Developer Tools → YAML → "Reload <automations / scripts / scenes / template entities / …>".
Each has a shell equivalent via the REST API (see below), but the UI button is faster and safer.

---

## REST API — the real ground truth
Base: `http://<host>:8123/api/`. Auth: `Authorization: Bearer <long-lived-access-token>`.

### Health check
```bash
curl -s http://localhost:8123/api/ \
  -H "Authorization: Bearer $HA_TOKEN"
# {"message": "API running."}
```

### Get all states
```bash
curl -s http://localhost:8123/api/states \
  -H "Authorization: Bearer $HA_TOKEN" | jq '.[].entity_id' | head
```

### Call a service (e.g. turn on a light)
```bash
curl -s -X POST http://localhost:8123/api/services/light/turn_on \
  -H "Authorization: Bearer $HA_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"entity_id":"light.living_room"}'
```

### Fire an event
```bash
curl -s -X POST http://localhost:8123/api/events/my_custom_event \
  -H "Authorization: Bearer $HA_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"source":"cli"}'
```

Generate the long-lived token: UI → profile icon (bottom left) → Security → "Create Token".

---

## Config file quick-reference

| File (in `/config`) | Purpose |
|---|---|
| `configuration.yaml` | top-level config, integration includes, HTTP, logger |
| `secrets.yaml` | `!secret foo` references target this file; never commit |
| `automations.yaml` | UI-managed automations (keep hand-edits minimal) |
| `scripts.yaml` | reusable action sequences |
| `scenes.yaml` | saved entity-state snapshots |
| `customize.yaml` | per-entity attribute overrides |
| `ui-lovelace.yaml` | only exists if dashboards are in YAML mode |
| `home-assistant.log` | current log file |
| `home-assistant_v2.db` | recorder (history/statistics) SQLite |

---

## Container-flavor housekeeping (this user's box)

### Inspect the running container
```bash
docker ps --filter name=homeassistant
docker inspect homeassistant --format '{{.Config.Image}} {{.State.Status}}'
```

### Update HA (Container flavor)
```bash
docker pull ghcr.io/home-assistant/home-assistant:stable
docker stop homeassistant && docker rm homeassistant
# re-run with the same compose / run command (keep the /config volume!)
```
**Always** read release notes first: https://www.home-assistant.io/blog/categories/release-notes/

### Backup before any upgrade
```bash
# Container flavor — snapshot the /config volume:
tar czf ~/ha-backup-$(date +%F).tgz /path/to/config
```
HAOS/Supervised: `ha backup new --name "pre-upgrade-$(date +%F)"` — far nicer.

### Sibling-service pattern (MQTT, Frigate, Ollama)
Each is its own container. Share the Docker network, point HA at them by container name:
```yaml
# configuration.yaml snippet
mqtt:
  broker: mosquitto
  port: 1883
```

---

## HACS (community store) ops
```bash
# Install HACS on Container flavor (one-time):
cd /config
wget -O - https://get.hacs.xyz | bash -
docker restart homeassistant
# then: UI → Settings → Integrations → "+ Add" → HACS → follow GitHub device-code flow
```
Updates to HACS integrations happen in UI → HACS → "Updates" tab.

---

## Diagnosis cheatsheet

| Symptom | First check |
|---|---|
| UI won't load after restart | `docker logs homeassistant` for `invalid config` / `Setup failed` |
| Automation didn't fire | Dev Tools → State → confirm trigger entity actually changed; then Logbook |
| Entity shows "unavailable" | Integration-level error → Settings → Devices & Services → integration card |
| Secrets not resolving | `!secret foo` indented wrong, or `secrets.yaml` not in config dir root |
| MQTT device missing | Mosquitto container up? HA MQTT integration reconnected after broker restart? |
| HTTPS reverse proxy loops | `http:` block in config must have `use_x_forwarded_for: true` + `trusted_proxies:` list |

---

## Signature nerd patterns

### Pattern 1 — "Dry-run before mutate"
```bash
docker exec -it homeassistant hass --script check_config -c /config && \
docker restart homeassistant
```
Chain the two with `&&`. If check fails, restart never fires.

### Pattern 2 — "Automation UI → YAML audit"
UI-created automations end up in `automations.yaml` with cryptic IDs. Grep by alias:
```bash
grep -n "alias:" /path/to/config/automations.yaml
```

### Pattern 3 — "Tailscale-only remote access"
Run Tailscale on the Docker **host**, advertise `:8123`, access via `http://<tailscale-name>:8123` from any device. No port-forward, no HA Cloud needed. Documented in `02_AREAS/HOME-LAB/SERVICES/home-assistant-remote-access-prep.md`.

### Pattern 4 — "Local LLM + Assist pipeline"
Ollama container + Open WebUI container + HA Assist with the Ollama conversation agent. Blueprint in `02_AREAS/HOME-LAB/AUTOMATION/HOME_ASSISTANT/ai-integration-blueprint.md`.

---

## Escape hatches
- Config broke, UI gone, no idea what → `docker exec -it homeassistant hass --script check_config -c /config`, read the error, fix the file on the host, restart.
- Need to roll back → stop container, restore `/config` from the backup tar, start container.
- Reset admin password (Container): `docker exec -it homeassistant hass --script auth -c /config reset <username> <newpassword>`.
- Totally stuck → ask upstream community: https://community.home-assistant.io/

## The authority ladder
1. `hass --script check_config` output (reality for *this* config).
2. `02_AREAS/HOME-LAB/` local docs (reality for *this* install).
3. https://www.home-assistant.io/docs/ (upstream canonical).
4. `references/facts.md` snapshot (dated).
5. Training-data guesses — **never**.
