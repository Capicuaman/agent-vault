# Chapter 10: A First Attempt: Weak Sequential Equilibrium

## Core Idea
Weak sequential equilibrium combines strategies with beliefs and requires optimality at information sets plus Bayesian updating where possible. It improves on SPE in some cases but does not fully refine subgame-perfect equilibrium.

## Frameworks Introduced
- **Assessment**: A pair consisting of a strategy profile and a belief system over nodes at information sets.
  - When to use: Analyze dynamic games where choices depend on beliefs about where the player is.
- **Sequential rationality**: At every information set, the player's planned action must be optimal given their beliefs and future strategy profile.
- **Bayesian updating at reached information sets**: Beliefs at information sets reached with positive probability should follow Bayes' rule from the strategy profile.
- **Weak sequential equilibrium (WSE)**: An assessment satisfying sequential rationality and Bayesian consistency at reached information sets.
  - Strength: eliminates some strictly dominated or non-credible behavior.
  - Weakness: leaves too much freedom at unreached information sets and may fail as an SPE refinement.

## Key Concepts
- **assessments**: key concept for a first attempt: weak sequential equilibrium.
- **sequential rationality**: key concept for a first attempt: weak sequential equilibrium.
- **Bayesian updating**: key concept for a first attempt: weak sequential equilibrium.
- **weak sequential equilibrium**: key concept for a first attempt: weak sequential equilibrium.
- **reached information sets**: key concept for a first attempt: weak sequential equilibrium.

## Mental Models
- Use **assessments** when you need to formalize the chapter’s strategic situation.
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
