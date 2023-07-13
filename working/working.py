import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    clock = re.search(r"^([0-9]+)(:([0-9]+))? AM to ([0-9]+)(:([0-9]+))? PM$",s )
    if clock:
        groupes = clock.groups()
        print(groupes)


def not_am_pm(hour, minute, apm):
    if apm == "PM":
        if int(hour) == 12:
            new_hour == 12
        else:
            new_hour == int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour == 0
        else:
            new_hour == int(hour)
    if minute == None:
        new_minute = ":00"
        time = f"{new_hour:02}" + new_minute
    else:
        time = f"{new_hour:02}" + " : " + minute
    return time

if __name__ == "__main__":
    main()