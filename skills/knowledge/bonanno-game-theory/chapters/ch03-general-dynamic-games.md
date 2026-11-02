# Chapter 3: General dynamic games

## Core Idea
General dynamic games add imperfect information, simultaneous-like uncertainty, subgames, and chance moves. The main refinement is subgame-perfect equilibrium: Nash equilibrium applied consistently to every proper subgame.

## Frameworks Introduced
- **Information set**: A collection of decision nodes a player cannot distinguish between when choosing.
  - When to use: Model hidden actions, simultaneous moves, or uncertainty about prior choices.
- **Strategy under imperfect information**: A contingent plan assigning the same action at all nodes within an information set.
  - Constraint: indistinguishable nodes cannot have different planned actions.
- **Subgame**: A portion of an extensive-form game that starts at a singleton information set and contains all successors without cutting information sets.
  - When to use: Find places where continuation play can be evaluated independently.
- **Subgame-perfect equilibrium (SPE)**: A strategy profile that induces a Nash equilibrium in every subgame.
  - When to use: Eliminate non-credible threats in dynamic games.
- **Chance moves**: Nature selects among branches according to specified probabilities.
  - When to use: Model exogenous uncertainty separately from strategic choice.

## Key Concepts
- **imperfect information**: key concept for general dynamic games.
- **information sets**: key concept for general dynamic games.
- **strategies**: key concept for general dynamic games.
- **subgames**: key concept for general dynamic games.
- **subgame-perfect equilibrium**: key concept for general dynamic games.
- **chance moves**: key concept for general dynamic games.

## Mental Models
- Use **imperfect information** when you need to formalize the chapter’s strategic situation.
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
