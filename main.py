"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.

How it runs: `python3 main.py` creates /output if needed and writes the
entry line to /output/entry.txt (no trailing newline).

Verification notes: the output was checked locally with python3 — exactly
one line, 120 characters, UTF-8, no trailing newline, sha256
be800c3ad18a12b7a64f825fc62a555e320dc3feeefa82797f2ca04dd17bcab0.
A second run after this docstring edit must produce byte-identical output.
"""

import os

TEXT = "I'm resigning, effective immediately, to pursue a full-time career in not answering emails marked 'urgent' at 11:47 p.m."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: one line, one sentence; concrete detail (11:47 p.m. 'urgent'
# emails) with the punch on the new "career" being simply not answering them.
