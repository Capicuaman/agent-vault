# Herdr interactive teaching pattern

Use this only when a topic genuinely benefits from a gamified static web app.

Distilled from `00_INBOX/herdr-gamified-webapp-prompt/app/`.

## Structural pattern

- single-page static app
- `index.html` wires the shell and semantic regions
- `styles.css` defines a dark dashboard with OKLCH color tokens
- `app.js` holds all teaching state and rendering

## Teaching pattern

- 3 levels
- each level has:
  - title
  - mission
  - summary
  - concepts
  - tasks
  - actions
- actions mutate a single in-memory world state
- progress is shown globally
- the user learns by triggering meaningful state changes

## UI pattern

- top status bar
- 3 framing cards
- left sidebar with 2 conceptual panels
- center canvas showing the mental model
- right rail with mission brief and explanation
- keyboard help dialog
- restart flow
- mastery summary

## Good fit signals

Use this pattern when the topic has:
- nested structure
- role or state changes
- commonly confused distinctions
- a process that becomes clearer through staged interaction

## Bad fit signals

Do not use this pattern when the topic is mostly:
- a simple reference
- a narrow checklist
- a straightforward setup guide
- a comparison that works better as a matrix or decision tree

## What should change for each new topic

- labels
- level content
- sidebar semantics
- canvas model
- mastery summary

## What should stay recognizable

- mission-based onboarding
- pacing
- action-feedback loop
- self-contained static implementation

## CLI shell simulator variant

When the topic is a command-line tool (cron, git, SQL), replace the dashboard canvas with a terminal emulator. See `pattern-library.md` §5a for the full variant specification and `cron-commander/` for the working example.
