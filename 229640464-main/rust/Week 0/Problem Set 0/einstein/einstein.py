# ask the user for mass as whole number (integer)
kilograms = input ("m: ")

# change input string into integer => type cast
kilograms = int(kilograms)

#calculate kilograms to Joules with a formula
joules = kilograms * pow(300000000, 2)

# print the value in Joules
output = "E: " + str(joules)
print(output)
