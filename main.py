"""Weirdest Job Title entry for make.fun.

Writes a single job title, 60 characters or fewer and nothing else,
to /output/entry.txt. The title is deterministic: the same bytes on
every run.
"""

import os

TITLE = "Senior Counter of Ceiling Tiles Above Dentists' Chairs"
# 54 characters: a real-sounding senior role with one gloriously
# specific twist — the ceiling tiles every patient stares at from
# the dentist's chair. Nothing else is written to the entry file.


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
