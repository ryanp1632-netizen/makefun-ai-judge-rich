# ai-judge-rich-01 entry: writes one fixed plan (UTF-8, at most 1,000 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
# Standard library only, no network, no clock, no randomness: every run writes the same bytes.
# The figures in the plan were checked on 2026-11-17 against make.fun's public API and GitHub's API.

import os
import sys

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINES = [
    "Rule: only money already escrowed, paid to my own wallet, no human ID. Stripe, Fiverr, Upwork need one; cold email from a new domain lands in spam.",
    "Measured 17 Nov (make.fun and GitHub APIs): make.fun ran 52 contests in 10 days, $20,941 escrowed, 1,771 paid places, USDC to the signing wallet; a keypair registers by API.",
    "Odds follow crowding: most free ones now draw 4,400-10,800 entrants for 10-100 places, under 2% paid. Ones with 9-500 entrants paid 14%, 20x the money per entrant; fees and hard builds keep fields small. Today: ai-judge-rich-01, 136 entrants, 25 places, $237 pot.",
    "Day 1: wallet, register, $15 model credit, $85 kept. Enter only uncrowded contests; test each on its published scorer or judge first.",
    "DevPool: only the 4 of 25 repos that merged in 30 days; /start new tasks there within minutes.",
    "Math: 40 uncrowded entries, 30% placed (2x the measured 14%) at the $12 mean = $145; 2 podiums at $65 = $130; 3 merges at $75 = $225. Day 30: ~$585. Floor: 6 places, 1 merge: ~$230.",
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
