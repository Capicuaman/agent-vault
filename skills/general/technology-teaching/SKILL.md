---
name: technology-teaching
description: Read technology files across the `textDump/` repo, extract the strongest explanation strategies and information patterns, then create the best teaching artifact for the target topic. Use when the user wants to understand a technology, compare tools, learn a workflow, turn docs into a study system, or build an educational webpage/app. Can choose among primers, study guides, decision guides, workflow guides, gamified static web apps, or hybrids.
---

# Technology Teaching

Use this skill to teach **any technology or workflow** in this repo, not just pi.

Your job is not to force one format. Your job is to:

1. read the best available source material in `textDump/`
2. identify the strongest explanation patterns already present in the repo
3. choose the teaching format that best fits the topic
4. produce a clear teaching artifact

## Scope and intent

This skill is repo-wide and should be usable anywhere in `textDump/`.

Use it for topics like:
- AI tools
- developer tools
- workflow systems
- automation platforms
- infrastructure topics
- creative coding tools
- internal project processes
- any technical concept with multiple relevant notes in the repo

## Required discovery workflow

Before writing, do all of the following:

### 1. Discover relevant files

Use `bash` with `find` and `rg` to locate topic-relevant files across the repo.

Look especially in:
- `03_RESOURCES/`
- `02_AREAS/`
- `01_PROJECTS/`
- `00_INBOX/`

Prefer files such as:
- `*primer*.md`
- `*guide*.md`
- `*study*.md`
- `*workflow*.md`
- `README.md`
- existing educational apps or static teaching UIs

Do not rely on one file if several relevant files exist.

### 2. Read a representative set

Read multiple high-signal files, not just the first match.

Aim to capture different teaching modes when available:
- foundational overview
- practical quickstart
- decision logic
- workflow steps
- quiz / reinforcement
- interactive / visual teaching

### 3. Extract the best explanation patterns

Use `references/pattern-library.md` to identify which teaching strategies fit the topic best.

You must explicitly decide which pattern or combination is best, based on the material.

## Pattern selection rule

Do **not** default to a webpage.

Choose the format that best teaches the topic:

- **Primer**: for broad orientation and first understanding
- **Study guide**: for mastery, retention, review, quiz, glossary
- **Decision guide**: when the main problem is choosing between tools or approaches
- **Workflow guide**: when the user needs a sequence of actions
- **Gamified web app**: when the topic has important distinctions, states, nested mental models, or benefits from learn-by-doing interaction
- **Hybrid**: when combining two patterns clearly improves comprehension

Always justify the choice briefly before building.

## If you choose a gamified web app

Read:
1. `00_INBOX/herdr-gamified-webapp-prompt/app/index.html`
2. `00_INBOX/herdr-gamified-webapp-prompt/app/styles.css`
3. `00_INBOX/herdr-gamified-webapp-prompt/app/app.js`
4. `references/herdr-pattern.md`

Then create a static app with exactly:
- `index.html`
- `styles.css`
- `app.js`

No framework, no bundler, no build step.

Preserve the underlying teaching process, not the labels:
- mission-based progression
- 3 levels
- framing cards
- left sidebar with meaningful alternate view(s)
- central canvas with the topic's real mental model
- right learning rail with tasks, actions, and explanation
- keyboard help
- mastery summary

Only choose this when interaction genuinely improves understanding.

## If you choose a markdown teaching document

Use the clearest structure for the pattern selected.

Examples:
- primer: what it is, core concepts, getting started, examples, next steps
- study guide: concepts, mechanisms, quiz, prompts, glossary
- decision guide: decision tree, matrix, scenarios, recommendations
- workflow guide: prerequisites, ordered steps, failure modes, verification

In Markdown outputs inside this repo:
- use ATX headers
- use practical examples
- add `[[wiki-links]]` when helpful
- preserve the tone/style of the surrounding directory

## Teaching quality rules

- plain language first, jargon second
- explain why distinctions matter
- prefer mental models over definition dumps
- separate overview from action steps
- include examples when they reduce ambiguity
- if several source files disagree, say so and choose the most credible/current one
- do not make the artifact more complex than the subject requires

## Review checklist

Before finishing, check:
- Did I read multiple relevant source files?
- Did I choose the best teaching pattern instead of forcing a favorite format?
- Is the output faithful to the repo's strongest existing explanation styles?
- Does it help the user understand, decide, or act?
- If a web app was chosen, does interaction truly teach something better than static text would?

## Optional validation

If you generate JavaScript for a static app, validate with:

```bash
node --check app.js
```

If you generate a multi-file teaching artifact, list the created files clearly in the final response.
