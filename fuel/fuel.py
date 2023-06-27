try:
    fraction = input("Fraction: ")
    x,y = fraction.split("/")
    x = int(x)
    y = int(y)
except (ValueError, ZeroDivisionError):
    fraction = input("Fraction: ")
    x,y = fraction.split("/")
    x = int(x)
    y = int(y)

except x > y:
    fraction = input("Fraction: ")
    x,y = fraction.split("/")
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
    #elif x > y:


