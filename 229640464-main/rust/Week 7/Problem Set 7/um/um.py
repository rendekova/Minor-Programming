import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # Count the number of times that “um” appears in that text, case-insensitively.
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()
