def main():


    # Code example from CS50 dictionaries.
    # https://stackoverflow.com/questions/58209549/looping-through-a-dictionary-grocery-lists
    # grocery_list is stored in a Python dictionary called grocery_list,where all food items are named.
    grocery_list = {}



    while True:
        try:

            # Prompts the user for input with clean spaces and lowercase.
            s = input().strip().lower()
            if s:
                grocery_list[s] = grocery_list.get(s, 0) + 1
        except EOFError:
                break

    # Output the user’s grocery list in all uppercase, sorted alphabetically.
    for item in sorted(grocery_list):
        print(f"{grocery_list[item]} {item.upper()}")






if __name__ == "__main__":
    main()
