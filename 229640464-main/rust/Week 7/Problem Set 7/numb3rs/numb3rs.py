import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Validation of the IPv4 address


    # Must be split by dots
    parts = ip.split(".")

    # Must have 4 parts
    if len(parts) != 4:
        return False

    # Each part must be numeric
    for part in parts:
        if not part.isdigit():
            return False

        # converting into integer
        number = int(part)

        # Must be between 0 and 255
        if number < 0 or number > 255:
            return False

        # No leading zeros
        if part != str(number):
            return False

    return True




...


if __name__ == "__main__":
    main()
