import sys
import csv
from tabulate import tabulate

# One command-line argument
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

# More than one command-line
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# Check file name and existence; ending .csv
file_name = sys.argv[1]


# Does not end with .csv
if not file_name.lower().endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

except FileNotFoundError:
        sys.exit("File does not exist")

if not rows:
        sys.exit()

headers = rows[0]
table = rows[1:]




# Outputs a table formatted as ASCII art using tabulate
print(tabulate(table, headers=headers, tablefmt="grid"))
