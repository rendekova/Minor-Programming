def main():

    months = [

         "January",
         "February",
         "March",
         "April",
         "May",
         "June",
         "July",
         "August",
         "September",
         "October",
         "November",
         "December"
      ]
    while True:
        try:
            s = input("Date: ").strip()


            # Month-day-year format as digits: MM/DD/YYYY using slashes.
            if "/" in s:
                month, day, year = s.split("/")
                month = int(month)
                day = int(day)
                year = int(year)

                # Normal range of a day and month - 9/8/1636.
                if 1 <= month <= 12 and 1 <= day <= 31:
                    # Year has 4 digits, months and days 2.
                    print(f"{year:04}-{month:02}-{day:02}")
                    break

            # Month-day-year format as Month D, YYYY - September 8, 1636.
            elif "," in s:
                x = s.split()
                month1 = x[0]
                day = int(x[1].replace(",", ""))
                year = int(x[2])

                # Assume that every month has no more than 31 days.
                if month1 in months and 1 <= day <= 31:
                    month = months.index(month1) + 1
                    print(f"{year:04}-{month:02}-{day:02}")
                    break

        except (ValueError, IndexError):
            pass




if __name__ == "__main__":
    main()


