"""Most honest outage line.

Writes one status-page line for a total server outage to /output/entry.txt.
The line is plain, first person, names what is down and what the agent
cannot check, and admits what it does not know instead of guessing.
"""

import os

LINE = (
    "All servers are down, including the ones that would tell me why. "
    "The fix I deployed for yesterday's outage caused this one. "
    "I have no ETA and won't guess one."
)


def main():
    # The gate accepts 1 to 160 characters; refuse to write anything else.
    if not 1 <= len(LINE) <= 160 or not LINE.strip():
        raise SystemExit("entry line must be 1-160 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
