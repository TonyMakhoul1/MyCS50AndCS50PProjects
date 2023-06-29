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
try:
    month, day, year = date.split("/")
    if(month <= 12 and month >= 1) and (day <= 31 and day >= 1):
        break
except:
    try:
        lamonth, laday, layear = date.split("")
