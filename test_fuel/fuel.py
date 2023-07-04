def main():
    fraction = input("Fraction: ")
    perc = convert(fraction)
    result = gauge(perc)
    print(result)


def convert(fraction):
    try:
        f = fraction
        x,y = f.split("/")
        x = int(x)
        y = int(y)
    except ValueError:
        f = fraction
        x,y = f.split("/")
        x = int(x)
        y = int(y)

    except ZeroDivisionError:
        f = fraction
        x,y = f.split("/")
        x = int(x)
        y = int(y)
    else:
        if x == 0:
            return 0
        elif x < y or x == y:
            z = (x / y) * 100
            z = round(z)
            '''if z <= 1:
                print("E")
            elif z >= 99:
                print("F")
            else:
                print(z,end ="%")
                print()'''
        elif x > y:
            f = fraction
            x,y = f.split("/")
            x = int(x)
            y = int(y)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()