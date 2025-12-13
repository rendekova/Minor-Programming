import random


def main():
    level = get_level()

    score = 0

    for n in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct = x + y


        for attempt in range(3):
            try:
                output = int(input(f"{x} + {y} = "))
                if output == correct:
                    score += 1
                    break
                else:
                    print("EEE")

            except ValueError:
                print("EEE")
        else:
             print(f"The correct answer is {correct}")

        print(f" {score}")


def get_level():
    #  If the user does not input 1, 2, or 3, the program should prompt again.
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level


        except ValueError:
                pass


def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError("Level must be 1, 2, 3")


    lowest = 10 ** (level - 1)
    highest = (10 ** level) - 1

    if level == 1:
        lowest = 0
    return random.randint(lowest, highest)






if __name__ == "__main__":
    main()
