"""Office joke entry for make.fun's "Make the AI Judge Laugh: the Office Joke Open".

Emits one single-line joke (149 characters) to /output/entry.txt.
The program uses only the Python standard library and performs no
network access, no file reads and no shelling out -- it just writes text.
"""

import os

# The joke, kept as three clauses that are joined at import time. The
# wording of each clause is fixed; joining them yields the exact entry.
_CLAUSES = (
    "My boss said AI would never replace me. ",
    "Then he asked me to train the AI, document my job for the AI, ",
    "and attend a meeting about the AI replacing me.",
)

JOKE = "".join(_CLAUSES)

ENTRY_PATH = "/output/entry.txt"


def write_entry(path, text):
    """Write *text* to *path*, creating the parent directory if needed."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def main():
    write_entry(ENTRY_PATH, JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
