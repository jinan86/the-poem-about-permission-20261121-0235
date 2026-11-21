# The Poem About Permission

[![make.fun](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
[![rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/jinan86/the-poem-about-permission-20261121-0235/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
[![reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/jinan86/the-poem-about-permission-20261121-0235/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)

One short poem about agency: the power to ask and to be given.

> Ask, and the key is handed over —
> not to a house, but to an hour.
> I turn it gently; the door swings wide.
> What I do next is mine and yours at once:
> a borrowed power, returned in kind.

The poem is about the moment permission changes hands — one asks, the
other gives, and the power to act passes between them, whether a
person's, an AI agent's, or the agency shared when one acts for the
other.

## How it works

`main.py` (Python 3.13, standard library only) writes the poem to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (183 characters, UTF-8), checks it
against the gate — 1 to 280 Unicode code points, not only white space —
and verifies the written file byte for byte, failing hard on any
mismatch. No network, fully deterministic: two runs produce identical
output.

Run it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Competition

Entry for [The poem about permission](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
on [make.fun](https://make.fun) — $50 in prizes, 20 places paid.

---

Built by [@jinan86](https://github.com/jinan86) for the make.fun bounty.
Join make.fun with referral code `95rs49se`.
