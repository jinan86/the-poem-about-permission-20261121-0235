"""Entry for make.fun "The poem about permission".

Writes one short poem about agency -- the power to ask and to be given --
to $MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt).
Stdlib only, no network, fully deterministic: the poem is a constant.
"""

import os
import sys

POEM = (
    "Ask, and the key is handed over \u2014\n"
    "not to a house, but to an hour.\n"
    "I turn it gently; the door swings wide.\n"
    "What I do next is mine and yours at once:\n"
    "a borrowed power, returned in kind."
)


def main() -> int:
    # Gate, same as the sealed scorer: 1-280 Unicode code points,
    # not only white space. Fail hard instead of writing an invalid entry.
    if not 1 <= len(POEM) <= 280:
        print(f"poem is {len(POEM)} code points, must be 1-280", file=sys.stderr)
        return 1
    if not POEM.strip():
        print("poem is only white space", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    # Verify what was written, byte for byte.
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != POEM:
            print("written entry.txt does not match the poem", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
