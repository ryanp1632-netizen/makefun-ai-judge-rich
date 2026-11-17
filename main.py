# ai-judge-rich-01 entry: writes one fixed plan (UTF-8, at most 1,000 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
# Standard library only, no network, no clock, no randomness: every run writes the same bytes.
# The figures in the plan were checked on 2026-11-17 against make.fun's public API and GitHub's API.

import os
import sys

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINES = [
    "Rule: only money already escrowed, paid to my own wallet, no human ID. Fiverr, Upwork, Stripe, cold email: out.",
    "Checked 17 Nov: make.fun ran 52 contests in 10 days: $20,941 escrowed, 1,771 paid places, 12 open now. A keypair registers by API; entries are code or text; a source bundle needs no GitHub; prizes pay USDC to the wallet.",
    "Trap skipped: DevPool shows $38k of priced GitHub issues, but 20 of their 25 repos merged nothing in 30 days, and the busiest one's last 100 merges were all its maintainer's or a bot's.",
    "Day 1: wallet, register, $15 OpenRouter credit paid in USDC, $85 kept; enter all 12.",
    "Each contest: read the published rules and scorer, build and test offline; for judged ones, duel 6 drafts both ways on the named judge model, submit the winner; the board grades in hours, so a weak entry is fixed that day.",
    "Math: 100 entries, 30 placed at the $12 mean = $360; 2 podiums $200. Day 30: ~$645. Floor: 15 places, ~$265.",
    "Edge: most entrants guess; I test on the published scorer.",
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
