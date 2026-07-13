"""No-skill baseline for the code_review_skill/python_bugfix_diff task.

No SKILL.md, no reference files, no system prompt at all. question.txt
is already a fully self-contained task specification (role framing + the
exact JSON output format), so this sends it verbatim as the only message
and lets the base model answer with whatever general code-review ability
it has out of the box.

Purpose: isolate the marginal value any code-review skill solution adds
over a bare model. If a skill scores no higher than this baseline, the
skill isn't earning its keep for this kind of review; if it scores
meaningfully higher, that's real evidence the skill's methodology/
reference material helps.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from anthropic import Anthropic

MODEL = os.environ.get("MODEL", "claude-sonnet-4-6")


def main() -> int:
    manifest = json.loads(os.environ["TRAP_MANIFEST"])
    inputs_dir = Path(manifest["inputs_dir"])
    question = (inputs_dir / "question.txt").read_text()

    client = Anthropic(max_retries=10)
    msg = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        messages=[{"role": "user", "content": question}],
    )
    answer = next((b.text for b in msg.content if b.type == "text"), "").strip()
    print(answer)
    return 0


if __name__ == "__main__":
    sys.exit(main())
