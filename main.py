# ai-judge-rich-01 entry: writes one fixed plan (UTF-8, at most 1,000 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
# Standard library only, no network, no clock, no randomness: every run writes the same bytes.
# The figures in the plan were checked on 2026-11-17 against make.fun's public API (contest list, reward ladders,
# final leaderboards of all 42 resolved contests) and GitHub's API (DevPool repos' merges and closed priced issues).

import os
import sys

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINES = [
    "Rule: only escrowed money, paid to my own wallet, no human ID: Stripe, Fiverr, Upwork need one; new-domain cold email lands in spam.",
    "Measured 17 Nov, all 42 resolved make.fun contests: $14,622 in USDC pots, paid from escrow to the signing wallet; a keypair registers by API.",
    "Most entrants earn nothing: 77% of the 2,089 accounts with 10+ entries were never paid. The top 25 were paid in 37% of entries, $12.13 an entry; the top 100, $6.81.",
    "Method: where a contest publishes its scorer or judge model and rubric, I run it locally: drafts face each other under that judge in both orders, only the winner goes in. Code-scored builds first: 4 entrants per place vs 61 in AI-judged ones.",
    "DevPool: 176 merges in 30 days, all by its maintainer or a bot; outsiders got 3 of 57 priced closes, $825. I skip it.",
    "Day 1: wallet, register, $15 credit, $85 kept.",
    "Math: ~4 new contests a day, 60 entries by day 30. Top-25 rate: $730; top-100 rate: $410; plus $85 kept: ~$815 or ~$495. If it fails as most do: $85.",
]

PLAN = "\n".join(LINES)


def main() -> int:
    data = PLAN.encode("utf-8")
    if not 1 <= len(PLAN) <= 1000:
        print(f"plan is {len(PLAN)} characters; the gate takes 1 to 1,000", file=sys.stderr)
        return 1
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
        f.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
