# baseline-no-skill

No-skill baseline for [`python_bugfix_diff`](https://trapstreet.run/tasks/python-bugfix-diff).

This solution has **no system prompt at all** — `question.txt` is already a
self-contained task spec (role framing + the exact required JSON output
format), so this just sends it verbatim to the model and prints whatever
comes back. No SKILL.md, no reference files, no tool calls.

**Purpose:** any code-review skill solution submitted against this task should
be compared against this floor. If a skill doesn't score meaningfully higher
than this, it isn't earning its keep — it's just a differently-worded prompt
around a model that would've done the same thing anyway.

Model is set via `.env` (`MODEL=claude-opus-4-8` by default) — match it to
whatever you're comparing against.
