def main():
    fraction = input("Fraction: ")
    perc = convert(fraction)
    result = gauge(perc)
    print(result)


def convert(fraction):
    while True:
        try:
            x,y = fraction.split("/")
            x = int(x)
            y = int(y)
            f = x / y
            if f <= 1:
                z = int(f * 100)
                return z
            else:
                fraction = input("Fraction: ")
                pass
        except(ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()