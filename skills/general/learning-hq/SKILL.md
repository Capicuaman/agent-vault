---
name: learning-hq
description: Scan the textDump repo for all learning materials and maintain the central Learning HQ HTML dashboard. Use when the user asks to scan learning materials, update the learning menu, check learning progress, regenerate the HTML index, or says "learning HQ". Also use when new study guides, primers, or learning paths are added to the repo and the menu needs updating.
---

# Learning HQ Skill

Manages the central gamified learning dashboard for the textDump PARA garden.

## Files Owned by This Skill

| File | Purpose |
|---|---|
| `03_RESOURCES/Learning/gamification-menu/index.html` | Main HTML dashboard — the gamified menu |
| `03_RESOURCES/Learning/gamification-menu/README.md` | How to serve it locally |
| `03_RESOURCES/Learning/_MOC_Learning.md` | Markdown index / MOC |
| `03_RESOURCES/Learning/bilan-design-progress.md` | Active progress tracker |
| `03_RESOURCES/Learning/bilan-design-learning-path.md` | Active 30-day path |
| `03_RESOURCES/Learning/ai-design-apps.md` | Tool reference |

## Trigger Phrases

- "scan learning materials"
- "update the learning menu"
- "regenerate learning HQ"
- "check my learning progress"
- "check my bilan learning progress"
- "learning HQ"
- Any time a new study guide / primer / learning path is added to the repo

---

## Protocol: Scan & Update

When triggered, follow this sequence:

### Step 1 — Scan for Learning Materials

Search these locations for any `.md` file that qualifies as a learning resource:

```bash
# Study guides, primers, quizzes, learning paths
find /home/capicuaman/Documents/textDump -name "*.md" \
  | xargs grep -l -i "study\|learn\|guide\|primer\|course\|tutorial\|path\|quiz\|onboarding" 2>/dev/null \
  | grep -v node_modules | grep -v ".git" | sort

# HTML apps and gamified projects
find /home/capicuaman/Documents/textDump -name "index.html" \
  | grep -v node_modules | grep -v ".git"
```

### Step 2 — Read the Progress File

Always read the current progress before updating:
```
03_RESOURCES/Learning/bilan-design-progress.md
```

Extract:
- `Current day` → update the progress bar % in the HTML (`day / 30 * 100`)
- `Resume at` → update the hero strip subtitle
- Last completed task → update badge labels

### Step 3 — Categorize New Materials

Map each new file to a section:

| File pattern / location | Section |
|---|---|
| `03_RESOURCES/Learning/` | Design Learning |
| `03_RESOURCES/AI/` | AI Tools & Agents |
| `03_RESOURCES/promptEngineering/` | Prompt Engineering |
| `01_PROJECTS/BILAN/SALES/ONBOARDING/` | bilan Product Knowledge |
| `01_PROJECTS/BILAN/MARKETING/RAG/` | bilan Product Knowledge |
| `03_RESOURCES/Software_Engineering/` | Software Engineering |
| `03_RESOURCES/Terminal_And_Shell/` | Terminal & Shell |
| `*gamif*` or `*quest*` or `*game*` or `index.html` | Gamified Projects |

### Step 4 — Generate a New Card

For each new resource, add a card block to the appropriate section in `index.html`:

```html
<a class="card" href="[RELATIVE_PATH_FROM_gamification-menu/]"
   style="--accent:[ACCENT_COLOR]; --accent-glow:[ACCENT_COLOR]22;">
  <span class="card-icon">[EMOJI]</span>
  <div class="card-tag">[TAG]</div>
  <div class="card-title">[TITLE]</div>
  <div class="card-desc">[1-2 sentence description of what it teaches]</div>
  <div class="card-footer">
    <span class="card-path">[SHORT_PATH]</span>
    <span class="card-arrow">→</span>
  </div>
</a>
```

### Step 5 — Update Progress Bar

Find this line in `index.html` and update the percentage:
```html
<div class="progress-bar-fill" style="width: X%"></div>
```

Formula: `(current_day / 30) * 100` → rounded to 1 decimal.

Also update:
- The `day-count` div (large number)
- The `progress-strip` subtitle text
- The badge labels on the featured card

### Step 6 — Update the MOC

Add any new file to `_MOC_Learning.md` under its section.

---

## Accent Colors by Section

| Section | Color |
|---|---|
| Design Learning | `#0066CC` (bilan Blue) |
| AI Tools | `#0891B2` (teal) |
| Prompt Engineering | `#F5A623` (gold) |
| bilan Product Knowledge | `#00AA44` (green) |
| Software Engineering | `#CC0000` (red) |
| Terminal & Shell | `#6B7280` (gray) |
| Gamified Projects | `#F5A623` (gold) |

---

## How to Serve the Dashboard

```bash
cd /home/capicuaman/Documents/textDump/03_RESOURCES/Learning/gamification-menu
python3 -m http.server 8790
# → open http://localhost:8790
```

---

## Progress Tracker Protocol

When the user says "Day N done" or "I finished Day N":

1. Read `bilan-design-progress.md`
2. Mark Day N as ✅ in the Completed table with any notes the user provided
3. Move the `Resume at` line to Day N+1
4. Update `Current day` to N+1
5. Add a dated entry to the Daily Log section
6. Update the HTML progress bar: `(N / 30) * 100`%
7. Update the `day-count` in the hero strip

## Check Progress Protocol

When the user says "check my bilan learning progress" or "where am I in the path":

1. Read `bilan-design-progress.md`
2. Report: current day, last completed task, what's next
3. Offer to brief them on the next day's tasks
4. Do NOT rebuild the full HTML unless asked

---

## Related Skills

- `bilan-base` — brand colors, fonts, personas (load for bilan-specific card content)
- `technology-teaching` — for generating new study guides to add to the menu
- `graphify` — for building knowledge graphs from the learning corpus

---

*Tags: #skill #learning #gamification #dashboard #progress*
