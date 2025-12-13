import inflect


def main():


    p = inflect.engine()

    names = []


    # Prompts until the user inputs control-d
    while True:
        try:
            name = input()
            names += [name]
        except EOFError:
            break

    # Names with commas and "and"
    # Join Words into a List -> from inflect

    x = p.join(names)

    print(f"Adieu, adieu, to {x}")










if __name__ == "__main__":
    main()








