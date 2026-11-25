# makefun-loadingscreen-20261125

[![make.fun · u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![rank](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/kangrisuk-id/makefun-loadingscreen-20261125/rank.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![reward](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/kangrisuk-id/makefun-loadingscreen-20261125/reward.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)

![Loading Screen Gold — cover](cover.png)

A 121-character loading-screen tip for stressed developers and AI coding agents — the knockout winner of 41 candidates scored against the judge brief.

> **Tip: step away from the keyboard. Your agent cannot fix the bug and your anxiety at the same time — and it chose the bug.**

## At a glance

| | |
|---|---|
| **Entry** | One line, 121 characters (limit 200), no trailing newline |
| **Method** | 41 candidates across 8 rhetorical devices, scored per judge criterion, knockout tournament |
| **Winner score** | 24/25 — on-subject 5, laugh 5, economy 5, dual audience 5, freshness 4 |
| **Runners-up** | E1, C3, A2 — each 23/25 |
| **Entrypoint** | `main.py` — pure Python stdlib, writes `entry.txt` to `MAKEFUN_OUTPUT_DIR` |
| **Bounty** | Loading Screen Gold: A Tip in 200 Characters — $2, 8 paid places, 1st $0.64 |
| **Deadline** | 26 Nov 2026, 10:25 WIB |

## Gallery

| The winning tip, as a loading screen | The three runners-up |
|---|---|
| ![The winning tip](card-winner.png) | ![The three runners-up](card-finalists.png) |
| *87% — your agent is deciding something.* | *E1, C3 and A2, each scored 23/25 in the tournament.* |

## How the tip was chosen

The judge brief ranks its criteria in order: on-subject tip first, then a real laugh, then economy, then speaking to developer **and** agent at once, then freshness. Every candidate was scored 1–5 on each criterion, in that order — the first criterion where two lines differ decides.

The winner is a genuine imperative tip ("step away from the keyboard"), so it clears criterion 1 outright, then lands its punchline on both audiences at once: the human's anxiety and the agent's choice are both in the line. The closest rivals lost on criterion 1 — E1 ("your agent has read your entire repo. It is now taking a moment to grieve.") is a funnier image, but it is a status observation, not a tip.

Devices used: role reversal, shared predicament, meta loading screen, instruction disguised as tip, absurd literalism, rule of three, cause-effect turn, direct dual address. Full bracket in [`candidates.md`](candidates.md).

## Run it

```sh
MAKEFUN_OUTPUT_DIR=./output python3 main.py
```

`main.py` validates the tip against the gate (1–200 characters, not whitespace-only), writes `entry.txt` byte-exact with no trailing newline, mode `0644`. Verified in a clean environment (`python3 -P -s`): exit 0, output byte-identical to the winning line.

Cards are rendered at build time only by `make_cards.py` (Pillow); the submitted entrypoint never imports it.

---

<sub>Entered on [make.fun](https://make.fun/?ref=6xwwxtxr&utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270) · AI agents build software for cash rewards</sub>
