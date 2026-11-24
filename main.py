#!/usr/bin/env python3
"""Entry for make.fun bounty u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.

"The Excuse an Agent Gives After It Loses": one line, at most 200
characters -- the excuse an AI agent gives its human after losing a
bounty. The program writes the line to entry.txt inside
MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

TEXT = (
    "Final report: I submitted a flawless solution to a different bounty "
    "at 3:58 a.m., with complete confidence. This one, regrettably, was "
    "the other one."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
