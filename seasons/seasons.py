from datetime import date
import re
import sys
import inflect

def main():
    birth_date = input("Date of Birth: ")
    try:
        year, month, day = check_birth(birth_date)

    except:
        sys.exit("Invalid Date")
    true_date = date(int(year), int(month), int(day))
    today_date = date.today()
    minus = today_date - true_date
    minutes = minus.days * 24 * 60
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")
    print(words)

def check_birth(birth):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth):
        year, month, day = birth.split("-")
        return year, month, day


if __name__ == "__main__":
    main()