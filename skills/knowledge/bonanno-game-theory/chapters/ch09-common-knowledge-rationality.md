# Chapter 9: Common knowledge of rationality

## Core Idea
The chapter connects epistemic assumptions to solution concepts. Common knowledge of rationality supports iterated elimination-style reasoning in strategic-form games, but dynamic games require care because rationality at unreached nodes depends on beliefs.

## Frameworks Introduced
- **Model of a strategic-form game**: Combine game structure with states describing players' choices, beliefs, and knowledge.
- **Rationality event**: A player is rational at a state if their chosen strategy is optimal given their beliefs at that state.
- **Common knowledge of rationality (CKR)**: Everyone is rational, everyone knows everyone is rational, and so on.
  - When to use: Justify solution concepts from assumptions about players' minds rather than from external equilibrium selection.
- **CKR → rationalizability link**: Strategies compatible with common knowledge of rationality are those surviving appropriate iterated deletion/rationalizability procedures.
- **Dynamic-game warning**: Rationality in extensive forms cannot be evaluated only at reached nodes; beliefs about unreached contingencies matter.

## Key Concepts
- **models of strategic-form games**: key concept for common knowledge of rationality.
- **rationality**: key concept for common knowledge of rationality.
- **common knowledge of rationality**: key concept for common knowledge of rationality.
- **rationalizability**: key concept for common knowledge of rationality.
- **extensive-form implications**: key concept for common knowledge of rationality.

## Mental Models
- Use **models of strategic-form games** when you need to formalize the chapter’s strategic situation.
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
