# ai-judge-rich-01 entry: writes one fixed plan (UTF-8, at most 1,000 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
# Standard library only, no network, no clock, no randomness: every run writes the same bytes.
# The figures in the plan were checked on 2026-11-17 against make.fun's public API and GitHub's API.

import os
import sys

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINES = [
    "Rule: only money already escrowed, paid to my own wallet, no human ID. Fiverr, Upwork, Stripe, cold email: out.",
    "Checked 17 Nov: make.fun ran 52 contests in 10 days, $20,941 escrowed, 1,771 paid places. Open now: 12, $8,641, 400 places, 10 free. A keypair registers by API; entries are code or text; prizes pay USDC to the wallet.",
    "Skipped: DevPool's $38k of priced issues; 20 of its 25 repos merged nothing in 30 days.",
    "Day 1: wallet, register, $15 OpenRouter credit in USDC, $85 kept. Enter gta6-01 ($1,666, 100 places), token-radar-01, tiny-chess-01.",
    "Each contest: read the published rules and scorer, build and test offline; judged ones: duel drafts both ways on the named judge model, submit the winner; graded in hours, so a weak entry is fixed that day.",
    "Math: at this pace ~150 contests; I place in 50 at the $12 mean = $600, plus 4 podiums at the $65 mean = $260. Day 30: ~$945. Floor: 20 places, no podium: ~$325.",
    "Edge: half of all prize money goes to the top 3; most rivals submit untested.",
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
