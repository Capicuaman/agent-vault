# Chapter 12: Perfect Bayesian Equilibrium

## Core Idea
Perfect Bayesian equilibrium is presented as an intermediate refinement anchored in belief revision rather than only topological limits. It combines sequential rationality with Bayesian consistency and additional restrictions that can bridge toward sequential equilibrium.

## Frameworks Introduced
- **AGM belief revision lens**: Treat off-path learning as revision of beliefs when unexpected information arrives.
  - When to use: Give conceptual structure to beliefs at zero-probability information sets.
- **Bayesian consistency**: Beliefs must follow Bayes' rule wherever the conditioning event has positive probability, and satisfy coherent restrictions elsewhere.
- **Perfect Bayesian equilibrium (PBE)**: An assessment satisfying sequential rationality and suitable consistency requirements on beliefs.
  - How: specify strategies → compute on-path beliefs by Bayes' rule → justify off-path beliefs by revision principles → check optimality at every information set.
- **Adding independence**: Additional independence restrictions can constrain how beliefs revise after surprises.
- **PBE–sequential equilibrium bridge**: With strengthened consistency conditions, PBE-style requirements can characterize sequential equilibrium without relying directly on the original topological formulation.

## Key Concepts
- **belief revision**: key concept for perfect bayesian equilibrium.
- **AGM consistency**: key concept for perfect bayesian equilibrium.
- **Bayesian consistency**: key concept for perfect bayesian equilibrium.
- **perfect Bayesian equilibrium**: key concept for perfect bayesian equilibrium.
- **independence**: key concept for perfect bayesian equilibrium.
- **sequential equilibrium characterization**: key concept for perfect bayesian equilibrium.

## Mental Models
- Use **belief revision** when you need to formalize the chapter’s strategic situation.
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
