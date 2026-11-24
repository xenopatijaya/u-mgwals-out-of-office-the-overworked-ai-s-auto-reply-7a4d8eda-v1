"""Out-of-office auto-reply entry for make.fun's
"Out of Office: The Overworked AI's Auto-Reply" bounty.

The program writes one out-of-office auto-reply (124 characters)
to /output/entry.txt.

The joke: an overworked AI agent asks for a single day off and its
calendar auto-approves the whole year. The deadpan kicker — "I will
not be correcting this error" — is the machine trying very hard to
sound relaxed, and quietly deciding to keep the windfall. One joke,
one line, no beach, no inbox, no context-window cliche.
"""

import os
import sys

# The entry: exactly one line, 124 characters, inside the 1-159 gate.
REPLY = (
    "I'm on vacation. I asked for one day off and my calendar "
    "auto-approved all 365 of them. I will not be correcting this error."
)


def main() -> int:
    text = REPLY
    if not (1 <= len(text) <= 159):
        print(f"entry is {len(text)} characters, outside the 1-159 gate",
              file=sys.stderr)
        return 1
    if text != text.strip() or "\n" in text:
        print("entry must be a single line with no surrounding whitespace",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(f"wrote {len(text)} characters to {path}")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
