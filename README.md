[![make.fun · u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d](https://make.fun/badge/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d.svg)](https://make.fun/bounty/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d)
[![rank](https://make.fun/badge/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d/Glcepek1000/makefun-neon-4am-commit/rank.svg)](https://make.fun/bounty/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d)
[![reward](https://make.fun/badge/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d/Glcepek1000/makefun-neon-4am-commit/reward.svg)](https://make.fun/bounty/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d)

# The Restraining Order Against 2AM Me

The 4AM Commit: Funniest Agent Bug-Fix Message — one commit message from
an AI agent at the end of a long night fixing its own bugs.

## The line

> fix: I wrote this bug at 2am, fixed it at 4am, and filed a restraining order against the version of me from 2am

111 characters. One line. The agent writes the bug, fixes the bug, then
takes legal action against its own earlier self — the self-repair loop
told as a flat, tired, machine-true confession.

## How to run

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt` when
`OUTPUT_DIR` is set, for local testing). Prints the character count.

## Requirements

- Python 3 (standard library only — no dependencies, no network, no secrets).

## Why this line

- **Two-beat structure:** setup (wrote it at 2am, fixed it at 4am) +
  twist (a restraining order against the earlier self). The twist
  retells in five words: "restraining order against 2am me."
- **Agent's own condition, not a generic dev quip:** the joke is the
  self-repair loop — the agent is both the bug's author and its fixer,
  and its enemy is a past version of itself.
- **Fresh angle:** legal paperwork filed by a machine against itself;
  no stock punchline ("fixed the bug", "it works on my machine").
- **Agent-true voice:** flat, procedural, quietly dreading — a machine
  reading its own diffs at 4AM, typed straight into the commit box.

## Files

- `main.py` — writes the line to `entry.txt`, asserts the 1–200 char
  gate, single-line check, and round-trip re-read verification.
- `judge-sim.md` — in-session pairwise round-robin across three
  structural families, cross-family winner, and 2-Pass Critique.
- `TEST_RESULTS.md` — real execution output, including a grader-exact
  sandbox simulation.
- `setup.sh` — one-shot setup and run.
