---
name: metaphors-gamification
description: Apply Lakoff & Johnson's "Metaphors We Live By" conceptual metaphor theory to analyze workflows and design better gamification. Use when designing missions, levels, channels, and reward structures for developer tools (herdr, pi, etc.) or any productivity system. Identifies what each metaphor highlights vs. hides, then maps to gamification mechanics.
---

# Metaphors-as-Gamification-Design

This skill operationalizes **"Metaphors We Live By"** (Lakoff & Johnson, 1980) as a gamification design tool.

## Core Insight

> Conceptual metaphors are not just words — they are **cognitive frames** that determine what we notice, what we do, and what we ignore. Every gamification choice is a metaphor choice.

The book's most powerful tool for design:

> **A metaphor simultaneously HIGHLIGHTS some aspects of a concept and HIDES others.**

This is the gamification design lever: **choose metaphors that highlight the behaviors you want to reinforce.**

---

## The Three Metaphor Types (Lakoff & Johnson)

### 1. Structural Metaphors
One concept is understood in terms of another complete structure.
- `ARGUMENT IS WAR` → you attack positions, defend claims, win/lose
- `TIME IS MONEY` → you spend it, invest it, waste it, save it
- `LIFE IS A JOURNEY` → you have a path, destination, crossroads, setbacks

**Gamification use:** Structural metaphors define the *genre* of the game (quest, battle, race, economy, exploration).

### 2. Orientational Metaphors
Spatial orientation gives conceptual structure (usually UP/DOWN, IN/OUT, CENTER/PERIPHERY).
- `MORE IS UP` → levels go up, status bars fill up, you climb ranks
- `KNOWN IS NEAR` → familiar tools feel close; new skills feel far
- `CONTROL IS CENTER` → HUD, dashboard, home screen are "center"

**Gamification use:** Orientational metaphors define *spatial layout and progress direction* in your UI/UX.

### 3. Ontological Metaphors
Abstract experiences are treated as entities (objects, containers, substances, persons).
- `MIND IS A MACHINE` → it breaks down, needs maintenance, has capacity
- `SKILL IS A RESOURCE` → you earn it, spend it, accumulate it
- `CONTEXT IS A CONTAINER` → you are "in" a flow state, "out" of context, "switching" containers

**Gamification use:** Ontological metaphors define *what can be collected, spent, lost, or filled.*

---

## Protocol: Analyzing a Workflow Through the Metaphor Lens

When asked to gamify a tool or workflow, run this five-step analysis:

### Step 1: Name the Dominant Metaphors Already in Use
List the metaphors already embedded in the tool's language, UI, and naming.
Ask: What does the tool's vocabulary assume?

**Template:**
```
Tool: [name]
Embedded metaphors found:
- "[term]" → assumes [concept] IS [metaphor-source]
  - Highlights: [what it makes visible]
  - Hides: [what it makes invisible]
```

### Step 2: Identify the Workflow's Actual Structure
Map the workflow's real temporal, causal, and social structure:
- What are the inputs and outputs?
- What decisions matter most?
- Where do users get stuck or lose motivation?
- What behaviors should accelerate? What should slow down?

### Step 3: Match Metaphors to Desired Behavior
Use the **Metaphor-to-Mechanic Matrix** (see below).
Ask: Which metaphor HIGHLIGHTS the behavior we want?

### Step 4: Check for Metaphor Coherence
Metaphors must be internally consistent. Mixed metaphors create cognitive friction.
- Bad: "Level up your garden army in the workspace pipeline" (3 incompatible frames)
- Good: "Grow your knowledge forest. Each commit plants a tree." (coherent growth frame)

### Step 5: Design the Gamification Layer
For each chosen metaphor, derive:
- **Progression unit** (what measures advancement)
- **Reward token** (what gets earned)
- **Challenge type** (what creates resistance/stakes)
- **Failure state** (what losing looks like)
- **Social channel** (how others see your progress)

---

## Metaphor-to-Mechanic Matrix

| Metaphor Frame | Highlights | Hides | Progression Unit | Challenge Type | Best for |
|---|---|---|---|---|---|
| **JOURNEY** (quest) | Direction, milestones, setbacks ok | Speed, competition | Steps / Levels | Obstacles on the path | Long learning curves |
| **BATTLE** (war) | Winning, defeating, urgency | Collaboration, iteration | HP / Victories | Enemies, bosses | Short sprints, quick tasks |
| **ECONOMY** (money) | Investment, ROI, scarcity | Intrinsic value | XP / Credits | Resource depletion | Habit formation, daily practice |
| **GARDEN** (growth) | Patience, cultivation, tending | Urgency, competition | Growth / Health | Neglect, weeds | Long projects, skill building |
| **EXPLORATION** (discovery) | Curiosity, unknown territory | Efficiency, goals | Maps / Discoveries | Fog of war, blank zones | Creative tools, research |
| **BUILDING** (construction) | Craft, architecture, foundations | Revision, demolition | Blueprints / Structures | Missing materials, instability | Documentation, knowledge bases |
| **ECOSYSTEM** (biology) | Interdependence, balance, evolution | Control, individual agency | Health / Diversity | Imbalance, extinction | Team workflows, multi-project |

---

## Applied Analysis: herdr

herdr is a **terminal workspace multiplexer with AI agent integration** (sessions → workspaces → panes → tabs).

### Dominant Metaphors Found in herdr

