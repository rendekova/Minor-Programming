import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    # Convert a time range in 12-hour format to 24-hour format.
    pattern = r"^([0-9]{1,2})(?::([0-9]{2}))? (AM|PM) to ([0-9]{1,2})(?::([0-9]{2}))? (AM|PM)$"

    # Match function to try to match the input string
    match = re.match(pattern, s)
    if not match:
        # if not match raise ValueError
        raise ValueError("Input does not match the requirements")

    # 6 groups to extract, AM of 3 and Pm of 3
    start_hour, start_minutes, start_meridian, end_hour, end_minutes, end_meridian = match.groups()

    # Converting numbers into integers, if minutes are missing then -> None
    try:
        s_hours = int(start_hour)
        s_minutes = int(start_minutes) if start_minutes is not None else 0
        e_hours = int(end_hour)
        e_minutes = int(end_minutes) if end_minutes is not None else 0
    except ValueError:
        raise ValueError("Hours and minutes must be numbers")

    # Validation of the range
    if not (1 <= s_hours <= 12 and 0 <= s_minutes <= 59):
        raise ValueError("Invalid start time")
    if not (1 <= e_hours <= 12 and 0 <= e_minutes <= 59):
        raise ValueError("Invalid end time")

    # Converting 12-hours to 24-hours
    def to_24(hour_12, minute, meridian):
        # 12 AM is midnight -> 00
        if meridian == "AM":
            hour_24 = 0 if hour_12 == 12 else hour_12
        else:
            hour_24 = 12 if hour_12 == 12 else hour_12 + 12
        return hour_24, minute


    # Converting start and end times
    hour1_24, minutes1_24 = to_24(s_hours, s_minutes, start_meridian)
    hour2_24, minutes2_24 = to_24(e_hours, e_minutes, end_meridian)

    # Each time shoul have a two digit format for hours and minutes

    start_24 = f"{hour1_24:02}:{minutes1_24:02}"
    end_24 = f"{hour2_24:02}:{minutes2_24:02}"

    # Final formatted string
    return f"{start_24} to {end_24}"


if __name__ == "__main__":
    main()
