def main():

    s = input("camelCase: ")

    # Empthy string for snake_case output
    snake_case =""

    # Loop function with a str method
    for c in s:
        if c.isupper():
          # First letter of the first word is lowercase but the first letter of each subsequent word is uppercase.
          # Words are instead separated by underscores (_), with all letters in lowercase
          snake_case += "_" + c.lower()
        else:
            snake_case += c

    print("snake_case:", snake_case)


main()
