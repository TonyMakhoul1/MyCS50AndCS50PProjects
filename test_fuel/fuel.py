def main():
    ...


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
            print("E")
        elif x < y or x == y:
            z = (x / y) * 100
            z = round(z)
            if z <= 1:
                print("E")
            elif z >= 99:
                print("F")
            else:
                print(z,end ="%")
                print()
        elif x > y:
            fraction = input("Fraction: ")
            x,y = fraction.split("/")
            x = int(x)
            y = int(y)


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()