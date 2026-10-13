# Technology teaching pattern library

This reference distills strong explanation patterns already present across `textDump/`.

## 1. Primer pattern

**Best for:** orientation, first contact, broad understanding

**Typical shape:**
- what it is
- key features or concepts
- getting started
- practical examples
- next steps
- resource links

**Observed examples:**
- `03_RESOURCES/AI/OPENCODE/opencode-primer.md`
- `02_AREAS/Workflow_Automation/n8n/n8n_primer.md`
- `01_PROJECTS/MUSIC/strudel/01_strudel_usage_primer.md`

**Strengths:**
- lowers activation energy
- good first teaching pass
- works well for tools and platforms

## 2. Study guide pattern

**Best for:** mastery, repetition, onboarding, high-retention learning

**Typical shape:**
- core concepts
- mechanisms or principles
- structured topic breakdown
- quiz / short-answer checks
- essay or reflection prompts
- glossary

**Observed examples:**
- `03_RESOURCES/AI/OLLAMA/OLLAMA_STUDY_GUIDE_PRIMER.md`
- `01_PROJECTS/BILAN/SALES/ONBOARDING/ES/00_Resumen_Capacitacion/study-guide.md`
- `01_PROJECTS/BILAN/MARKETING/RAG/notebooklm_outputs/*study_guide.md`

**Strengths:**
- helps users retain complex material
- good when understanding must become fluency
- strong for training programs

## 3. Decision guide pattern

**Best for:** selecting the right tool, architecture, or workflow

**Typical shape:**
- decision tree
- comparison matrix
- scenario analysis
- recommendation rules
- ROI or tradeoff framing

**Observed examples:**
- `03_RESOURCES/AI/MCP/mcp-decision-guide.md`
- some git/workflow comparison notes across the repo

**Strengths:**
- reduces ambiguity
- strong when the real task is choosing, not merely understanding

## 4. Workflow guide pattern

**Best for:** step-by-step execution

**Typical shape:**
- prerequisites
- ordered steps
- examples or command snippets
- validation and troubleshooting
- best practices

**Observed examples:**
- `03_RESOURCES/Software_Engineering/git/solo-multi-computer-git-workflow.md`
- cron and automation guides
- setup and implementation guides across `01_PROJECTS/` and `02_AREAS/`

**Strengths:**
- turns knowledge into action
- good for operational tasks

## 5. Gamified interactive app pattern

**Best for:** topics with states, distinctions, nested structures, or process learning by interaction

**Typical shape:**
- mission-based progression
- 3 levels
- action-feedback loop
- side panels showing alternate perspectives
- central mental model canvas
- mastery summary

**Observed example:**
- `00_INBOX/herdr-gamified-webapp-prompt/app/`

**Strengths:**
- excellent for mental models users confuse repeatedly
- useful when interaction teaches relationships better than static text

### 5a. CLI shell simulator variant

**Best for:** command-line tools and syntax where muscle memory matters more than mental-model visualization

**Distinctions from the base gamified app:**
- replaces the central canvas with a **terminal emulator** (prompt, buffer, scrollback)
- user **types real commands** instead of clicking buttons
- **live validation**: green output for valid commands, red for errors
- **autocomplete** (Tab) teaches discoverability
- **vim-style modes** (INSERT/NORMAL) add realism for power-user topics
- **progressive hinting**: `hint` command gives 3 escalating clues (vague → specific → literal answer)
- **"Did you mean?"** suggestions after failures, based on common mistakes for the topic
- **streak counter** for gamification feedback

**When to choose this variant:**
- the real-world skill is typing commands, not clicking a UI
- syntax errors are the primary failure mode (cron, SQL, regex, git)
- users need to practice under "shell-like" constraints

**Observed example:**
- `02_AREAS/Workflow_Automation/unified-workflow/automation/cron_reference/cron-commander/`

**File structure:**
- `index.html` — terminal DOM with prompt, buffer, status line
- `styles.css` — dark terminal theme, color-coded output states
- `app.js` — command parser, hint engine, autocomplete, level state

## 6. Hybrid pattern

**Best for:** topics that need more than one teaching mode

**Examples:**
- primer + decision guide
- workflow guide + study guide
- gamified app + quick reference markdown

**Rule:**
Only use hybrid when the combination clearly improves teaching. Do not combine formats just to be ambitious.

## Selection rubric

Choose based on the user's real need:

- **"What is this and how do I start?"** → Primer
- **"I need to really learn this"** → Study guide
- **"Which one should I use?"** → Decision guide
- **"How do I do this step by step?"** → Workflow guide
- **"I keep confusing these concepts"** → Gamified interactive app
- **"I need to practice typing commands with real feedback"** → CLI shell simulator variant
- **"I need both orientation and execution"** → Hybrid

## Important constraint

Do not force the Herdr app pattern onto every topic.

It is powerful, but only when the subject benefits from interaction and mental-model visualization.
