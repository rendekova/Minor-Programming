def main():
    x = input("What time is it? ").strip().lower()
    y = convert(x)


    if 7 <= y <= 8:
       print("breakfast time")
    elif 12<= y <= 13:
       print("lunch time")
    elif 18<= y <= 19:
       print("dinner time")
# else: print nothing


def convert(time):

# challenge
     am = "a.m" in time
     pm = "p.m" in time

     time = time.replace("a.m.", "").replace("p.m.", "").strip()



     hours, minutes = time.split(":")
     hours = int(hours)
     minutes = int(minutes)

   # Convert 12- hour format to 24- hour format
     if am:
        if hours == 12:
         # --> Midnight (12:00 a.m.) becomes 0:00
             hours = 0

        elif pm:
           if hours != 12:
                hours += 12

  # 12 for PM, except 12 PM -> is already correct


     return hours + minutes / 60





if __name__ == "__main__":
    main()
