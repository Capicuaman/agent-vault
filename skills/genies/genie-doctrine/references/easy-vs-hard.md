# What Is Easy vs What Is Hard

Extracted from real change artifacts. The point is to build accurate intuition:
what looks hard is often easy, and what looks easy is where the career is spent.

## Easy (and chronically underestimated)

Not worthless — this is the visible 80% of a feature. But it does not build
judgment, because it lives entirely inside boundaries you control.

- **The happy path.** Intended input → intended output.
- **The isolated feature.** One function, screen, or endpoint, no interaction.
- **"Works on my machine."** Your OS, shell, encoding, config.
- **Adding to a catalog.** A new model, provider, enum value, config field.
- **Rendering and plumbing.** Moving data A→B with no state and no concurrency.

> **Tell:** if you can describe the change without the words *state*, *other*,
> *concurrent*, *version*, *environment*, or *exit path*, it is probably easy.

## Hard (and it is almost never the algorithm)

Algorithms are usually the easy part: self-contained, testable, closed. The hard
parts are open systems.

| Hard thing | Symptom | Practice |
|---|---|---|
| **Lifecycle & state** | "works until you close it wrong / cancel / crash" | Ask who owns the state and who releases it on every exit path. |
| **Concurrency & admission** | "works alone, fails under load / in parallel" | Reason about admission, backpressure, cancellation — not just correctness. |
| **Cross-platform reality** | "works on Linux, breaks on Windows" | Treat the environment as untrusted input; normalize at the boundary. |
| **Caching & consistency** | "correct but slow / stale / silently wrong after a change" | For every cache, name what invalidates it and who guarantees it. |
| **Failure semantics** | "retried a permanent error" / "gave up on a blip" | Classify errors by cause, not by message substring. |
| **Backward compatibility** | "the upgrade broke everyone's config" | Design the change path, not just the new shape. |
| **Reproducibility** | "works in dev, fails on fresh install / CI" | Build from clean, on target, with pinned inputs. |
| **Input space** | "one weird input breaks it" | Enumerate input classes, not examples. Test empty and non-ASCII first. |

## The meta-lesson

> The hard part of software is not writing code that does the thing. It is writing
> code that keeps doing the thing in an environment you do not control, across
> states you did not enumerate, for people whose needs change.

Every "hard" row above is a version of that sentence. Reading change artifacts
proves it, over and over, in a hundred concrete ways.

## What this implies for practice

- Do not practice by building more happy paths. You already can.
- Practice by **adding the boundary**: cancel it mid-flight, run it from a clean
  checkout, feed it the weird encoding, upgrade the dependency, simulate the
  failure.
- Read the *Fixed* sections of changelogs, not the *Added* sections. Added teaches
  what is possible; Fixed teaches what is fragile.
