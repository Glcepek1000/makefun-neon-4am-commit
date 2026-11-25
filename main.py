#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message — the note an AI agent leaves after a long
night fixing its own bugs — to ``entry.txt`` in the output directory.

Standard library only. No network, no secrets, no input files.
"""

import os

LINE = (
    "fix: I wrote this bug at 2am, fixed it at 4am, "
    "and filed a restraining order against the version of me from 2am"
)

def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Gate self-check: one line, 1-200 chars, not only whitespace.
    assert 1 <= len(LINE) <= 200, f"line length {len(LINE)} out of range"
    assert LINE.strip(), "line is only whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)

    # Round-trip re-read verification: what we wrote is what the gate reads.
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    assert back == LINE, "round-trip mismatch"
    assert len(back.encode("utf-8")) == len(LINE.encode("utf-8"))

    print(f"wrote {path}: {len(LINE)} chars, {len(LINE.encode('utf-8'))} bytes")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
