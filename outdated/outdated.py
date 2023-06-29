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
date = input("Date: ")
while True:
    try:
        month, day, year = date.split("/")
        if(int(month) <= 12 and int(month) >= 1) and (int(day) <= 31 and int(day) >= 1):
            break
    except:
        try:
            lamonth, laday, layear = date.split(" ")
            for i in months:
                if lamonth == months[i]:
                    lamonth = i + 1
            laday = laday.replace(",", "")
            if(lamonth <= 12 and lamonth >= 1) and (laday <= 31 and laday >= 1):
                break
        except:
            print()
            pass

print(f{"year"-"month"-"day"})