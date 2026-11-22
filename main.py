"""Write the competition entry plan to /output/entry.txt.

No network, no dependencies: the plan text is a fixed string.
Output path defaults to /output/entry.txt; override with the
ENTRY_OUTPUT environment variable (used for local testing).
"""

import os

ENTRY = (
    "Day 1: list a $30 Fiverr gig: fix one slow Shopify page in 24h. "
    "Find buyers: Google 'site:myshopify.com', email 50 owners/day. "
    "Deliver 2 fixes/day, upsell $49/mo maintenance. "
    "$100 buys a domain and ads. Likely day 30: $450. "
    "Edge: owners already see their slow PageSpeed score."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= 280) or not text.strip():
        raise ValueError(f"entry must be 1-280 non-blank chars, got {len(text)}")
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
