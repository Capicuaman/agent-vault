# The Boundary Doctrine

The single most useful idea in this family.

> **Nearly every hard bug is a collision with a boundary the author did not
> control.** The easy work lives entirely inside boundaries you fully own. The
> hard work is lifecycle, concurrency, environment, and interfaces with things
> you cannot see.

So for any fix, artifact, or diff, ask the one question that unlocks it:

> **Which boundary did this cross?**

## Why this is the right abstraction

Bug trackers classify by *symptom* ("grep returns wrong results"), which does not
transfer. Boundaries classify by *cause shape*, which does. Once you can name the
boundary, you can predict the bug class in code you have never seen — and design
it out before it exists.

## The seven classes

### 1. Environment
**You do not control the machine.** OS, shell, encoding, `PATH`, locale,
filesystem semantics, user-set config, the launch directory.

- **Detection questions:** What does this assume about the OS, shell, encoding,
  or working directory? What user-controlled variable changes its semantics?
  What tool wrote the file it is reading?
- **Symptoms:** "works on Linux, breaks on Windows"; "works in my shell"; "works
  from the project dir".
- **Real examples:** PowerShell 5.1 prepends a UTF-8 BOM that breaks JSON parsing;
  `RIPGREP_CONFIG_PATH` silently turning regex searches literal; Nix putting its
  own Node first on `PATH`; `.env` files leaking from the launch directory.
- **Design implication:** treat the environment as untrusted input. Normalize at
  the boundary. Prefer explicit config over ambient config.

### 2. Lifecycle / state
**State that outlives the thing that set it.** Start/stop ordering, cleanup on
abnormal exit, resumption, ownership.

- **Detection questions:** Who sets this state? Who releases it on *every* exit
  path, including cancel, crash, and kill? What happens on resume?
- **Symptoms:** "works until you close it wrong"; "the terminal is broken after";
  "fine on a fresh session, broken after resume".
- **Real examples:** terminal left in mouse-tracking / alt-screen mode after an
  abnormal exit; a background clipboard helper suspended with the parent process;
  resumed sessions losing tools registered after the branch was recorded.
- **Design implication:** assign an owner and a release path. Prefer state that
  dies with its scope.

### 3. Concurrency
**You do not control interleaving.** Admission, queues, backpressure, races,
cancellation.

- **Detection questions:** How many can run at once? What happens at the limit?
  What happens when one is cancelled mid-flight? What is counted as alive?
- **Symptoms:** "works alone, fails in parallel / under load"; "sometimes".
- **Real examples:** scripts failing immediately when both workers were busy
  (now queue with a deadline); a second dialog replacing the first so its promise
  never settled; cancelled workers still counted toward the limit.
- **Design implication:** reason about admission and cancellation, not just
  correctness. Queue with a deadline rather than failing fast.

### 4. Interface / contract
**You do not control the other side.** Third-party APIs, protocols, providers,
proxies, caches you can only observe, undocumented limits.

- **Detection questions:** Who else implements this contract? What are its
  undocumented limits? What does it cache, and what invalidates it? What is
  retryable and what is permanent?
- **Symptoms:** "works against one provider, fails against another"; "correct but
  slow"; "stale after a change"; "retries a permanent error".
- **Real examples:** prompt cache lost on every deferred tool load; HTTP 413 on
  large bodies instead of compacting; a strict tool set rejected for grammar size
  and needing a non-strict retry.
- **Design implication:** classify errors by *cause*, not by message substring.
  For every cache, name the invalidation guarantee.

### 5. Input space
**You did not enumerate it.** Encodings, punctuation, malformed data, unenumerated
states, adversarial strings.

- **Detection questions:** What classes of input exist, not examples? What about
  empty, whitespace-only, non-ASCII, malformed escapes, regex metacharacters?
- **Symptoms:** "one weird input breaks it"; "fine for English".
- **Real examples:** a bare `\r\n` tool output causing 400s; CJK punctuation
  breaking Markdown emphasis; `\usepackage` breaking JSON escape parsing; `[` and
  `(` breaking file autocomplete.
- **Design implication:** enumerate input *classes*. Test the empty and the
  non-ASCII case first.

### 6. Human / time
**You do not control the future.** Backward compatibility, deprecation windows,
migration, changed defaults, retired upstream models.

- **Detection questions:** Who depends on the current shape? What is the change
  path for them? How long is the deprecation window? What default are we changing
  under someone's feet?
- **Symptoms:** "the upgrade broke everyone's config"; "silently different".
- **Real examples:** published schema URLs moving; a handler event becoming a
  union; a default model being retired by the provider.
- **Design implication:** design the *change path*, not just the new shape. Ship
  the migration guide with the breaking change.

### 7. Reproducibility
**You do not control the build graph.** Packaging, dependency resolution,
environment leakage, determinism, installers.

- **Detection questions:** Does this work from a clean checkout, on the target, with
  pinned inputs? What leaks in from the ambient environment?
- **Symptoms:** "works in dev, fails on fresh install / in CI"; "works on my machine
  but not after `npm ci`".
- **Real examples:** pinning internal deps to exact versions to stop fresh installs
  mixing incompatible packages; a flake build failing when a provider switched APIs;
  keeping every old release on update.
- **Design implication:** reproducibility is a feature. Build from clean, on target,
  with pins.

## Using the classes

**Retrospectively** (genie-read, genie-error): classify each artifact. After ~20,
the distribution tells you where a project's real difficulty lives.

**Prospectively** (genie-review): for each class, ask its detection questions of
the diff. Most findings fall out of asking two or three.

**In design** (genie-write, genie-design): for each class, either own the boundary
explicitly (validate, normalize, assign ownership) or declare that you do not and
fail loudly there.

## The tell

If you can describe a change without using the words *state*, *other*,
*concurrent*, *version*, *environment*, or *exit path*, it is probably easy — and
probably not where mastery is built.
