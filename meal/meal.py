def main():
    ...


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    if minutes == "60":
        hours = hours + 1
    

if __name__ == "__main__":
    main()