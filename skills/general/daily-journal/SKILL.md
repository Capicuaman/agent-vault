---
name: daily-journal
description: Interactive daily journaling for the 05_JOURNAL folder. Use when the user wants to journal, brain-dump, capture IRL events, do a check-in, reflect on the day, or manage the automated journal agent (enable/disable cron). Fills the human sections of daily-YYYY-MM-DD.md that the automation can't touch.
---

# Daily Journal Skill

This skill manages the **two-layer journaling system** in `05_JOURNAL/`:

| Layer | Tool | What it captures |
|-------|------|-----------------|
| **Automated** | `journal_agent.py` (cron) | Git commits, task-log, work metrics |
| **Human** | This skill (interactive) | IRL events, mood, goals, insights, reflection, gratitude |

The human layer fills the sections the bot can't — real life, feelings, thoughts. Never touch the auto sections (Daily Log, Work Snapshot, Daily Synthesis, Metrics).

---

## 1. Managing the Automated Agent (Enable / Disable)

Before any session, check if the user wants to enable or disable the cron agent.

### Check current status
```bash
crontab -l 2>/dev/null | grep -q journal_agent && echo "ENABLED" || echo "DISABLED"
```

### Enable the cron agent
```bash
/home/capicuaman/Documents/textDump/.agents/skills/daily-journal/scripts/enable-cron.sh
```

### Disable the cron agent
```bash
/home/capicuaman/Documents/textDump/.agents/skills/daily-journal/scripts/disable-cron.sh
```

### Run agent manually (one-shot, no cron needed)
```bash
/usr/bin/python3 /home/capicuaman/Documents/textDump/03_RESOURCES/Workflow_Automation/journal_automation/journal_agent.py --force --live
```

**When the user asks about the agent:** always show current status first, then offer enable/disable.

---

## 2. Session Startup — Always Do This First

```bash
# 1. Get today's date
date +%Y-%m-%d

# 2. Check if today's journal exists and show its current state
cat /home/capicuaman/Documents/textDump/05_JOURNAL/daily-$(date +%Y-%m-%d).md 2>/dev/null || echo "NO JOURNAL YET — run agent first"
```

If no file exists, run the agent to create the scaffold before journaling.

Then **scan the file** and identify:
- Which manual sections are still `{{PLACEHOLDER}}` or `_____` → need filling
- Which sections have real content → preserve exactly as-is
- The auto-generated sections (Daily Log, Work Snapshot, Daily Synthesis, Metrics) → **never edit these**

---

## 3. Session Modes

Detect intent from what the user says and pick the right mode:

### Mode A — Full Check-In (morning or midday)
*Triggered by: "journal", "check-in", "start my day", "morning"*

