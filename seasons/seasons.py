from datetime import date
import re
import sys

def main():
    birth_date = input("Date of Birth: ")
    try:
        year, month, day = check_birth(birth_date)
        print(year, month, day)

    except:
        sys.exit("Invalid Date")
    true_date = 

def check_birth(birth):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth):
        year, month, day = birth.split("-")
        return year, month, day


if __name__ == "__main__":
    main()