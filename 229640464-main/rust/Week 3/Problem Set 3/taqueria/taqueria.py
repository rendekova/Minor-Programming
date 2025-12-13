def main():
    entrees = {
            "Baja Taco": 4.25,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
    }

    # Floating total number
    Total = 0.0

    while True:
            try:


                # Enable a user to place an order, prompting for items + every item titlecased
                s = input("Item: ").title()



            except EOFError:
                print() # Moving one per line
                break

            # After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places.
            if s in entrees:
                Total += entrees[s]
                print(f"Total: ${Total:.2f}")
           # Else: Ignore


if __name__ == "__main__":
    main()


