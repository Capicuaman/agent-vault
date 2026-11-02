# Chapter 1: Ordinal games in strategic form

## Core Idea
A strategic-form game separates the physical possibilities of interaction from players' preferences, then studies which strategies survive dominance reasoning or mutual best-response reasoning. This chapter establishes the basic solution concepts for ordinal games.

## Frameworks Introduced
- **Game frame vs game**: A frame specifies players, choices, and outcome function; a game adds each player's preference ranking over outcomes.
  - When to use: Separate institutional design from preference assumptions.
  - How: define players and strategy sets, define outcomes for every strategy profile, then attach preferences.
- **Strict dominance**: A strategy is strictly dominated when another strategy gives a strictly better outcome against every opponent profile.
  - When to use: Eliminate choices a rational player should never use.
  - How: compare one strategy to alternatives row-by-row/column-by-column across all contingencies.
- **Weak dominance**: A strategy is weakly dominated when another is never worse and sometimes better.
  - When to use: Flag fragile strategies, but be cautious: deletion order can matter.
- **Iterated deletion procedures**: Repeatedly remove dominated strategies to simplify the game.
  - When to use: Find rationalizable candidates before looking for equilibrium.
  - Failure mode: weak-dominance deletion may remove equilibria or depend on order.
- **Nash equilibrium**: A strategy profile where every player's strategy is a best response to the others.
  - When to use: Model stable self-enforcing outcomes in simultaneous or strategically reduced interaction.
- **Second-price auction logic**: Truthful bidding is strategically robust because the winner pays the second-highest bid, not their own bid.
- **Pivotal mechanism**: Align private reports with social choice by charging players for the externality their report imposes.

## Key Concepts
- **game frames**: key concept for ordinal games in strategic form.
- **strict dominance**: key concept for ordinal games in strategic form.
- **weak dominance**: key concept for ordinal games in strategic form.
- **second-price auction**: key concept for ordinal games in strategic form.
- **pivotal mechanism**: key concept for ordinal games in strategic form.
- **iterated deletion**: key concept for ordinal games in strategic form.
- **Nash equilibrium**: key concept for ordinal games in strategic form.
- **infinite strategy sets**: key concept for ordinal games in strategic form.

## Mental Models
- Use **game frames** when you need to formalize the chapter’s strategic situation.
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
