import sys
import csv




# Expects the user to provide two command-line arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

names = sys.argv[1]
output = sys.argv[2]

# the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house
students = []

try:
    with open(names, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                last, first = row["name"].split(", ")
                students.append({"first": first, "last": last, "house": row['house']})
            except ValueError:
                    sys.exit("Invalid name format")
except FileNotFoundError:
        sys.exit(f"Could not read {names}")


# the name of a new CSV to write as output, whose columns should be, in order, first, last, and house
# Converts that input to that output, splitting each name into a first name and last name.

with open(output, "w", newline='') as csvfile:
    student_info = ["first", "last", "house"]
    writer = csv.DictWriter(csvfile, fieldnames=student_info)
    writer.writeheader()
    writer.writerows(students)





