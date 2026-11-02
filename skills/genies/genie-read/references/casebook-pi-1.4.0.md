# Casebook: pi 1.4.0 (released 2026-10-21)

A worked example. Every interesting fix from one real release, classified by the
boundary it crossed. Use it as a model for building your own casebooks.

Source: `CHANGELOG.md` of `@earendil-works/pi-coding-agent`, sections `[1.4.0]`,
`[1.3.0]`, `[1.2.0]`.

## The reframe

None of the interesting fixes are algorithmic. They are collisions with boundaries
the authors did not control — environment, lifecycle, concurrency, interfaces,
input space, time, reproducibility.

## Classified fixes

### Environment
- `pi update` failed on `managed-install.json` when PowerShell 5.1 had added a
  UTF-8 BOM.
- `mcp.json` files with a UTF-8 BOM failed to parse, silently skipping all MCP
  servers and breaking `pi mcp add/remove`.
- `grep` tool honored `RIPGREP_CONFIG_PATH`, where `--fixed-strings` silently
  turned regex searches literal → now runs `rg --no-config`.
- Standalone binaries loaded `.env*` from the launch directory (1.1.0).
- Nix package put its Node first on `PATH`, so the bash tool used pi's Node
  instead of the user's (1.3.0).
- Symlinked `AGENTS.md` in a nested git worktree loaded no project context (1.2.0).
- Windows shell detection: Microsoft Store aliases; PowerShell outside `PATH`;
  legacy WSL `bash.exe` when Windows isn't in `C:\Windows`.

### Lifecycle / state
- Terminal left in mouse-tracking, focus-reporting, Kitty keyboard, and alt-screen
  modes when pi exited without normal teardown.
- Background `wl-copy`/`xclip`/`xsel` suspended with pi on Ctrl+Z, hanging pasting.
- Resumed sessions / `/tree` navigation leaving extension tools inactive.
- Sessions broken after recovering from an output-limit cutoff: truncated tool
  call dropped but its results kept → every later request rejected.

### Concurrency
- Codemode scripts failed immediately when both workers were busy → now wait up to
  60s; `PI_CODEMODE_MAX_WORKERS` raises the limit.
- Concurrent extension dialogs: a second replaced the first and the first promise
  never settled.
- (1.3.0) Repeated timeouts/aborts accumulating surviving workers; admission now
  limits live workers, counting cancelled ones until actual exit.

### Interface / contract
- OpenAI prompt cache lost on every deferred tool load after a tool was removed.
- GitHub Copilot large bodies (many images) → HTTP 413 instead of compacting+retrying.
- Automatic retry not triggering for more gateway upstream failures, Codex proxy
  `stream disconnected`, transient Vertex OAuth refresh; retrying on digits in
  request IDs or byte counts.
- (1.3.0) Anthropic/Bedrock 400 when an error tool result contains images.
- (1.2.0) Anthropic strict tool set rejected for grammar/tool-count/union limits →
  retry once non-strict.

### Input space
- Whitespace-only tool output (bare `\r\n`) → 400 on OpenAI Completions/Responses
  and Google.
- CJK punctuation breaking Markdown bold/italic; unclosed `$$` math swallowing
  later tables.
- Tool-call args with an invalid `\u` escape (e.g. `\usepackage`) dropping fields (1.3.0).
- `@` file autocomplete failing on regex metacharacters `[` `(`.

### Human / time
- (1.2.0) Breaking changes: published schema URLs; `before_agent_start` became a
  union; session counted busy during startup.
- (1.1.0) `--tools +name/-name` semantics; `outputPad` scope change.
- Retired default models (Copilot `gpt-5.4` → `gpt-6.1-sol`).

### Reproducibility
- (1.3.0) Pinned internal deps to exact versions to stop fresh installs mixing
  incompatible packages.
- (1.3.0) Nix flake build failing when a provider switched APIs; catalog pin refresh.
- (1.1.0) Managed installs kept every old release; `pi update` now keeps two.

### Failure semantics (a sub-theme worth its own casebook)
- Compaction/branch summaries failing "generation hit the token cap" when reasoning
  consumed the fixed output limit → use the model's output limit.
- `/compact <instructions>` ignored when the split turn was the only new content.
- Retry classification by cause, not substring.

## Lessons to carry forward

1. **Most "hard" is boundary.** Environment, lifecycle, concurrency, interface.
2. **The smallest diffs often fix the worst bugs** (`--no-config`, strip BOM,
   restore terminal on exit). Complexity is not where you think.
3. **Silent failures are the worst class** — a BOM skipping all MCP servers, config
   changing grep semantics. Fail loudly at boundaries.
4. **Caches and derived state are a tax** paid forever in consistency bugs.
5. **Time is a boundary.** Interfaces must be designed with their change path.
6. **Reproducibility is a feature**, invisible until a fresh install breaks.

## How to build your own casebook

Pick one release. Copy every *Fixed* entry. Classify each by boundary. Write one
reusable lesson per fix, stripped of project nouns. After a few releases, compare
the distributions — you will find where that project's real difficulty lives, and
you will start recognizing the same shapes in your own code.
