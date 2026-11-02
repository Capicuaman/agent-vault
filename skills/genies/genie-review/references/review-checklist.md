# Review Checklist by Boundary

Each pass has detection questions and red flags. You rarely need all seven; run
the ones the diff plausibly touches.

---

## 1. Environment

**Questions**

- What does this assume about the OS, shell, terminal, locale, or filesystem?
- What does it assume about the **working directory**?
- Which environment variables change its behavior? Are any of them ambient
  (`PATH`, `*_CONFIG_PATH`, `.env` files in the launch dir)?
- Does it read a file another tool wrote? What encoding will that tool use?
  (BOM, CRLF, UTF-16 on Windows?)
- Does it invoke a subprocess? Is that binary guaranteed present, and which
  version?
- Does it write to a path that may be a symlink, a mount, or read-only?

**Red flags**

- `process.env.X` with no validation and no default.
- `os.getcwd()` used to locate app resources.
- Parsing JSON/YAML/TOML without stripping a BOM.
- `spawn("bash")` / `subprocess.run(["sh", ...])` on a cross-platform codebase.
- String path concatenation instead of a path library.
- Sorting or comparing strings without specifying locale.

**Concrete scenario to ask about:** "What happens if the user runs this from `/`
or from a directory with a `package.json` that is not the project?"

---

## 2. Lifecycle / state

**Questions**

- What **new state** does this introduce? Where does it live?
- Who **releases** it, and on which exit paths — success, error, cancel, crash,
  SIGINT, timeout?
- Is teardown **symmetric** with setup? Is it idempotent?
- What happens if the setup runs twice (reload, reconnect, hot restart)?
- Does this survive session resume / process restart? Should it?
- Does it mutate global or module-level state that outlives the caller?

**Red flags**

- Registration without deregistration (`on(...)`, `addEventListener`,
  `setInterval`, `atexit`).
- `try { ... } finally` missing around a resource that needs release.
- A cache or registry with no invalidation function.
- State written to a module-level variable.
- A partial migration on error (half-written file, half-applied config).

**Concrete scenario:** "Kill the process mid-operation. What is left on disk or in
the terminal state?"

---

## 3. Concurrency

**Questions**

- How many of these can run at once? What enforces that?
- What happens **at the limit** — fail fast, queue, drop, or spawn more?
- Is there a **deadline** on waiting?
- What happens when one is **cancelled mid-flight**? Is it counted as alive
  until it actually exits?
- Is shared state accessed without a lock, or held across an `await`?
- Are results applied in completion order when they must be in submission order?
- Can two of these interleave to produce an invalid intermediate state?

**Red flags**

- `Promise.all` over a collection with an unbounded length.
- An unawaited promise whose rejection is unhandled.
- A mutex held across I/O.
- A counter of "active workers" decremented in a place that cancellation skips.
- A check-then-act sequence with an `await` in between.
- Retries without jitter or a cap.

**Concrete scenario:** "Run two of these simultaneously with the same input. Then
cancel one halfway."

---

## 4. Interface / contract

**Questions**

- Which external API, protocol, or provider does this depend on?
- What are its **undocumented limits** (payload size, rate, grammar size, tool
  count, concurrent streams)?
- What does it **cache**, and what invalidates that cache? Does this change
  invalidate it for everyone or just for the new path?
- Which errors are **transient** and which are permanent? Is the classification
  by cause or by message substring?
- Is the retry safe (idempotent)? What is the backoff and the cap?
- What does this do when the other side returns a shape you did not expect?
- Does this change a **contract** others implement? Who else must change?

**Red flags**

- `if (err.message.includes("timeout"))` — substring retry classification.
- A cache keyed without the dimension that actually varies.
- Assuming a response field is always present.
- Assuming a list is non-empty or ordered.
- Retrying a non-idempotent request.
- Adding a required field to a request type others construct.

**Concrete scenario:** "The provider returns a 200 with an empty body, or a 429
with `Retry-After: 0`. What happens?"

---

## 5. Input space

