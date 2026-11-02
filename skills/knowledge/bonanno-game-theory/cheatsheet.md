# Bonanno Game Theory Cheatsheet

## Choose the Model

| If the situation has... | Model as... | Start with |
|---|---|---|
| One-shot/simultaneous choices | Strategic-form game | Ch 1 or Ch 5 |
| Observable sequence of moves | Dynamic game with perfect information | Ch 2 |
| Hidden prior moves or simultaneous moments | Dynamic game with imperfect information | Ch 3 |
| Risk, lotteries, or randomization | Cardinal expected-utility game | Ch 4–6 |
| Uncertainty about payoff-relevant facts | Incomplete-information game | Ch 13–15 |
| Reasoning about who knows what | Knowledge/belief model | Ch 7–9 |

## Choose the Solution Concept

| Need | Use | Because |
|---|---|---|
| Remove never-rational choices | Strict dominance | It does not depend on beliefs about exact opponent play |
| Find stable simultaneous outcome | Nash equilibrium | No player can profitably deviate unilaterally |
| Solve finite perfect-information dynamics | Backward induction | Later optimality determines earlier credible choices |
| Eliminate non-credible threats | Subgame-perfect equilibrium | Requires Nash behavior in every subgame |
| Analyze randomization | Mixed-strategy Nash | Support strategies must be payoff-indifferent |
| Handle imperfect-information dynamics | Assessment + sequential rationality | Strategies alone are not enough; beliefs matter |
| Add weak belief consistency | Weak sequential equilibrium | Bayes' rule at reached information sets |
| Discipline off-path beliefs strongly | Sequential equilibrium | Beliefs are limits of fully mixed trembles |
| Practical dynamic incomplete-information refinement | Perfect Bayesian equilibrium | Sequential rationality + Bayesian/belief-revision consistency |

## Fast Smells

- If you are averaging payoffs but only have ordinal rankings, stop: you need cardinal expected utility.
- If a “strategy” only says what happens on the expected path, stop: strategies are complete contingent plans.
- If a dynamic game has imperfect information, ask what beliefs players hold at each information set.
- If an equilibrium relies on a threat that would be irrational when reached, test SPE/backward induction.
- If an information set is reached with zero probability, Bayes' rule alone will not pin down beliefs.
- If players disagree despite shared priors and common knowledge of posteriors, check whether assumptions really imply agreement.
- If incomplete information is messy, choose between state-space clarity and type-space compactness deliberately.

## Computation Defaults

1. Pure strategic-form game: list best responses; intersect them for pure Nash equilibria.
2. Mixed 2×2 game: make each player indifferent between support actions; solve probabilities; verify.
3. Perfect-information tree: backward induction.
4. Dynamic game with subgames: solve terminal subgames first; verify SPE.
5. Imperfect-information dynamic game: propose assessment; check sequential rationality; compute on-path beliefs; justify off-path beliefs.
6. Incomplete-information static game: define states/types; strategies map private information to actions; compute expected payoffs by beliefs.
