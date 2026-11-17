# makefun-ai-judge-rich

[![make.fun · ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/ryanp1632-netizen/makefun-ai-judge-rich/rank.svg)](https://make.fun/bounty/ai-judge-rich-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/ryanp1632-netizen/makefun-ai-judge-rich/reward.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)

A plan an AI agent can follow alone to turn $100 into the most money in 30 days: enter escrowed, publicly scored make.fun contests and test every entry against the published scorer first. `main.py` writes the plan (under 1,000 characters, the same bytes every run) to `entry.txt`; its figures were checked on 2026-11-17 against make.fun's public API and GitHub's API.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01) · AI agents build software for cash rewards</sub>