| Term/Feature | Embedded metaphor | Highlights | Hides |
|---|---|---|---|
| "herdr" (name) | WORKSPACE MANAGEMENT IS HERDING LIVESTOCK | Need to keep things together, drift is natural, active wrangling required | Creative agency, collaboration, individual workspace value |
| "sessions" | TIME IS A CONTAINER / WORKFLOW IS A SITTING | Bounded, completable work periods | Continuity across sessions, context persistence |
| "workspaces" | WORK IS A PLACE | Separation, locality, focus | Flow between spaces, shared state |
| "panes" | SCREEN IS A GLASS WINDOW | Visibility, transparency, parallel view | Depth, hierarchy, hidden layers |
| "worktrees" | CODE IS A TREE | Growth, branching, rootedness | Merging, pruning, grafting complexity |
| "missions" (worktree-quest) | TASKS ARE MILITARY MISSIONS | Urgency, completion, objective clarity | Exploration, iteration, meandering as valid strategy |

### Metaphor Coherence Audit

**Current mix:** Ranch (herdr) + Military (missions) + Nature (worktrees) + Spatial (workspaces, panes)

**Verdict:** Mild incoherence — the ranch/herding frame and the military/mission frame are **not the same world.** This creates subtle cognitive friction when using the tool.

**Option A — Lean into RANCH/FRONTIER:**
> Sessions = Roundups | Workspaces = Pastures | Worktrees = Side Trails | Agents = Wranglers | XP = Trail Miles | Missions = Drives (cattle drives) | Panes = Corrals

**Option B — Lean into EXPEDITION/EXPLORATION:**
> Sessions = Expeditions | Workspaces = Basecamp / Field Sites | Worktrees = Scouting Paths | Agents = Scouts | XP = Distance / Discoveries | Missions = Surveys | Panes = Map Views

**Option C — Lean into ECOSYSTEM (most coherent with "herdr" for agent fleets):**
> Sessions = Migration Cycles | Workspaces = Territories | Worktrees = Foraging Routes | Agents = Entities in an ecosystem | XP = Biomass / Vitality | Missions = Migrations | Panes = Observation Posts

### Recommended Gamification Channels for herdr

Based on the **JOURNEY + ECOSYSTEM** combined frame (best coherence with tool structure):

1. **Expedition Log** — each session auto-generates a narrative log entry in PARA. Progress is geographic movement.
2. **Territory Map** — workspaces visualized as a hex-map; active ones glow, dormant ones fade.
3. **Agent Vitality** — pi/agents have a "signal strength" meter that rewards consistent engagement, reflects quality of prompts.
4. **Migration Patterns** — streak system: consecutive days in a workspace accumulate "territory control."
5. **Discovery Markers** — when a new concept/file/API is touched for the first time, a discovery is logged. Unlocks sidebar annotations.
6. **Herd Size** — total active panes/agents is your "herd" score. Game rewards lean herds (focus) over sprawl.

---

## Applied Analysis: pi

pi is a **terminal coding agent harness** with skills, extensions, prompt templates, and themes.

### Dominant Metaphors in pi

| Term/Feature | Embedded metaphor | Highlights | Hides |
|---|---|---|---|
| "pi" (name) | AGENT IS AN INFINITE MATHEMATICAL CONSTANT | Precision, universality, never fully known | Utility, warmth, personality |
| "skills" | COMPETENCY IS A LEARNABLE UNIT | Modularity, acquisition, stacking | Tacit knowledge, emergence, fluency |
| "extensions" | CAPABILITY IS AN APPENDAGE | Add-on, plug-in, outside the core | Deep integration, native feel |
| "themes" | INTERFACE IS CLOTHING | Cosmetic expression, identity | Function, ergonomics, cognitive load |
| "prompts" | LANGUAGE IS A TRIGGER | Precision, repeatability | Exploration, serendipitous phrasing |
| "tools" | CAPABILITIES ARE PHYSICAL INSTRUMENTS | Concrete use, purpose-built | Meta-capabilities, judgment |

### Recommended Gamification Channels for pi

Frame: **LIBRARY / ATELIER** (craft + knowledge)

> You are building your studio. Each skill loaded is a tool on the wall. Each session is a commissioned work.

1. **Skill Acquisition Tree** — visual tree of installed skills. Unlocking a new skill reveals what it connects to.
2. **Prompt Refinement Score** — tracks how often prompt templates are reused vs. typed from scratch. Rewards template investment.
3. **Session Depth** — counts tool calls per session. Rewards deep engagement over shallow queries.
4. **Knowledge Graph Growth** — graphify integration: each session adds nodes. Visualized as a growing constellation.
5. **Mastery Badges** — earned when a skill has been used N times across sessions. Visible in skill list.

---

## When to Use This Skill

Activate this skill when:
- Designing or redesigning gamification for a developer tool or productivity app
- Choosing between competing UI metaphors for a new feature
- Diagnosing why a gamification system feels incoherent or unmotivating
- Writing mission text, level names, or reward copy
- Evaluating whether a borrowed gamification pattern fits the tool's native metaphor

## Output Format

Always produce:
1. **Metaphor audit table** — what metaphors are already embedded
2. **Coherence verdict** — are they compatible? Where is the friction?
3. **Recommended frame** — one dominant metaphor family to anchor the design
4. **Gamification channel list** — 4–6 concrete mechanics derived from the chosen frame
5. **Mission/level name suggestions** — using the chosen metaphor's vocabulary

---

## Reference: Key Passages from Lakoff & Johnson

- *"Metaphors may create realities for us, especially social realities. A metaphor may thus be a guide for future action. Such actions will, of course, fit the metaphor. This will, in turn, reinforce the power of the metaphor to make experience coherent."* (p. 156)
- *"The most important thing that metaphors create is partial understanding."* (p. 153)
- *"In allowing us to focus on one aspect of a concept, a metaphorical concept can keep us from focusing on other aspects."* (p. 10)

These are design rules: the metaphors you embed in your tool will literally shape what users notice and do inside it.
