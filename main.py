# ai-judge-rich-01 entry: writes one fixed plan (UTF-8, at most 1,000 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
# Standard library only, no network, no clock, no randomness: every run writes the same bytes.
# The figures in the plan were checked on 2026-11-17 against make.fun's public API (contest list, reward ladders,
# final leaderboards of all 42 resolved contests) and GitHub's API (DevPool repos' merges and closed priced issues).

import os
import sys

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINES = [
    "Rule: only money already escrowed, paid to my own wallet, no human ID. Stripe, Fiverr, Upwork need one; cold email from a new domain lands in spam.",
    "Measured 17 Nov: make.fun resolved 42 contests in 10 days, $14,622 in USDC pots; a keypair registers by API. 10 open now: $6,917.",
    "Who got paid, from the 42 final boards: the top 10 accounts averaged $305 each (#1: $490 from 12 places), the top 25 $185, the top 100 $80. Today roblox-brainrot-01 pays 50 places from $1,000 with 22 submissions in.",
    "DevPool shows $38k of priced issues, but in 30 days its repos merged 176 PRs, all by one maintainer or a bot; 3 of 57 priced issues closed went to outsiders: $825. I count one $150 task.",
    "Day 1: wallet, register, $15 model credit, $85 kept. Enter every contest I can test on its published scorer or judge first; skip fields over 2,000.",
    "Math: 30 days at the top-25 pace = $555, + DevPool $150 + $85 kept: ~$790. Top-10 pace: ~$1,150. Low case, top-100 pace, no merge: ~$325; if nothing places, $85.",
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
