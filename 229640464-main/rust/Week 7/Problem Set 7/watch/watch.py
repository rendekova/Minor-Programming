import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    """
    Extracts any YouTube URL that’s the value of a src attribute of an iframe element therein, and returns its shorter, shareable youtu.be equivalent as a str.
    """

    # Pattern breakdown and code with functions
    pattern = r'<iframe[^>]*\s+src="https?://(?:www\.)?youtube\.com/embed/([A-Za-z0-9_-]+)"'

    # Match function
    match = re.search(pattern, s)
    if not match:
        return None

    video = match.group(1)
    return f"https://youtu.be/{video}"




if __name__ == "__main__":
    main()
