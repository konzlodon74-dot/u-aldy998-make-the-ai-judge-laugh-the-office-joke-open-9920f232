#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open.

Writes one original line of office comedy to /output/entry.txt.
Standard library only, deterministic.
"""

import os

# The joke, composed here: a meeting called to decide whether the
# meeting could have been an email -- and the punchline is that the
# minutes were emailed to the people who skipped it. Specific office
# detail, a turn that pays off in the last few words, nothing explained.
JOKE = (
    "We held a meeting to decide whether the meeting could have been "
    "an email \u2014 the minutes were emailed to everyone who skipped it."
)


def main() -> None:
    # The gate requires 1 to 200 characters of non-whitespace text.
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars"
    assert "\n" not in JOKE and JOKE == JOKE.strip(), \
        "joke must be exactly one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(JOKE)


if __name__ == "__main__":
    main()
