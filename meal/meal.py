def main():
    time = input("What time is it? ")
    time = convert(time)
    



def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    new_minutes = minutes / 60
    return hours + minutes

if __name__ == "__main__":
    main()