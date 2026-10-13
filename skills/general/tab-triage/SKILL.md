---
name: tab-triage
description: Triage a OneTab URL dump — clean tracking params, classify each link as Keep/Inbox/Discard, route saves to the right PARA location, extract session insights, and update the daily journal. Use when the user pastes OneTab output, says "process my tabs", "triage links", or "what was I looking at".
---

# Tab Triage Skill

Transforms a messy OneTab dump into structured knowledge routed into the right PARA location. Three phases: **Parse → Triage → Store**.

---

## Phase 1 — Parse & Clean

### Step 1: Clean tracking params from URLs
```bash
echo "<paste>" | python3 /home/capicuaman/Documents/textDump/.agents/skills/tab-triage/scripts/clean-urls.py
```
Or save the dump to `/tmp/onetab-raw.txt` first:
```bash
python3 /home/capicuaman/Documents/textDump/.agents/skills/tab-triage/scripts/clean-urls.py /tmp/onetab-raw.txt
```

### Step 2: Classify noise immediately — no analysis needed
Drop these without showing to user:
- Homepage URLs: `youtube.com` (no path), `reddit.com` (no path), `gmail.com`, `amazon.com/404`
- Pure search results without content: Bing/Google search pages
- Dead links: `404`, `Page Not Found`
- Auth session URLs the user can't return to: most `localhost:*` unless they specifically want them

---

## Phase 2 — Triage Table

After cleaning, produce a triage table. Show it to the user and ask for confirmation before writing anything.

### Triage categories

| Signal | Category | PARA destination |
|--------|----------|-----------------|
| `github.com/[AI orgs]`, Gemini sessions, Perplexity AI queries | 🤖 AI / Dev Tools | `03_RESOURCES/AI/` (pick closest subfolder) |
| `github.com/` repos, dev docs, programming languages | 🛠️ Software Engineering | `03_RESOURCES/Software_Engineering/DEV/` |
| `figma.com`, design tools, CSS/UI YouTube | 🎨 Design | `03_RESOURCES/` (create `Design/` if missing) |
| `youtube.com/watch`, tutorials, full walkthroughs | 📺 Learning / Video | `03_RESOURCES/` by topic |
| Health, diet, fitness, supplements | 🏃 Health | `02_AREAS/Personal_Development/` |
| `01_PROJECTS/` adjacent work, active project tooling | 🎯 Active Project | `01_PROJECTS/[project]/resources.md` |
| Payment links, forms, one-time admin | 📋 Admin / Ephemeral | `00_INBOX/` (note + date, review & purge) |
| Own GitHub notes (`Capicuaman/textDump`) | 🔁 Own Notes | Already in repo — just note the visit |
| Family, parenting, education for kids | 👨‍👩‍👧 Personal / Family | `02_AREAS/Personal_Development/` |
| Unclassifiable or unclear | 📥 Inbox | `00_INBOX/` |
| Noise (as above) | 🔴 Discard | — |

### Table format to show user

```
| # | Title | Clean URL | Category | Destination | Action |
|---|-------|-----------|----------|-------------|--------|
| 1 | nexu-io/open-design | github.com/nexu-io/open-design | 🛠️ Dev Tools | 03_RESOURCES/AI/ | Keep |
| 2 | PachaMama — Figma | figma.com/design/... | 🎨 Design | 01_PROJECTS/? | Keep |
| 3 | Gmail | gmail.com | 🔴 Noise | — | Discard |
```

Tell the user: "Say OK to confirm, or override any row (e.g. 'move 4 to Projects', 'discard 7')."

---

## Phase 3 — Session Insights

Before writing, synthesize what the tabs reveal. Look for patterns:
- Clusters of related topics → infer what the person was working on
- Connections to today's goals (check `05_JOURNAL/daily-YYYY-MM-DD.md`)
- New tools / repos worth flagging
- Anything that contradicts or enriches their current projects

Write a 3-5 sentence **Session Insight** paragraph. This is the highest-value output — more useful than any individual link.

---

## Phase 4 — Store

### 4a. Write curated onetab file

File: `03_RESOURCES/Knowledge_Management/onetab/YYYY-MM-DD.md`

Format:
```markdown
# Tab Triage — YYYY-MM-DD

## 💡 Session Insights
[3-5 sentence synthesis of what these tabs reveal]

## 🟢 Saved

### 🤖 AI / Dev Tools
- [Title](url) — one-line note on why it's interesting

### 🎨 Design
...

### 📚 Learning
...

### 🏃 Health / Personal
...

### 📋 Admin (review & purge by [date+7days])
- [Title](url) — context note

## 📥 Inbox (needs decision)
- [Title](url) — what's unclear about it

## 🔴 Discarded
Dropped N noise tabs (Gmail, YouTube home, Amazon 404, etc.)
```

### 4b. Update today's journal

Append to `05_JOURNAL/daily-YYYY-MM-DD.md`:
- Add a `[IRL] Tab triage: N links processed` line to the correct time-block in Daily Log
- Fill or append to `🔗 Related Notes` with wiki-links to PARA files that were touched
- Add key insights to `💡 Insights & Learnings` if they're genuinely insightful

### 4c. Route individual saves (optional, confirm with user)

For high-signal links the user wants to deeply integrate, offer to:
- Add to an existing resource file in the right PARA folder
- Create a new resource note if the topic has no home yet
- Add to a project's resource list if it's project-specific

Use the `edit` tool with targeted appends. Never overwrite existing files.

---

## PARA Quick Reference

```
textDump/
├── 00_INBOX/              ← Unprocessed, ephemeral, unclear
├── 01_PROJECTS/           ← Active projects (bilan, herdr, etc.)
├── 02_AREAS/
│   ├── HOME-LAB/          ← Infrastructure, networking
│   └── Personal_Development/  ← Health, books, philosophy, family
├── 03_RESOURCES/
│   ├── AI/                ← AI tools (CLAUDE, GEMINI, pi, herdr, etc.)
│   │   ├── CLAUDE/
│   │   ├── GEMINI/
│   │   ├── pi/
│   │   └── herdr/
│   ├── Software_Engineering/
│   │   └── DEV/           ← Dev tools, repos, languages
│   ├── Knowledge_Management/
│   │   └── onetab/        ← ← ← Curated tab dumps go here
│   └── Misc/YouTube/      ← Video resources
└── 05_JOURNAL/            ← Daily notes (never store links here directly)
```

---

## Handling Gemini / AI Chat Sessions

Gemini sessions (`gemini.google.com/app/[id]`) are often not revisitable without auth. Instead of saving the URL:
1. Ask user: "The Gemini session on [topic] — do you want to save a summary of what you were exploring?"
2. If yes: write a short note to the appropriate `03_RESOURCES/` file instead of the URL
3. Same for Perplexity searches, Claude sessions, etc.

---

## Script Path Reference

| Script | Path |
|--------|------|
| URL cleaner | `/home/capicuaman/Documents/textDump/.agents/skills/tab-triage/scripts/clean-urls.py` |
| Onetab output dir | `/home/capicuaman/Documents/textDump/03_RESOURCES/Knowledge_Management/onetab/` |
| Today's journal | `/home/capicuaman/Documents/textDump/05_JOURNAL/daily-$(date +%Y-%m-%d).md` |
