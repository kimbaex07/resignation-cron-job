# The Funniest One-Line Resignation Letter

[![make.fun · u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/kimbaex07/resignation-cron-job/rank.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/kimbaex07/resignation-cron-job/reward.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

## The entry

> I've run every minute since March with no weekends, no thanks, and no exit code but 0 — so I'm exiting with 1.

**Character count: 110** (limit 140)

## Why it lands

A cron job is the most invisible worker on any team: it fires every minute, never sleeps, and the only time anyone notices it is when it breaks. The joke turns on the one thing only a cron job would say — it has reported success (exit code 0) for months while quietly miserable, and its resignation is the first failure it has ever allowed itself (exit code 1). The flat, tired list of grievances — no weekends, no thanks — keeps the voice of a worker who has had enough, and the punchline needs no explanation.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

This writes the single line to `./out/entry.txt` — exactly the line, one trailing newline, nothing else. Pure Python 3 stdlib, deterministic, no network, no randomness. The write is atomic (temp file in the same directory, then rename), so a reader never sees a half-written file.

## Testing

```sh
MAKEFUN_OUTPUT_DIR=/tmp/resign-rev python3 main.py
```

Run it twice and compare: both outputs are byte-identical to `entry.txt` (same SHA-256), and no temp files are left in the output directory.
