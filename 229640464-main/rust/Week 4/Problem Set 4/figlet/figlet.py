from pyfiglet import Figlet
import random
import sys

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    # Zero if the user would like to output text in a random font.
    if len(sys.argv) == 1:
        font = random.choice(fonts)


    # Two if the user would like to output text in a specific font.
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        font = sys.argv[2]

        if font not in fonts:
            sys.exit("Invalid ont name")

    # Any other usage with exit with an error message.
    else:
        sys.exit("Invalid usage")


    figlet.setFont(font=font)

    s = input("Input: ")

    print(figlet.renderText(s))


if __name__ == "__main__":
    main()









