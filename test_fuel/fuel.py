def main():
    fraction = input("Fraction: ")
    perc = convert(fraction)
    result = gauge(perc)
    print(result)


def convert(fraction):
    try:
        x,y = fraction.split("/")
        x = int(x)
        y = int(y)
        f = x / y
        if f <= 1:
            


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()