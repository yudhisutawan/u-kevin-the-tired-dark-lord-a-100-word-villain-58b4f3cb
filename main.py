#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes the tournament-winning monologue (L4, necromancer mother) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Standard library only. Writes nothing to the repository directory.
"""

import os

ENTRY = (
    "Put that sword away before someone loses an eye. "
    "I have raised three thousand skeletons this century and not one of them "
    "stays buried past supper. They wander off. They lose their femurs. "
    "Last week one of them tried to unionize. "
    "I am not plotting the fall of your kingdom, boy \u2014 I am trying to get "
    "my children to bed. The grave-soil is damp, the shovels are rusted, and "
    "the high priest keeps sending me invoices for funerals I already "
    "performed. Go on. Slay me. Then explain to three thousand restless dead "
    "why their mother isn't coming home."
)

# Length guard: the monologue must stay within the 100-word limit.
assert len(ENTRY.split()) <= 100


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars ({len(ENTRY.split())} words) to {path}")


if __name__ == "__main__":
    main()
