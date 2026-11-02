# Chapter 2: Dynamic games with perfect information

## Core Idea
Perfect-information dynamic games are modeled as trees where each player observes all previous moves. Backward induction selects plans that are optimal from the end of the tree backward, making credible sequential reasoning explicit.

## Frameworks Introduced
- **Game tree/frame**: Represent temporal order with decision nodes, available choices, successor nodes, and terminal outcomes.
  - When to use: Any interaction where timing and observed history matter.
- **Backward induction**: Solve finite perfect-information games by choosing optimal actions at final decision nodes, replacing them with their induced outcomes, then moving backward.
  - When to use: Finite games with no simultaneous moves or hidden actions.
  - How: mark terminal payoffs → solve last decision nodes → collapse solved subtrees → repeat to root.
- **Strategy in a dynamic game**: A complete contingent plan specifying what a player would do at every decision node they control.
  - When to use: Convert dynamic games to strategic form or reason about off-path behavior.
- **Credibility test**: A threat or promise must be optimal when its decision node is reached, not merely useful ex ante.
  - Use when evaluating commitments in negotiations, entry deterrence, or bargaining.

## Key Concepts
- **trees**: key concept for dynamic games with perfect information.
- **decision nodes**: key concept for dynamic games with perfect information.
- **terminal nodes**: key concept for dynamic games with perfect information.
- **backward induction**: key concept for dynamic games with perfect information.
- **strategies**: key concept for dynamic games with perfect information.
- **subgame-perfect reasoning**: key concept for dynamic games with perfect information.

## Mental Models
- Use **trees** when you need to formalize the chapter’s strategic situation.
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
