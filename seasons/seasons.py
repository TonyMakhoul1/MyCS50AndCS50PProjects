from datetime import date
import re
import sys

def main():
    birth_date = input("Date of Birth: ")
    check_birth(birth_date)


def check_birth(birth):
    birth = re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
    if birth:
        grps = birth.groups()
        print(grps)
    sys.exit(1)


if __name__ == "__main__":
    main()