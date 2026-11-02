# Patterns

## Build the Game in Layers
**When to use**: Any new strategic situation.
**How**: Identify players → feasible actions/strategies → outcomes → preferences/payoffs → timing → information → beliefs → solution concept.
**Trade-offs**: Slower upfront, but prevents using Nash/SPE/PBE before their assumptions are met.

## Dominance Pruning
**When to use**: Strategic-form games with obviously bad strategies.
**How**: Check strict dominance first; only then consider weak dominance, noting order sensitivity. In cardinal games, also check dominance by mixed strategies.
**Trade-offs**: Strict dominance is robust; weak dominance can delete meaningful equilibria.

## Nash Best-Response Check
**When to use**: Candidate simultaneous-move or strategic-form outcomes.
**How**: For each player, hold others' strategies fixed and ask whether the player can improve by deviating.
**Trade-offs**: Stability concept, not automatically a prediction or welfare criterion.

## Mixed-Strategy Support Method
**When to use**: Finite cardinal strategic-form games with no pure equilibrium or with randomization.
**How**: Guess supports → impose indifference over support strategies → solve probabilities → verify excluded pure strategies are no better.
**Trade-offs**: Efficient for small games; support guesses grow combinatorially.

## Backward Induction
**When to use**: Finite dynamic games with perfect information.
**How**: Solve final decision nodes, replace subtrees with induced outcomes, and iterate backward.
**Trade-offs**: Strong in perfect information; not enough when information sets or off-path beliefs matter.

## Subgame-Perfect Equilibrium Test
**When to use**: Dynamic games with proper subgames.
**How**: Identify every proper subgame and verify the strategy profile induces Nash equilibrium in each.
**Trade-offs**: Eliminates non-credible threats but may be weak in games with few/no proper subgames.

## Assessment-Based Dynamic Analysis
**When to use**: Imperfect-information dynamic games.
**How**: Specify strategies and beliefs at information sets; check sequential rationality and belief consistency.
**Trade-offs**: More realistic off-path analysis, but belief restrictions become conceptually important.

## Bayesian Belief Update
**When to use**: Evidence has positive prior probability.
**How**: Condition probabilities using Bayes' rule.
**Trade-offs**: Clear and disciplined on path; cannot directly handle zero-probability surprises.

## Belief Revision for Off-Path Events
**When to use**: A player reaches an information set that the candidate strategy profile says should not occur.
**How**: Use belief-revision principles or equilibrium consistency requirements to justify revised beliefs.
**Trade-offs**: More conceptually transparent than arbitrary off-path beliefs, but may require extra assumptions.

## Incomplete-Information State-Space Modeling
**When to use**: Players are uncertain about payoff-relevant facts.
**How**: Define states, information partitions, beliefs, state-contingent payoffs, and strategies contingent on information.
**Trade-offs**: Transparent about knowledge and events; less compact than type-space notation for standard Bayesian games.

## Type-Space Translation
**When to use**: You need conventional Harsanyi Bayesian-game notation.
**How**: Encode each player's private information and beliefs as types; define strategies as functions from types to actions.
**Trade-offs**: Compact for equilibrium computation; can hide the underlying event/knowledge structure.
