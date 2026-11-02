---
name: bonanno-game-theory
description: 'Knowledge base from "Game Theory: An open access textbook with 165 solved exercises" by Giacomo Bonanno. Use when applying Bonanno''s frameworks for strategic-form games, dynamic games, Nash equilibrium, common knowledge, belief revision, perfect Bayesian equilibrium, and incomplete information.'
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# Game Theory: An open access textbook with 165 solved exercises
**Author**: Giacomo Bonanno | **Pages**: ~585 | **Chapters**: 16 main chapters/sections | **Generated**: 2026-10-06

## How to Use This Skill

- **Without arguments** — load Bonanno’s core game-theory modeling sequence and solution-concept map.
- **With a topic** — ask about `Nash equilibrium`, `backward induction`, `common knowledge`, `PBE`, `incomplete information`, or another indexed topic; read the relevant chapter file before answering.
- **With chapter** — ask for `ch05`, `chapter 12`, etc.; load that specific chapter.
- **Browse** — ask “what chapters do you have?” to see the full index.

When a request concerns a topic not covered in the Core Frameworks below, read the relevant chapter file before answering.

---

## Core Frameworks & Mental Models

- **Model before solving**: First identify players, choices/strategies, outcomes, preferences/payoffs, timing, information, and beliefs. Only then choose a solution concept.
- **Frame vs game**: A game frame gives the physical/institutional structure; a game adds preferences or payoffs. Use this separation when testing whether a result comes from rules of the environment or from player objectives.
- **Ordinal before cardinal**: Use ordinal preference rankings for deterministic choice and dominance/Nash reasoning where only ordering matters. Use cardinal expected-utility payoffs when lotteries, risk, mixed strategies, or behavioral strategies are involved.
- **Dominance reasoning**: Remove strategies that a rational player should not use. Strict dominance is robust; weak dominance is useful but order-sensitive and can be treacherous.
- **Nash equilibrium**: Use when seeking a self-enforcing profile of strategies: each player's choice is optimal given the others'. Do not treat Nash as prediction until the information and rationality assumptions are justified.
- **Backward induction**: Use for finite perfect-information dynamic games. Solve from terminal decision nodes back to the root to test sequential credibility.
- **Subgame perfection**: Use in dynamic games to require Nash equilibrium in every proper subgame. It eliminates many non-credible threats, but may be too weak when imperfect information leaves few proper subgames.
- **Behavioral strategies**: In extensive-form games with cardinal payoffs, randomize locally at information sets rather than only over complete plans.
- **Knowledge partitions**: Model what a player knows by the set of states they consider possible. An event is known if it holds throughout the relevant information cell.
- **Common knowledge**: Use when everyone knows a fact, everyone knows that everyone knows it, and so on indefinitely. Many equilibrium and rationality arguments implicitly require this stronger condition, not merely mutual knowledge.
- **Belief and Bayes**: Add probabilities to knowledge structures when uncertainty has degrees. Use Bayes' rule at positive-probability information sets; use belief revision principles for surprises/off-path events.
- **Common knowledge of rationality**: Connect epistemic assumptions to solution concepts such as rationalizability. Ask what players know about each other's rationality before claiming a deletion procedure is justified.
- **Assessment**: For dynamic games with imperfect information, reason with both strategies and beliefs. Sequential rationality requires optimal action at each information set given those beliefs.
- **Weak sequential equilibrium**: Requires sequential rationality and Bayesian updating where information sets are reached. Useful first attempt, but too permissive off path.
- **Sequential equilibrium**: Strengthens assessments by requiring consistency of beliefs as limits of fully mixed perturbations. Powerful but technically and conceptually demanding.
- **Perfect Bayesian equilibrium**: Bonanno presents PBE through belief revision and Bayesian consistency. Use it when you need a practical refinement for dynamic games with imperfect information and off-path beliefs.
- **State-space approach to incomplete information**: Model possible states, information, and beliefs directly. Bonanno uses this as the main route into incomplete-information games before explaining type spaces.
- **Type-space approach**: Use Harsanyi types to encode payoff information and belief hierarchies. Translate between state-space and type-space views depending on whether events/knowledge or conventional Bayesian-game notation is more useful.

---

## Chapter Index

