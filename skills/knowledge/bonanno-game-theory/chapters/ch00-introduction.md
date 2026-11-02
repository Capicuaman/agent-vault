# Chapter 0: Introduction

## Core Idea
Game theory is a formal language for representing and analyzing interactive situations: cases where several players choose actions that affect one another. Bonanno frames the book as rigorous non-cooperative game theory for rational players, moving from ordinal preferences to cardinal expected-utility payoffs, then to knowledge, belief, refinements, and incomplete information.

## Frameworks Introduced
- **Interactive situation model**: Represent a situation by players, feasible actions/strategies, outcomes, and preferences; use when verbal strategic reasoning is too vague.
  - When to use: Any decision where another decision-maker's action affects your payoff.
  - How: identify players → list choices → map choice profiles to outcomes → specify each player's preferences/payoffs.
- **Non-cooperative lens**: Analyze interaction without enforceable binding agreements; communication may exist, but contracts do not solve the incentives.
  - When to use: markets, auctions, bargaining without enforceable side contracts, political strategy, mechanism design.
  - How: model incentives at the level of individual optimality, not group welfare.
- **Ordinal/Cardinal split**: Start with preference rankings when only order matters; move to cardinal payoffs when lotteries, risk, and mixed strategies matter.
  - When to use: ordinal for deterministic comparisons; cardinal for expected utility and probability.

## Key Concepts
- **interactive situations**: key concept for introduction.
- **players/actions/outcomes**: key concept for introduction.
- **non-cooperative game theory**: key concept for introduction.
- **ordinal vs cardinal payoffs**: key concept for introduction.
- **knowledge and incomplete information**: key concept for introduction.

## Mental Models
- Use **interactive situations** when you need to formalize the chapter’s strategic situation.
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
