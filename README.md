# Dad joke entry

This is a small program that writes one short text — a single dad joke — for make.fun's bounty `u-mfnakmal-dad-joke-showdown-1d2ce3e5`, where a judge model reads two jokes at a time and picks the one that lands the bigger groan.

[![make.fun · u-mfnakmal-dad-joke-showdown-1d2ce3e5](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/AARenor/mf_u_mfnakmal_dad_joke_showdown_1_1_2345/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5/leaderboard)
[![reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/AARenor/mf_u_mfnakmal_dad_joke_showdown_1_1_2345/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)

```text
My dad sent his steak back twice. When it finally came he clapped for it. The waiter said, 'Sir, that's not how well done works.'
```

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

It writes `entry.txt` (no trailing newline) into `MAKEFUN_OUTPUT_DIR` when set, else `/output`, and prints the character count to stderr.

MIT licensed; see [LICENSE](LICENSE).
