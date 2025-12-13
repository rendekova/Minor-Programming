def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Convert $ amount from str to float (as decimal)
    x = float(d.replace("$",  ""))
    return x


def percent_to_float(p):
    # Convert % from str to float (as decimal)
    y = float(p.replace("%", "")) /100
    return y


main()