Ask these in order, one at a time (don't dump all at once):
1. **Mood & Energy** → "How are you feeling right now? Energy level 1-10?"
2. **Today's Goals** → "What are the 2-3 most important things you want to do today?"
3. **Personal Development** → "Anything for yourself today — learning, health, habit?"
4. **Weather / Context** → "What's the vibe outside / where are you working from?"

Then write everything into the file.

### Mode B — Brain Dump (freeform IRL capture)
*Triggered by: "brain dump", "let me tell you about", "something happened", "capture this", "I want to write"*

Let the user talk freely. Don't interrupt. When they're done:
1. Extract **events/facts** → Daily Log (morning/afternoon/evening slot)
2. Extract **feelings/energy** → Mood field
3. Extract **insights/learnings** → Insights & Learnings section
4. Extract **wins** → What Went Well
5. Extract **struggles** → Challenges Faced
6. Extract **gratitude items** → Gratitude section
7. Identify any **wiki-links** to PARA notes → Related Notes section

Ask the user to confirm the extraction before writing.

### Mode C — End-of-Day Reflection
*Triggered by: "reflect", "end of day", "wrap up", "evening", "how'd today go"*

Ask these, one at a time:
1. "What actually got done today?" (if Work Snapshot is empty)
2. "What went well?"
3. "What was hard or frustrating?"
4. "What's one thing you learned or noticed today?"
5. "What are you grateful for?" (aim for 3 specific things)
6. "What's the first thing on tomorrow's list?"

Then write all of it into the file.

### Mode F — OneTab / Link Dump
*Triggered by: pasted URLs, "process my tabs", "what was I looking at"*

Hand off to the `tab-triage` skill — it handles the full pipeline:
```
/skill:tab-triage
```
The tab-triage skill will clean URLs, triage, generate insights, write to `onetab/YYYY-MM-DD.md`, and update today's journal automatically.

---

### Mode D — Quick Log Entry
*Triggered by: "log this", "add to journal", "note this", "quick entry"*

User gives a short note. Slot it into the right time block (Morning/Afternoon/Evening) of the Daily Log based on current time, prefixed with `[IRL]` to distinguish from git commits.

### Mode E — IRL Event Capture
*Triggered by: "I had a meeting", "I talked to", "something cool happened", "I went to"*

Capture the event with:
- Who was involved
- What happened
- What you took away from it
- Any follow-up action → add to tomorrow's preview

---

## 4. Writing Rules

### Manual sections you OWN (safe to edit)
- `📅 Date & Context` → Weather, Mood
- `🎯 Today's Goals` → Primary Focus, Secondary Tasks, Personal Development
- `💡 Insights & Learnings`
- `🤔 Reflection` → What Went Well, Challenges Faced, Lessons Learned, Gratitude
- `📋 Tomorrow's Preview`
- `🔗 Related Notes`
- Daily Log entries prefixed with `[IRL]` (append, never remove existing lines)

### Auto sections — HANDS OFF
- `📝 Daily Log` → git commit lines (only append `[IRL]` entries, never delete)
- `Work Snapshot` → task-log data
- `Daily Synthesis` → auto-generated outcomes
- `📊 Metrics & Tracking` → script-calculated
- `Tags` footer → auto-generated
- `<!-- Last auto-update: ... -->` comment

### Format rules
- Replace `{{PLACEHOLDER}}` and `_____` with real content — never leave placeholders in filled sections
- Use `[[wiki-links]]` for PARA cross-references (people, projects, resources)
- Keep mood emoji + 2-5 word description: `😊 focused and curious`
- Energy level: a number, 1-10
- Goals: use checkbox format `- [ ] actual goal text`
- IRL Daily Log entries: `- [IRL] Brief description of what happened`

---

## 5. Edit Pattern

When writing to the journal, use the `edit` tool with targeted replacements. Match the exact placeholder text.

Example — filling mood:
```
oldText: "**Mood:** 😊 _____"
newText: "**Mood:** 😊 energized and a bit scattered"
```

Example — filling a goal:
```
oldText: "- [ ] {{PRIMARY_GOAL_1}}"
newText: "- [ ] Finish the daily-journal skill and guide the session"
```

Never use `write` on the whole file — it would wipe the auto sections.

---

## 6. Closing the Session

After writing:
1. Show a clean summary of what was filled
2. Remind the user of any sections still left blank (offer to fill them or leave for later)
3. Confirm the file path: `05_JOURNAL/daily-YYYY-MM-DD.md`
4. If evening session: remind that `journal_agent.py --force --live` should run after any git push

---

## 7. Quick Reference — File & Script Paths

| Thing | Path |
|-------|------|
| Today's journal | `/home/capicuaman/Documents/textDump/05_JOURNAL/daily-$(date +%Y-%m-%d).md` |
| Journal template | `/home/capicuaman/Documents/textDump/05_JOURNAL/daily-note-template.md` |
| Agent script | `/home/capicuaman/Documents/textDump/03_RESOURCES/Workflow_Automation/journal_automation/journal_agent.py` |
| Agent config | `/home/capicuaman/Documents/textDump/03_RESOURCES/Workflow_Automation/journal_automation/config.json` |
| Cron enable | `/home/capicuaman/Documents/textDump/.agents/skills/daily-journal/scripts/enable-cron.sh` |
| Cron disable | `/home/capicuaman/Documents/textDump/.agents/skills/daily-journal/scripts/disable-cron.sh` |
| Cron log | `/home/capicuaman/Documents/textDump/03_RESOURCES/Workflow_Automation/journal_automation/cron.log` |
