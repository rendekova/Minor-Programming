import sys
import os
from PIL import Image, ImageOps

def main():

    # two command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Validation of th file or file extensions

    valid_extensions = [".jpg", ".jpeg", ".png"]

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    input_extensions = os.path.splitext(input_file)[1].lower()
    output_extensions = os.path.splitext(output_file)[1].lower()

    if input_extensions not in valid_extensions:
        sys.exit("Invalid input")

    if output_extensions not in valid_extensions:
        sys.exit("Invalid input")

    if input_extensions != output_extensions:
        sys.exit("Input and output have different extensions.")



    # Non existing file -> error
    try:
        image = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    # Shirt overlaying
    shirt = Image.open("shirt.png")
    size = shirt.size

    image = ImageOps.fit(image,size)
    image.paste(shirt, shirt)
    image.save(output_file)


if __name__ == "__main__":
    main()
