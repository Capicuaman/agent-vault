# Chapter 8: Adding beliefs to knowledge

## Core Idea
Belief enriches knowledge structures with probabilities. Bayesian updating handles positive-probability evidence, while belief revision handles surprises; like-mindedness and agreement results discipline how rational agents' beliefs can diverge.

## Frameworks Introduced
- **Probabilistic belief**: Assign probabilities to possibilities inside a player's information cell.
  - When to use: Model uncertainty quantitatively rather than as mere possibility.
- **Bayesian updating**: Condition prior beliefs on observed events with positive probability.
  - How: posterior(event) = prior(event ∩ evidence) / prior(evidence).
- **Belief revision**: Revise beliefs when the observed event had prior probability zero or was not previously expected.
  - When to use: Off-path information sets and surprise evidence.
- **Harsanyi consistency / like-mindedness**: Players share a coherent probabilistic structure so differences in beliefs arise from different information, not arbitrary priors.
- **Agreeing to disagree**: Under common priors and common knowledge of posteriors, persistent disagreement is constrained or impossible.
  - Use as a diagnostic for whether a model allows heterogeneous priors or asymmetric information.

## Key Concepts
- **probabilistic beliefs**: key concept for adding beliefs to knowledge.
- **conditional probability**: key concept for adding beliefs to knowledge.
- **Bayes rule**: key concept for adding beliefs to knowledge.
- **belief updating**: key concept for adding beliefs to knowledge.
- **belief revision**: key concept for adding beliefs to knowledge.
- **Harsanyi consistency**: key concept for adding beliefs to knowledge.
- **like-mindedness**: key concept for adding beliefs to knowledge.
- **agreeing to disagree**: key concept for adding beliefs to knowledge.

## Mental Models
- Use **probabilistic beliefs** when you need to formalize the chapter’s strategic situation.
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
