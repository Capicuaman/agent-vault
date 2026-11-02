# Chapter 5: Mixed strategies in strategic-form games

## Core Idea
Once payoffs are cardinal, players can randomize over pure strategies. Mixed-strategy equilibrium is found by making opponents indifferent among the pure strategies they mix over, while excluding strategies that cannot be optimal.

## Frameworks Introduced
- **Mixed strategy**: A probability distribution over a player's pure strategies.
  - When to use: Model unpredictability or equilibrium in games with no pure Nash equilibrium.
- **Expected payoff against a mixed strategy**: Weight payoffs by the probabilities assigned to opponents' pure strategies.
- **Mixed-strategy Nash equilibrium**: Each player's mixed strategy is a best response to the others' mixed strategies.
  - How: identify support candidates → impose indifference within each support → verify excluded strategies are no better → check probabilities.
- **Support**: Pure strategies assigned positive probability in a mixed strategy.
  - Rule: In equilibrium, all pure strategies in a player's support must yield the same expected payoff.
- **Strict dominance and rationalizability with cardinal payoffs**: A pure strategy may be dominated by a mixed strategy, not only by another pure strategy.
  - Use when pruning before equilibrium computation.

## Key Concepts
- **cardinal payoffs**: key concept for mixed strategies in strategic-form games.
- **mixed strategies**: key concept for mixed strategies in strategic-form games.
- **mixed-strategy Nash equilibrium**: key concept for mixed strategies in strategic-form games.
- **support**: key concept for mixed strategies in strategic-form games.
- **indifference**: key concept for mixed strategies in strategic-form games.
- **strict dominance**: key concept for mixed strategies in strategic-form games.
- **rationalizability**: key concept for mixed strategies in strategic-form games.

## Mental Models
- Use **cardinal payoffs** when you need to formalize the chapter’s strategic situation.
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
