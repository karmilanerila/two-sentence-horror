"""Two-Sentence Horror — writes one original two-sentence horror story.

The story is fixed text: deterministic, no randomness, no network.
It writes to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt)
with mode 0644 so the grader (uid 65534) can read it.
"""

import os
import stat

# Exactly two sentences, well under the 400-character limit.
STORY = (
    "Every night before bed I count the chairs in my kitchen: "
    "four, always four, because I live alone. "
    "Tonight there were five, and the fifth was pulled out, "
    "as if someone had only just stood up from it."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(STORY.encode("utf-8"))
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
