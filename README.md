# code-review-skill-baseline

No-skill baseline for [`python_bugfix_diff`](https://trapstreet.run/tasks/python-bugfix-diff).

The other 3 reference solutions (`code-review-skill-awesome`, `code-review-skill-jeffallan`,
`code-review-skill-alireza`) each embed a real community "code review" Claude Skill
(SKILL.md + its reference files) as the system prompt. This solution has **no
system prompt at all** — `question.txt` is already a self-contained task spec
(role framing + the exact required JSON output format), so this just sends it
verbatim to the model and prints whatever comes back.

**Purpose:** without this, comparing the 3 skills only tells you which skill is
*relatively* better — never whether any of them beat a model with zero
specialized guidance. This solution is the zero point every skill has to clear
to prove it's earning its keep.

Same model (`claude-opus-4-8`, set via `.env`) as the other 3, for a fair
comparison.
