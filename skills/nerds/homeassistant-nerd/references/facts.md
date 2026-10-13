# Home Assistant — Facts Snapshot

**Snapshot date:** 2026-10-07
**Source URL:** https://www.home-assistant.io/
**Captured snapshot:** `~/Documents/textDump/01_PROJECTS/BILAN/raw/www_home-assistant_io.md` (captured via `graphify_add`)
**Local operating docs:** `~/Documents/textDump/02_AREAS/HOME-LAB/AUTOMATION/HOME_ASSISTANT/` and `~/Documents/textDump/02_AREAS/HOME-LAB/SERVICES/`

Treat as snapshot. For "latest" questions, refresh via `graphify_add https://www.home-assistant.io/` first.

---

## Identity
- **Name:** Home Assistant.
- **Tagline:** *"Awaken your home — open source home automation that puts local control and privacy first."*
- **Latest release at snapshot:** 2026.9.4 ("There's room on this bus", Sep 2, 2026). Also 2026.8 "Approachable by design" (Aug 5, 2026).
- **License:** Apache 2.0 (core). Open source.
- **Steward:** **Open Home Foundation** — non-profit, cannot be sold or acquired.
- **Commercial partners funding the foundation:** Nabu Casa (makes Home Assistant Cloud + official hardware), Apollo Automation.
- **Integrations:** 1,500+ at snapshot date.
- **Install base claim:** "Over 2.7 million households."

## Core architecture / mental model
Home Assistant is a Python application that runs as a **central event hub**: integrations connect to devices/services locally, surface *entities* (lights, sensors, media players…), and the automation engine fires on *triggers*, filters via *conditions*, and executes *actions* that call `service.call` on those entities. Dashboards (**Lovelace**) are a visualization layer over the same entity state. **Local-first** is the architectural commitment: cloud fallback only when a device/service forces it.

## Install flavors (what the user has to know first)
| Flavor | What it is | Updates / Add-ons |
|---|---|---|
| **Home Assistant OS** (HAOS) | Full OS image for a Pi / NUC / VM / Green | Full add-on store (via Supervisor), full `ha` CLI |
| **Home Assistant Supervised** | Debian + Supervisor | Full add-on store + `ha` CLI (fragile, discouraged for new installs) |
| **Home Assistant Container** | Docker container only | **No add-on store, no `ha` CLI** — manage sidecar services yourself |
| **Home Assistant Core** | Raw Python venv | No add-ons, no Supervisor, dev-focused |

**This user's install (per `02_AREAS/HOME-LAB/`):** Container flavor, Docker on Synology DS220+. Migration to Raspberry Pi is in planning docs. **This matters:** no `ha` CLI, no Supervisor add-ons — Frigate/MQTT/etc. run as sibling Docker services.

## Key facts table
| Thing | Value |
|---|---|
| Default HTTP port | 8123 |
| Default config dir (HAOS/Supervised) | `/config` |
| Default config dir (Container) | mounted volume → `/config` inside container |
| Default DB | SQLite at `home-assistant_v2.db` in config dir (recorder) |
| Main config file | `configuration.yaml` |
| Secrets file | `secrets.yaml` (never commit) |
| Automations UI → YAML | `automations.yaml` |
| Scripts | `scripts.yaml` |
| Scenes | `scenes.yaml` |
| Lovelace storage mode | UI-driven by default; YAML mode is opt-in |
| REST API base | `http://<host>:8123/api/` (Bearer token) |
| WebSocket API | `ws://<host>:8123/api/websocket` |
| Supervisor API (HAOS/Supervised only) | `http://supervisor/` from inside add-ons |

## Companion ecosystem (first-party)
- **Mobile apps:** iOS, Android, Wear OS, Apple Watch. Send location for presence detection; receive push notifications.
- **Home Assistant Cast:** turn any Chromecast into a dashboard display.
- **ESPHome:** sibling project for custom firmware on ESP32/ESP8266 devices. Starter Kit shipping at snapshot date.
- **Assist:** on-device voice assistant with wake-word support, LLM-pluggable.
- **Home Assistant Hardware:** Green (hub), Connect ZBT-2 (Zigbee/Thread), Connect ZWA-2 (Z-Wave), Voice Preview Edition.
- **Home Assistant Cloud (Nabu Casa):** paid remote-access + Alexa/Google voice bridge. Local-first does **not** require it.

## Common integration categories (SKILL.md relevant)
- **Hue** — direct bridge integration, local.
- **Eufy** — community integration; cloud-dependent for most models.
- **Frigate** — NVR with person/object detection; MQTT-connected; runs as a separate container.
- **MQTT** — needs an external broker (Mosquitto typically); backbone for Frigate, ESPHome, Zigbee2MQTT.
- **HACS (Home Assistant Community Store)** — third-party integration + dashboard-card installer; **not** in Container flavor's add-on list — install manually.
- **Tailscale** — HACS integration available; or run Tailscale on the host for private remote access without exposing 8123.

## Local-AI pattern on this box (from `ai-integration-blueprint.md`)
Pattern already planned: Home Assistant → **Assist** → local LLM via **Ollama** / **Open WebUI**, with **Frigate** feeding vision events into automations. Treat the blueprint doc as the source of truth for the current state.

## Known failure modes HA ops people repeat
- Editing `configuration.yaml` and restarting without `ha core check` (or `hass --script check_config`) first → broken startup, no UI.
- Storing secrets inline instead of in `secrets.yaml` → leak on screenshot/paste.
- Mixing Lovelace UI mode and YAML mode in the same dashboard → UI edits silently stop persisting.
- Running Container flavor and assuming the add-on store exists.
- Expecting `ha` CLI on Container flavor (it only ships with HAOS/Supervised).
- Upgrading HA across a breaking release without reading the release notes → integrations silently fail at startup.

## Snapshot discipline
- `facts.md` is dated at the top. Refresh via `graphify_add https://www.home-assistant.io/` whenever asked about "latest" or version-specific behavior.
- Local `02_AREAS/HOME-LAB/AUTOMATION/HOME_ASSISTANT/*.md` is ground truth for *this user's* install. If it disagrees with upstream docs, the local doc wins for this user's box.
- Breaking-change release notes live at `https://www.home-assistant.io/blog/categories/release-notes/`. Refresh before any major-version upgrade.
