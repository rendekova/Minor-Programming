from datetime import date
import sys
import inflect

engine = inflect.engine()

def main():
    birth = input("Date of Birth: ")
    try:
        birth_date = date.fromisoformat(birth)
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()
    minutes = min_lived(birth_date, today)
    words = engine.number_to_words(minutes, andword="").capitalize()
    print(f"{words} minutes")

def min_lived(birth_date,today):
    difference = today - birth_date
    return round(difference.days * 24 * 60)


if __name__ == "__main__":
    main()
