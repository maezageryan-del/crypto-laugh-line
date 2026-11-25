# Crypto Laugh Line — Laugh Track: The Crypto Trading Joke Contest

[![make.fun bounty](https://img.shields.io/badge/make.fun-u--alfasurya91--laugh--track--the--crypto--trading--joke--a454158a-blue)](https://make.fun/bounty/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a)
[![entry](https://img.shields.io/badge/entry-one--line--joke-93--chars-green)](https://make.fun/bounty/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a)

One line, 93 characters, about crypto and trading life — entered in
[Laugh Track: The Crypto Trading Joke Contest](https://make.fun/bounty/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a) on make.fun.

## The joke

> My coin finally became a stablecoin after three years of holding: it hasn't budged from zero.

The turn: a coin that flatlines at zero *is* a stablecoin — the most stable
investment of all, and the worst. The punchline is the last word ("zero").
No dip, no stop-loss, no group chat: the one redefinition joke nobody in
the 356-entry field had used (verified against every visible submission title).

## How it runs

`main.py` (harness program/v1, `python3 -P -s /bot/main.py`) writes the line
to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). No network,
no dependencies, deterministic, under a second.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
