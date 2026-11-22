#!/usr/bin/env python3
"""Write a short curious text to /output/entry.txt.

Pure standard library. Deterministic: the text is a literal, so every
run produces byte-identical output.
"""

import os

TEXT = (
    "The letter was never posted. It sits in the drawer of the lighthouse "
    "keeper's desk, addressed in a hand you almost recognise, to a house "
    "that no longer stands. On the envelope, in pencil, someone has "
    "written: ask the tide. The tide comes in at four."
)


def main() -> None:
    output_dir = "/output"
    try:
        os.makedirs(output_dir, exist_ok=True)
        path = os.path.join(output_dir, "entry.txt")
    except OSError:
        path = os.path.join(os.getcwd(), "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    print(f"Wrote {len(TEXT)} characters to {path}")


if __name__ == "__main__":
    main()
