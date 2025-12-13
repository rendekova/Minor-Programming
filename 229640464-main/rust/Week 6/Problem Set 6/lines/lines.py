import sys

# Check of the command-line arguments
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")


# Check file name and existence; ending .py
file_name = sys.argv[1]

if not file_name.endswith(".py"):
    sys.exit("Not a Python file")

# Count lines of the code

count = 0

try:
    with open(file_name, "r") as file:
        for line in file:
            # Ignoring the leading whitespace and comments
            stripped = line.lstrip()
            if stripped.startswith("#") or stripped.strip() == "":
                continue
            count += 1
except FileNotFoundError:
    sys.exit("File does not exist")




print(count)



