def main():
    time = input("What time is it? ")
    time = convert(time)
    if time < 8.0 and time >= 7.0:
        print("breakfast time")
    if time < 13.0 and time >= 12.0:
        print("lunch time")
    if time < 19.0 and time >= 18.0:
        print("dinner time")



def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    new_minutes = minutes / 60
    return hours + new_minutes

if __name__ == "__main__":
    main()