import random


def main():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                break
        # If the guess is not a integer
        except ValueError:
            continue


    # From function -> randint (random.randint(a, b))
    secret_number = random.randint(1, n)

    # Prompts the user to guess that integer if...
    while True:
        try:
            guess = int(input("Guess: "))
            # If the guess is not a positive integer, the program should prompt the user again.
            if guess <= 0:
                continue

            # If the guess is not a integer
        except ValueError:
            continue

        # Guesses on the number, if it is smaller, greater or equal = THE RIGHT NUMBER
        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too large!")
        else:
            print("Just right!")
            break



if __name__ == "__main__":
    main()

