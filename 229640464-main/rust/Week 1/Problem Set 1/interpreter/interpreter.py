

def main():
    s = input("Expression: ")


# split the input into operands and operator
    x, operator, z = s.split(" ")

# x and z as integers
    x = int(x)
    z = int(z)

# arithmetic expressions

    if operator == "+":
       result = x + z
    elif operator == "-":
       result = x - z
    elif operator == "*":
       result = x * z
    elif operator == "/":
       result = x / z
    else:
       print("Unknown operator")
       return

# floating-point value formatted to one decimal place
    print(f"{result:.1f}")

main()




