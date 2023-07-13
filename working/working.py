import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    clock = re.search(r"^([0-9]+)(:([0-9]+))? (AM|PM) to ([0-9]+)(:([0-9]+))? (AM|PM)$",s )
    if clock:
        groupes = clock.groups()
        if int(groupes[0]) > 12 or int(groupes[4]) > 12:
            raise ValueError
        if int(groupes[2]) >= 60 or int(groupes[6]) >= 60:
            raise ValueError
        time_one = not_am_pm(groupes[0], groupes[2], groupes[3])
        time_two = not_am_pm(groupes[4], groupes[6], groupes[7])
        return time_one + " to " + time_two
    else:
        raise ValueError

def not_am_pm(hour, minute, apm):
    if apm == "PM":
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)
    if minute == None:
        new_minute = ":00"
        time = f"{new_hour:02}" + new_minute
    else:
        time = f"{new_hour:02}" + ":" + minute
    return time

if __name__ == "__main__":
    main()