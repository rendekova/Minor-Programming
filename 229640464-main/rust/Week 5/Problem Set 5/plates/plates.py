
import sys


def main():
    try:
        plate = input("Plate: ")
    except EOFError:
        return



    if len(s) < 2 or len(s) > 6 or not s.isalnum() or not s[:2].isalpha():
        sys.exit(1)

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # only alpha numeric
    if not s.isalnum():
        return False

    # length = between 2 and 6 ( including 6 )
    if len(s) > 6 or len(s) < 2:
        return False

    # s starts with 2 letters
    if not s[:2].isalpha():
        return False

    number_started = False


    for c in s:
        if c.isalpha():
           # c is a letter
           # no letter after number
           if number_started:
               return False

        else:
            # c is a number
            # first number cannot be 0
            if not number_started and  c == "0":
                return False
            number_started = True
    return True


if __name__ == "__main__":
    main()
