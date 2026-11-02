# Chapter 14: Incomplete Information: Dynamic Games

## Core Idea
Dynamic incomplete-information games combine hidden payoff-relevant states with observed histories. Players update beliefs from actions, so equilibrium reasoning requires both strategic plans and beliefs after histories.

## Frameworks Introduced
- **Dynamic incomplete-information model**: Combine an extensive-form structure with states of nature, information, and belief revision after observed actions.
- **Signaling logic**: Actions can convey information about private states, so strategies affect both payoffs and beliefs.
  - When to use: Entry games, reputation, bargaining with private values, informed-sender interactions.
- **Beliefs after histories**: Players must form posterior beliefs over payoff-relevant states after observing play.
- **Sequential rationality under incomplete information**: At each information set/history, actions must maximize expected payoff given current beliefs.
- **Multi-sided private information**: When multiple players' types/states are unknown, strategies and beliefs must account for nested uncertainty.

## Key Concepts
- **dynamic incomplete information**: key concept for incomplete information: dynamic games.
- **signaling**: key concept for incomplete information: dynamic games.
- **one-sided incomplete information**: key concept for incomplete information: dynamic games.
- **multi-sided incomplete information**: key concept for incomplete information: dynamic games.
- **beliefs after histories**: key concept for incomplete information: dynamic games.
- **sequential rationality**: key concept for incomplete information: dynamic games.

## Mental Models
- Use **dynamic incomplete information** when you need to formalize the chapter’s strategic situation.
- Think in **solution concepts** only after the information, timing, and payoff assumptions are explicit.
- Prefer Bonanno’s separation of frames, preferences, beliefs, and strategies to avoid mixing institutional facts with rationality assumptions.

## Anti-patterns
- **Solving before modeling**: Jumping to equilibrium language before specifying players, choices, information, payoffs, and beliefs.
- **Confusing ordinal and cardinal payoffs**: Treating rank-only preferences as if expected-payoff arithmetic were meaningful.
- **Ignoring off-path contingencies**: In dynamic games, a strategy is a complete contingent plan, not merely the path expected to occur.

## Reference Tables
| Modeling question | Use this chapter when... | Output you should produce |
|---|---|---|
| What is the strategic object? | The chapter's assumptions match your situation | Players, strategies/actions, outcomes, preferences/payoffs |
| What information is available? | Timing, uncertainty, or hidden information matters | Information sets, knowledge cells, beliefs, or types |
| What solution concept is justified? | Rationality/stability assumptions are explicit | Dominance, Nash, backward induction, SPE, WSE, sequential equilibrium, PBE, or Bayesian equilibrium |

## Worked Example
A compact way to apply this chapter is to build the model in layers: first list players and feasible choices, then add outcomes and preferences/payoffs, then add timing and information, and only then apply the chapter's solution concept. For example, if a seller and buyer interact under hidden valuation, do not begin with “the equilibrium is...”. First ask whether values are ordinal or cardinal, whether moves are simultaneous or dynamic, what each side observes, and how beliefs update after observed actions.

## Key Takeaways
1. Make the informational assumptions visible; most mistakes in game theory are hidden information mistakes.
2. Pick the weakest solution concept that your assumptions actually justify.
3. In dynamic games, strategies specify contingent behavior at information sets, including unreached ones.
4. Cardinal payoff analysis requires expected-utility structure; ordinal rankings are not enough for mixed-strategy arithmetic.
5. Beliefs are part of the object of analysis whenever players are uncertain about nodes, states, or types.

## Connects To
- **SKILL.md Core Frameworks**: high-level navigation across Bonanno’s modeling sequence.
- **cheatsheet.md**: quick decision guide for selecting solution concepts.
- **glossary.md**: compact definitions of the terms introduced here.
