#!/usr/bin/env python3
"""Office joke entry for make.fun.

Writes one single-line joke about office life to /output/entry.txt.
The gate requires UTF-8 text of 1 to 199 characters, not only whitespace.
No network, no input files, no model calls: the joke is a constant.
"""

import os
import sys

JOKE = (
    "I marked myself 'in a meeting' so I could eat lunch in peace, "
    "and now that meeting has a weekly invite and three attendees."
)


def main() -> int:
    text = JOKE.strip()
    if not text:
        print("refusing: joke is blank", file=sys.stderr)
        return 1
    if len(text) > 199:
        print(f"refusing: joke is {len(text)} chars, gate allows at most 199",
              file=sys.stderr)
        return 1
    if "\n" in text:
        print("refusing: joke must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text + "\n":
        print("refusing: entry.txt does not match the joke", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
