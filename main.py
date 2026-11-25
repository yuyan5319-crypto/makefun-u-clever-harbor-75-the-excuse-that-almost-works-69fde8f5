#!/usr/bin/env python3
"""Write the one-line excuse for GTA 6 launch week to /output/entry.txt.

The line has to read like a text a gamer fires off to the boss in a
hurry: one line, plain words, no setup, no signature. The angle is a
small, boring, specific household mishap with a gaming detail tucked
inside it -- a controller charger killing the power -- rather than any
of the classics (dead grandmother, flat tyre, sudden fever). Nothing
in it confesses to playing GTA; the manager is left with a flat full
of no electricity and an electrician due at noon.

The program writes exactly one line, no trailing blank lines, and is
fully deterministic: the same line every run, no network, no random
numbers, standard library only (the grading sandbox is Python 3.13
with nothing installed).
"""

import os

EXCUSE = (
    "sorry can't come in, my controller charger fried the power strip "
    "and tripped the whole flat, electrician's at noon"
)


def main():
    words = EXCUSE.split()
    if not 1 <= len(words) <= 20:
        raise SystemExit(f"excuse is {len(words)} words, must be 1-20")
    if not 1 <= len(EXCUSE) <= 140:
        raise SystemExit(f"excuse is {len(EXCUSE)} chars, must be 1-140")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.txt")
    with open(dest, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")
    print("wrote", dest, len(EXCUSE), "chars,", len(EXCUSE.split()), "words")


if __name__ == "__main__":
    main()
