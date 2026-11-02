# Chapter 15: Incomplete Information: the type-space approach

## Core Idea
The final chapter presents Harsanyi's type-space approach and relates it to the state-space method used earlier. Types encode payoff-relevant information and beliefs; state-space and type-space representations can be converted into one another.

## Frameworks Introduced
- **Type of a player**: A formal object encoding what the player knows and believes, often including payoff information and beliefs about others' types.
- **Types that know their own payoffs**: A type determines the player's payoff function, simplifying Bayesian-game representation.
- **General type-space case**: Types may encode richer belief hierarchies, including beliefs about others' beliefs.
- **State-space ↔ type-space conversion**: Translate states and information/belief structures into types, and conversely reconstruct state-like descriptions from type profiles.
  - When to use: Choose state-space for transparency of events and knowledge; choose type-space for conventional Bayesian-game notation.
- **Harsanyi program**: Turn incomplete information into imperfect information about types so standard strategic reasoning can be applied.

## Key Concepts
- **types**: key concept for incomplete information: the type-space approach.
- **type spaces**: key concept for incomplete information: the type-space approach.
- **payoff types**: key concept for incomplete information: the type-space approach.
- **belief hierarchies**: key concept for incomplete information: the type-space approach.
- **state-space/type-space equivalence**: key concept for incomplete information: the type-space approach.

## Mental Models
- Use **types** when you need to formalize the chapter’s strategic situation.
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
