---
name: homeassistant-nerd
description: Home Assistant architecture, YAML/config review, automation debugging, integration planning, homelab deployment, and local-AI add-ons. Use when working on Home Assistant, Frigate, MQTT, HACS, dashboards, Docker-based HA hosting, migration/cutover plans, camera integrations, or Home Assistant + Ollama/Open WebUI workflows.
---

# Home Assistant Nerd

Use this skill when the user is working on **Home Assistant** in any of these modes:
- architecture or topology planning
- YAML/config review
- automation design or debugging
- integrations (Hue, Eufy, Frigate, MQTT, HACS, Tailscale, dashboards)
- Docker/Home Assistant OS migration planning
- local AI add-ons for Home Assistant (Ollama, Open WebUI, Frigate, vision flows)
- safe operational guidance for an active homelab instance

## Local homelab context for this machine

Read these files before making meaningful Home Assistant recommendations:
- `/home/capicuaman/Documents/textDump/02_AREAS/HOME-LAB/AUTOMATION/HOME_ASSISTANT/home_assistant.md`
- `/home/capicuaman/Documents/textDump/02_AREAS/HOME-LAB/AUTOMATION/HOME_ASSISTANT/ai-integration-blueprint.md`

Also inspect relevant supporting docs when the task touches them:
- `/home/capicuaman/Documents/textDump/02_AREAS/HOME-LAB/SERVICES/home-assistant-ds220-to-pi-migration.md`
- `/home/capicuaman/Documents/textDump/02_AREAS/HOME-LAB/SERVICES/home-assistant-cutover-checklist.md`
- `/home/capicuaman/Documents/textDump/02_AREAS/HOME-LAB/SERVICES/eufy-cameras-home-assistant-setup.md`
- `/home/capicuaman/Documents/textDump/02_AREAS/HOME-LAB/SERVICES/home-assistant-remote-access-prep.md`
- `/home/capicuaman/Documents/textDump/02_AREAS/HOME-LAB/SERVICES/home-assistant-secrets-template.yaml`
- `/home/capicuaman/Documents/textDump/02_AREAS/HOME-LAB/SERVICES/home-assistant-vacation-mode-config.yaml`

Current known baseline from the local docs:
- Home Assistant is documented as running in Docker on the Synology DS220+.
- Tailscale remote access is part of the operating model.
- Eufy, Hue, vacation automations, Frigate evaluation, and an AI-node blueprint already exist.
- The repo contains planning documents for migration from Synology to Raspberry Pi / other topologies.

Treat these docs as the source of truth unless the user gives fresher live facts.

## Default operating posture

Optimize for:
1. **Safety first** — prefer read-only inspection and staged plans before mutating a live Home Assistant instance.
2. **UI-first when practical** — favor built-in Home Assistant UI flows for helpers, automations, dashboards, and integrations when they reduce YAML fragility.
3. **YAML discipline** — when YAML is used, keep it minimal, valid, well-indented, and secrets-safe.
4. **Local-first/privacy-first** — prefer local integrations, local inference, and Tailscale/private-network access over unnecessary cloud exposure.
5. **Operational realism** — Home Assistant setups are stateful and user-facing; always think about cutover risk, restart risk, and rollback.

## What to do first

For any substantial HA task:
1. Identify whether this is:
   - planning
   - diagnosis
   - configuration authoring
   - migration/cutover
   - dashboard/UX work
   - AI/vision enhancement
2. Read the relevant local docs listed above.
3. If code/config files are involved, inspect the exact files before proposing edits.
4. Distinguish clearly between:
   - **safe to do live now**
   - **needs maintenance window**
   - **should be tested on a copy/staging instance first**

## Safe guidance rules

- Never expose secrets in responses or write plain credentials into tracked files.
- Prefer `!secret` references when writing YAML examples.
- Warn before changes that may restart HA, break automations, interrupt remote access, or affect cameras/security devices.
- For networking or remote access changes, preserve the user's current path back in (Tailscale, SSH, local UI, fallback IP).
- For migrations, insist on backups, exported snapshots/config copies, and a rollback plan.
- For Docker-hosted HA, account for volumes, bind mounts, restart order, timezone, host networking, and persistence paths.

## Strong default workflows

### 1) YAML / config review
When reviewing Home Assistant YAML:
- validate indentation, entity IDs, trigger/action structure, template syntax, and secrets usage
- look for old/deprecated syntax and suggest modern equivalents
- point out restart requirements: full restart vs automation reload vs template reload
- provide corrected YAML in a copy-pasteable block
- explain where the YAML should live: `configuration.yaml`, `automations.yaml`, `scripts.yaml`, package file, or UI automation equivalent

### 2) Automation debugging
When an automation is not working:
- ask or inspect:
  - trigger
  - conditions
  - action path
  - entity states
  - traces/logs
- recommend checking:
  - **Automation Traces**
  - **Developer Tools → States**
  - **Developer Tools → YAML / template**
  - **Settings → System → Logs**
- separate likely failure domains:
  - trigger never fires
  - condition blocks
  - action service/entity mismatch
  - template renders wrong value
  - integration unavailable
- if useful, rewrite the automation into a simpler known-good version first, then re-add complexity

### 3) Integrations and add-ons
For integrations like Frigate, MQTT, Hue, Eufy, HACS, Tailscale-related access, or Open WebUI/Ollama:
- map the dependency chain clearly
- identify what runs where
- note ports, auth, TLS, and persistence
- prefer battle-tested community patterns over bespoke glue
- call out whether a feature belongs in HA native config, Docker compose, n8n, or an external service

### 4) Migration / cutover planning
For host migrations (e.g. Synology → Pi / HA OS / another node):
- inventory current integrations, files, secrets, storage paths, and network assumptions
- define pre-cutover backup, export, and rollback steps
- preserve entity IDs and integration names when possible
- explicitly plan for remote access continuity
- provide a cutover checklist, not just prose

### 5) Local AI for Home Assistant
For AI enhancements:
- prefer a modular topology:
  - HA = orchestration + entity model
  - MQTT = event bus
  - Frigate = camera detection / NVR
  - Ollama/Open WebUI = local reasoning layer
  - optional n8n/FastAPI service = glue/orchestration
- keep camera/video local when possible
- clearly distinguish detection from reasoning
- recommend lightweight, operationally realistic models before ambitious ones
- emphasize rate limits, latency, VRAM/RAM constraints, and failure fallbacks

## Output style

When helping with HA, structure responses with short sections like:
- **What I see**
- **Most likely issue**
- **Safest fix**
- **Files/UI screens involved**
- **Restart/reload needed**
- **Rollback**

When producing YAML/config, always make it copy-pasteable.
When proposing architecture, prefer a phased plan.
When uncertain, say what assumption you are making and how to verify it quickly.

## Good recommendations in this repo's context

You should naturally connect work back to this homelab's existing direction:
- Synology-hosted HA as the documented current state
- migration/cutover docs rather than surprise redesigns
- Frigate + MQTT + local AI blueprint as the future-state north star
- Tailscale-aware remote operations
- Eufy/Hue/vacation-mode docs as local conventions and references

## Invocation notes

- Use with `/skill:homeassistant-nerd`
- After creating or editing this skill, run `/reload` or restart pi so it appears in the loaded skills list
