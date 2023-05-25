def main():
    time = input("What time is it? ")



def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    if minutes == "60":
        hours = hours + 1
        minutes = 0
    if hours == "7" and (minutes <= 59 or minutes >= 00):
        print("breakfast time")
    if hours == "8" and minutes == "00":
        print("breakfast time")
    if hours == "12" and (minutes <= 59 or minutes >= 00):
        print("lunch time")
    if hours == "13" and minutes == "00":
        print("lunch time")
    if hours == "18" and (minutes <= 59 or minutes >= 00):
        print("dinner time")
    if hours == "19" and minutes == "00":
        print("dinner time")
    

if __name__ == "__main__":
    main()