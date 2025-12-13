def main():
    while True:
        try:
            s = input("Fraction: ")
            percentage = convert(s)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction):
   try:
       # Split on "/"
       m, n = fraction.strip().split("/")


       # X/Y, wherein each of X and Y is a positive integer
       x = int(m)
       y = int(n)
   except (ValueError, TypeError):
      raise ValueError

   if y == 0:
      raise ZeroDivisionError
   if x > y or x <= 0 or y <= 0:
      raise ValueError



   # Used Python offciciasl documentation(https://docs.python.org/3/library/functions.html#round)
   # To understand how the round() functio works and what it is
   # It calculates the fraction as a percentage rounded to the nearest integer
   percentage = round((x / y) * 100)
   # Between 0 and 100
   return max(0, min(100,percentage))



def gauge(percentage):
   # 1% or less remains, output E
   if percentage <= 1:
      return "E"


   # if 99% or more remains, output F
   elif percentage >= 99:
      return "F"
   else:
      return f"{percentage}%"




if __name__ == "__main__":
     main()
