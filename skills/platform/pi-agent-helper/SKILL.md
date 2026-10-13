---
name: pi-agent-helper
description: Helps with recurring questions about pi, pi-agent, pi-coding-agent, and related customization topics. Use when explaining pi concepts, finding the right docs, comparing skills/extensions/prompt templates/system files, scaffolding pi customizations, or debugging why a pi feature is not loading.
---

# Pi Agent Helper

Use this skill whenever the user references **pi-agent**, **pi**, the **pi coding agent**, or asks about skills, prompt templates, extensions, themes, packages, the SDK, the TUI, providers/models, custom providers, or configuration.

## Clarify the term when needed

`pi-agent` can mean two different things:

1. the terminal harness/package: `@mariozechner/pi-coding-agent`
2. the lower-level package: `@mariozechner/pi-agent`

If the user is asking about the terminal app, docs, commands, sessions, customization, or workflows, assume they mean **`@mariozechner/pi-coding-agent`**.
If they ask about library internals or package APIs, call out the distinction explicitly.

## Primary local documentation roots on this machine

- Main README:
  - `/home/capicuaman/.npm-global/lib/node_modules/@mariozechner/pi-coding-agent/README.md`
- Docs directory:
  - `/home/capicuaman/.npm-global/lib/node_modules/@mariozechner/pi-coding-agent/docs`
- Examples directory:
  - `/home/capicuaman/.npm-global/lib/node_modules/@mariozechner/pi-coding-agent/examples`

## Topic → docs map

- Overview, philosophy, commands, sessions, customization overview:
  - `README.md`
- Skills:
  - `docs/skills.md`
- Prompt templates:
  - `docs/prompt-templates.md`
- Extensions:
  - `docs/extensions.md`
  - `examples/extensions/`
- Themes:
  - `docs/themes.md`
- Keybindings:
  - `docs/keybindings.md`
- SDK / embedding:
  - `docs/sdk.md`
  - `examples/`
- TUI components:
  - `docs/tui.md`
- Providers and auth:
  - `docs/providers.md`
- Custom models/providers:
  - `docs/models.md`
  - `docs/custom-provider.md`
- Packages:
  - `docs/packages.md`
- Sessions / tree / compaction / settings:
  - `docs/session.md`
  - `docs/compaction.md`
  - `docs/settings.md`

## Working method

1. Identify the exact pi topic.
2. Read the relevant installed docs before answering.
3. Follow linked docs/examples if the answer depends on implementation details.
4. Prefer the simplest customization layer that fits:
   - **Prompt template** = reusable phrasing
   - **Skill** = repeatable workflow or knowledge pack
   - **Extension** = new behavior, tools, commands, hooks, or UI
   - **SYSTEM.md / APPEND_SYSTEM.md** = persistent global behavior/instructions
5. When suggesting implementation, show exact target paths.
6. When new skills, prompts, or extensions are created, remind the user to run `/reload` or restart pi if needed.

## Response style

- Be concise but specific.
- Show exact file paths clearly.
- Separate **recommendation**, **why**, and **how to use it**.
- Include invocation examples such as `/skill:name` or `/template-name`.
- Prefer installed docs over memory when answering pi-specific questions.

## Default recommendation heuristics

- If the user says they will ask about pi repeatedly, recommend a **global skill**.
- If the user wants shortcuts for recurring prompts, recommend **prompt templates**.
- If the user wants new commands, tools, UI, guards, or automation, recommend an **extension**.
- If the user wants pi to always behave a certain way across tasks, recommend **SYSTEM.md** or **APPEND_SYSTEM.md**.
