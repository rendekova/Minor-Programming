def get_height(min_height=1, max_height=8):
    while True:
        try:
            height = int(input(f"Enter a height ({min_height}-{max_height}): "))
            if min_height <= height <= max_height:
                return height
            else:
                print(f"Height must be a number between {min_height} and {max_height}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def draw_pyramid(height):
    for i in range(1, height + 1):
        spaces = height - i
        blocks = i
        line = f"{' ' * spaces}{'#' * blocks}  {'#' * blocks}"
        print(line)


def main():
    height = get_height()
    draw_pyramid(height)


if __name__ == "__main__":
    main()