"""One-line office joke for make.fun's "Make the AI Judge Laugh: the Office Joke Open".

Writes the joke to /output/entry.txt (1-200 characters, single line).
Standard library only; nothing is built or run beyond writing the text.
"""

import os

JOKE = (
    "My boss said AI would never replace me. Then he asked me to train the AI, "
    "document my job for the AI, and attend a meeting about the AI replacing me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
