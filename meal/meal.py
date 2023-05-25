def main():
    time = input("What time is it? ")
    time = convert(time)
    if time < 8.0 and time >= 7.0:
        print("")



def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    new_minutes = minutes / 60
    return hours + minutes

if __name__ == "__main__":
    main()