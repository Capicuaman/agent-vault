# Chapter 7: Knowledge and common knowledge

## Core Idea
Bonanno models knowledge using possible states and information partitions: what an individual knows is what holds throughout the states they consider possible. The chapter then iterates knowledge across players to define common knowledge.

## Frameworks Introduced
- **Information partition**: A division of possible states into cells representing what a player can distinguish.
  - When to use: Formalize who knows what under uncertainty.
- **Individual knowledge operator**: A player knows an event when the event contains all states in that player's information cell at the actual state.
  - How: locate actual state → find player's cell → check whether the event holds across the whole cell.
- **Interactive knowledge**: Model statements such as “player 1 knows that player 2 knows E” by nesting knowledge operators.
- **Mutual knowledge vs common knowledge**: Mutual knowledge means everyone knows E; common knowledge means everyone knows E, everyone knows everyone knows E, and so on indefinitely.
  - When to use: Coordination, equilibrium reasoning, public announcements, and assumptions about rationality.

## Key Concepts
- **individual knowledge**: key concept for knowledge and common knowledge.
- **information partitions**: key concept for knowledge and common knowledge.
- **interactive knowledge**: key concept for knowledge and common knowledge.
- **mutual knowledge**: key concept for knowledge and common knowledge.
- **common knowledge**: key concept for knowledge and common knowledge.

## Mental Models
- Use **individual knowledge** when you need to formalize the chapter’s strategic situation.
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
