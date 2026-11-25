#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes the tournament-winning loading-screen tip (v3, 40+ candidates
scored against the judge brief, knockout winner) to entry.txt.

The tip is a single line, 121 characters, aimed at stressed developers
and AI coding agents at once. Python standard library only.
"""

import os

TIP = (
    "Tip: step away from the keyboard. Your agent cannot fix the bug "
    "and your anxiety at the same time \u2014 and it chose the bug."
)


def main() -> None:
    # Gate check, mirroring the sealed scorer: UTF-8 text, 1-200 chars,
    # not whitespace-only. Fail loudly here rather than shipping invalid.
    if not (1 <= len(TIP) <= 200):
        raise SystemExit(f"tip is {len(TIP)} characters, must be 1-200")
    if not TIP.strip():
        raise SystemExit("tip is whitespace-only")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TIP)
    print(f"wrote {path}: {len(TIP)} characters, {len(TIP.encode('utf-8'))} bytes")


if __name__ == "__main__":
    main()
