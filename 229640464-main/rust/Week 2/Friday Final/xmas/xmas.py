def main():
    while True:
        try:
             s = int(input("How many lines? "))

             if s <= 0:
                print("Please enter a positive number.")
                continue


             # 5 lines, 1,3,5,7,9 (odd numbers) stars (multiples) with spaces.
             for i in range(s):
                 spaces = s - i - 1
                 stars = 2 * i + 1
                 lines = " " * spaces + "*" * stars
                 print(lines)


             break

        except ValueError:
             print("Thats not a valid number. Try again.")










if __name__ == "__main__":
    main()


