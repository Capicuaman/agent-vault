# Technology Onboarding Packet Template

Use this template when `tech-onboarding-orchestrator` decides the user needs a durable teaching/evaluation artifact. Keep it concise unless the user asks for a full study pack.

```markdown
# <Technology> Onboarding Packet

**Source:** <URL/path>
**Snapshot date:** <YYYY-MM-DD>
**Chameleon role:** <role used for this pass>
**Status:** <one-off intake | evaluating | adopted | nerd candidate | skill candidate | agent candidate>

## 1. Why this is on the radar

- <user's reason>
- <problem it may solve>
- <what success would look like locally>

## 2. What it actually is

<Plain-language canon paragraph. Avoid hype.>

## 3. Prior-art check

**What most people use for this job:** <dominant tool/pattern, if known>

**Where this technology fits:**
- <standard / niche / experimental / replacement / complement>

**Adoption signal:** <stars, maintainers, activity, ecosystem references, docs quality, caveats>

## 4. Mental model

Explain the smallest model that makes the technology click:

- Core object: <...>
- Main flow: <...>
- Config/state lives at: <...>
- Extension point: <...>

## 5. Quickstart / 15-minute tour

> Do not install, clone, or run untrusted code unless the user approved it.

```bash
# copy-pasteable commands, if appropriate
```

Verification:

```bash
# command that proves it worked
```

## 6. Teaching artifact decision

Recommended teaching shape: <primer | workflow guide | decision guide | study guide | gamified app | hybrid>

Why this shape:
- <reason>

## 7. Local infrastructure connections

- Existing notes: <paths or none found>
- Existing skills to combine: <skills>
- Existing projects affected: <paths>
- Possible wiki-links: [[...]], [[...]]

## 8. Nerd / forge / prompt-skill-agent triage

### Nerd-worthiness

Recommendation: <no nerd yet | candidate | forge `<thing>-nerd` now>

Evidence:
- <frequency/adoption need>
- <need for factual grounding>
- <stable single-tech scope>

### Forge-scout

Recommendation: <no forge | candidate card needed | use existing forge>

Reason:
- <artifact shape / repetition evidence>

### Prompt / skill / agent

Recommended echelon: <E0 prompt | E1 skill | E2 agent>

Reason:
- <stability/frequency/risk>

## 9. Recommended next moves

1. <next action>
2. <next action>
3. <next action>

## 10. Open questions

- <question>

## Sources

- <URL/path>
```

## Quality bar

Before saving a packet, confirm:

- The source URL/path and snapshot date are present.
- The prior-art section names a standard tool or says why no standard emerged.
- The mental model is not just definitions.
- The nerd/forge/agent decision has evidence, not vibes.
- The next moves are actionable from an SSH session.
