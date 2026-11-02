# Chapter 13: Incomplete Information: Static Games

## Core Idea
Incomplete-information games are modeled with states that determine payoffs, knowledge, and beliefs. Bonanno emphasizes a state-space approach rather than starting with Harsanyi types, then applies it to static games with one-sided, two-sided, and multi-sided uncertainty.

## Frameworks Introduced
- **State-space approach**: Model uncertainty using possible states, players' information, beliefs, and state-dependent games.
  - When to use: Represent incomplete information directly without immediately introducing types.
- **Incomplete information**: At least one player is uncertain about payoffs, available actions, or relevant features of the strategic situation.
- **One-sided incomplete information**: One player has private information while others are uncertain about it.
- **Two-sided/multi-sided incomplete information**: Multiple players hold private information and beliefs about others' information.
- **Bayesian strategic reasoning**: A strategy must prescribe actions across the player's information possibilities and be optimal in expected payoff given beliefs.
  - Use when solving auctions, signaling-free private-value games, or static games with payoff uncertainty.

## Key Concepts
- **state-space approach**: key concept for incomplete information: static games.
- **incomplete information**: key concept for incomplete information: static games.
- **one-sided incomplete information**: key concept for incomplete information: static games.
- **two-sided incomplete information**: key concept for incomplete information: static games.
- **multi-sided incomplete information**: key concept for incomplete information: static games.
- **Bayesian games**: key concept for incomplete information: static games.

## Mental Models
- Use **state-space approach** when you need to formalize the chapter’s strategic situation.
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