| # | Title | Key Frameworks |
|---|-------|----------------|
| [ch00](chapters/ch00-introduction.md) | Introduction | interactive situations, non-cooperative game theory, ordinal/cardinal map |
| [ch01](chapters/ch01-ordinal-games-strategic-form.md) | Ordinal games in strategic form | dominance, iterated deletion, Nash equilibrium, auctions |
| [ch02](chapters/ch02-dynamic-games-perfect-information.md) | Dynamic games with perfect information | trees, strategies, backward induction |
| [ch03](chapters/ch03-general-dynamic-games.md) | General dynamic games | imperfect information, subgames, SPE, chance |
| [ch04](chapters/ch04-expected-utility.md) | Expected Utility | lotteries, risk attitudes, expected utility axioms |
| [ch05](chapters/ch05-mixed-strategies-strategic-form.md) | Mixed strategies in strategic-form games | mixed strategies, support, mixed Nash, rationalizability |
| [ch06](chapters/ch06-dynamic-games-cardinal-payoffs.md) | Dynamic games with cardinal payoffs | behavioral strategies, SPE limitations |
| [ch07](chapters/ch07-knowledge-common-knowledge.md) | Knowledge and common knowledge | information partitions, mutual/common knowledge |
| [ch08](chapters/ch08-beliefs-knowledge.md) | Adding beliefs to knowledge | Bayesian updating, belief revision, like-mindedness |
| [ch09](chapters/ch09-common-knowledge-rationality.md) | Common knowledge of rationality | epistemic rationality, rationalizability |
| [ch10](chapters/ch10-weak-sequential-equilibrium.md) | A First Attempt: Weak Sequential Equilibrium | assessments, sequential rationality, WSE |
| [ch11](chapters/ch11-sequential-equilibrium.md) | Sequential Equilibrium | consistent assessments, trembles, off-path beliefs |
| [ch12](chapters/ch12-perfect-bayesian-equilibrium.md) | Perfect Bayesian Equilibrium | AGM belief revision, Bayesian consistency, PBE |
| [ch13](chapters/ch13-incomplete-information-static-games.md) | Incomplete Information: Static Games | state-space Bayesian games, one/two/multi-sided uncertainty |
| [ch14](chapters/ch14-incomplete-information-dynamic-games.md) | Incomplete Information: Dynamic Games | signaling, belief updates after histories |
| [ch15](chapters/ch15-type-space-approach.md) | Incomplete Information: the type-space approach | Harsanyi types, belief hierarchies, equivalence |

## Topic Index

- **AGM belief revision** → ch12
- **Assessments** → ch10, ch11, ch12
- **Backward induction** → ch02
- **Bayesian updating** → ch08, ch10, ch12, ch14
- **Behavioral strategies** → ch06
- **Belief revision** → ch08, ch12
- **Cardinal payoffs** → ch04, ch05, ch06
- **Chance moves** → ch03
- **Common knowledge** → ch07, ch09
- **Common knowledge of rationality** → ch09
- **Dominance** → ch01, ch05
- **Expected utility** → ch04
- **Imperfect information** → ch03, ch10, ch11, ch12
- **Incomplete information** → ch13, ch14, ch15
- **Information sets** → ch03, ch06, ch10
- **Iterated deletion** → ch01, ch09
- **Mixed strategies** → ch05
- **Nash equilibrium** → ch01, ch05
- **Perfect Bayesian equilibrium / PBE** → ch12
- **Rationalizability** → ch05, ch09
- **Sequential equilibrium** → ch11, ch12
- **Signaling** → ch14
- **State-space approach** → ch13, ch14, ch15
- **Subgame-perfect equilibrium / SPE** → ch03, ch06, ch10
- **Type-space approach** → ch15
- **Weak sequential equilibrium / WSE** → ch10

## Supporting Files

- [glossary.md](glossary.md) — key terms with concise definitions
- [patterns.md](patterns.md) — reusable modeling/solution patterns
- [cheatsheet.md](cheatsheet.md) — decision rules for model and solution-concept choice

---

## Scope & Limits

This skill covers Bonanno’s book content at the level of synthesized frameworks, concepts, and practitioner decision rules. It does not reproduce the textbook or its solved exercises. For formal proofs, exact definitions, and full exercise solutions, consult the source text.
