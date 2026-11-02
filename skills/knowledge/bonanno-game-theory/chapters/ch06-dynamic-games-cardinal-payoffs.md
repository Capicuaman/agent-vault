# Chapter 6: Dynamic games with cardinal payoffs

## Core Idea
Dynamic games with cardinal payoffs allow randomization at information sets through behavioral strategies. Subgame-perfect equilibrium remains useful but can be too weak when imperfect information leaves no proper subgames to discipline off-path beliefs.

## Frameworks Introduced
- **Behavioral strategy**: At each information set, assign a probability distribution over available actions.
  - When to use: Extensive-form games where players may randomize locally.
- **SPE revisited with cardinal payoffs**: Use Nash equilibrium in every subgame, now allowing mixed/behavioral strategies.
  - How: solve continuation games at proper subgames and verify consistency with root play.
- **Limitation of subgame perfection**: If a dynamic game has few or no proper subgames, SPE may fail to eliminate implausible behavior at unreached information sets.
  - Use this smell to move toward sequential, weak sequential, or perfect Bayesian equilibrium.

## Key Concepts
- **behavioral strategies**: key concept for dynamic games with cardinal payoffs.
- **mixed strategies in extensive form**: key concept for dynamic games with cardinal payoffs.
- **subgame-perfect equilibrium revisited**: key concept for dynamic games with cardinal payoffs.
- **problems with SPE**: key concept for dynamic games with cardinal payoffs.

## Mental Models
- Use **behavioral strategies** when you need to formalize the chapter’s strategic situation.
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
