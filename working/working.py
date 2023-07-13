import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    clock = re.search(r"^([0-9]+)(:([0-9]+))? AM to ([0-9]+)(:([0-9]+))? PM$",s )
    if clock:
        groupes = clock.groups()
        print(groupes)





if __name__ == "__main__":
    main()