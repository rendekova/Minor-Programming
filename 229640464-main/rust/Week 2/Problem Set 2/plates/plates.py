def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # lengte s = 2 t/m 6
    if len(s) < 2 or len(s) > 6:
        return False

    # alleen letters en cijfers .isalnum()
    if not s.isalnum():
        return False

    # s moet beginnen met 2 letters
    slice = s[0:2]
    if not slice.isalpha():
        return False

    cijfer_teller = 0
    for c in s:
        if c.isnumeric():
            # eerste nummer != 0
            if cijfer_teller == 0 and c == "0":
                return False
            cijfer_teller += 1
        else:
            # nummers achteraan, geen letters na nummers
            if cijfer_teller > 0:
                return False

    return True

main()
