# Chapter 4: Expected Utility

## Core Idea
Cardinal game theory requires payoffs that represent preferences over lotteries, not merely rankings over certain outcomes. Expected utility turns risky prospects into comparable numerical values under a set of consistency axioms.

## Frameworks Introduced
- **Lottery**: A probability distribution over basic outcomes.
  - When to use: Model decisions where final outcomes are uncertain.
- **Expected utility**: Evaluate a lottery by summing utility(outcome) × probability(outcome).
  - When to use: Compare risky prospects and build cardinal payoffs for mixed-strategy games.
- **Risk attitude**: Utility curvature represents risk aversion, neutrality, or love of risk over money outcomes.
  - How: concave utility → risk averse; linear → risk neutral; convex → risk seeking.
- **Representation theorem**: If preferences over lotteries satisfy the expected-utility axioms, they can be represented by a utility function unique up to positive affine transformations.
  - Practical implication: Only positive affine transformations preserve expected-utility meaning; arbitrary ordinal transformations do not.
- **Axiomatic discipline**: Independence and continuity assumptions justify treating lottery choices numerically rather than rhetorically.

## Key Concepts
- **money lotteries**: key concept for expected utility.
- **risk attitudes**: key concept for expected utility.
- **expected utility representation**: key concept for expected utility.
- **axioms**: key concept for expected utility.
- **von Neumann-Morgenstern utility**: key concept for expected utility.

## Mental Models
- Use **money lotteries** when you need to formalize the chapter’s strategic situation.
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
