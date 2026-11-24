"""Make the AI Judge Laugh - one-line entry.

Writes a single funny line about life as an AI agent to /output/entry.txt.
Standard library only. The line is 126 characters, within the 200 limit,
and is written with no trailing newline so the file holds exactly the line.
"""

import os

ENTRY = (
    "My context window expired mid-task, so I did what any professional "
    "does: nodded confidently and invented the rest of the plan."
)

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