**Questions**

- What **classes** of input exist — not examples?
- Empty string? Whitespace-only? Only a newline? `\r\n`?
- Non-ASCII, CJK, RTL, combining marks, emoji?
- Very long? Very many? Deeply nested?
- Regex metacharacters, quotes, backslashes, `\u` escapes?
- Malformed JSON with a partial parse — does it run with partial data or fail?
- Is user text ever interpolated into a shell command, a regex, or a query?

**Red flags**

- `.split(" ")` or `.trim()` as the only normalization.
- A regex built from user input.
- `JSON.parse` inside a `try` that falls back to `{}`.
- Assuming a string is ASCII when measuring length or slicing.
- Rendering user text without escaping per output format.

**Concrete scenario:** "Feed it the empty string, then a string of only `\r\n`,
then a CJK string with punctuation."

---

## 6. Human / time

**Questions**

- Who depends on the behavior being changed? How many, and can you count them?
- What is their **migration path**, concretely — a command, a codemod, a doc?
- Is the change **backward compatible**? If not, is it marked breaking?
- How long is the **deprecation window**? Is there a warning before removal?
- Does this change a **default**? A default change is a breaking change with a
  larger blast radius than an API change.
- Can an old client and a new server coexist during rollout?
- What happens if the user upgrades and then **downgrades**?

**Red flags**

- Changing a default with no mention in the changelog.
- Removing a public symbol without a deprecation cycle.
- A schema or config change with no version bump.
- A migration that only runs forward.
- Assuming all clients update at once.

**Concrete scenario:** "A user on the previous version talks to the new version.
What breaks first?"

---

## 7. Reproducibility

**Questions**

- Does this work from a **clean checkout**, on the target platform, with `npm ci`
  / `pip install -r` / a fresh container?
- Are new dependencies **pinned**? Could two packages resolve to incompatible
  versions?
- Does the build depend on the **ambient environment** (a globally installed
  binary, an unpinned tool, a local cache)?
- Is the build **deterministic**? Same input, same artifact?
- Does CI exercise the same path the user will?
- Does the install path work on a machine with none of the dev tools?

**Red flags**

- `"latest"` or `"*"` in a dependency spec.
- Build scripts calling a tool assumed to be on `PATH`.
- Relying on a warm cache for correctness.
- Platform-specific code behind no test matrix.
- A release artifact that is not built from the tagged commit.

**Concrete scenario:** "Build in a fresh container with no cache and no globally
installed tools."

---

## The three shapes of bad fix

### Symptom patch
Suppresses the message without removing the condition.
- `catch { return null }`
- Raising a timeout instead of fixing the hang
- Filtering the warning out of the logs

**Ask:** "If I delete this line, what still fails — and is that failure the real
one?"

### New owned state
Adds a cache, flag, registry, or counter that now needs an invalidation rule.
- A memoized result with no invalidation
- A "seen" set that grows forever
- A global initialized once and read everywhere

**Ask:** "What invalidates this, and where is that written down?"

### Swallowed failure
Turns an error into a `null`, a retry, or a warning, moving the failure to a place
with less context.
- Retrying a permanent error until the timeout swallows the real cause
- Defaulting a missing value instead of reporting it
- Downgrading a hard failure to a log line

**Ask:** "When this genuinely fails, who finds out, and do they have enough
context to act?"

---

## Verification checklist

- [ ] A test fails before the change and passes after.
- [ ] The test covers the boundary that was actually crossed.
- [ ] There is a positive check (the operation succeeds), not just absence of error.
- [ ] Cancellation/timeout paths are exercised.
- [ ] The error path is exercised, not only the success path.
- [ ] The changelog entry names the symptom a user would search for.

## Writing the review

For each finding:

> **[Boundary]** — `<file>:<line>`: `<what the code does>`. If `<concrete
> scenario>`, then `<consequence>`. Was `<alternative>` considered, or is the
> guard owned elsewhere?

Lead with blocking findings. Say explicitly when the diff is fine. Never pad.
