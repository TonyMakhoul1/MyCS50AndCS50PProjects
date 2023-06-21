fraction = input("Fraction: ")
x,y = fraction.split("/")
x = int(x)
y = int(y)

while True:
    try:
        fraction = input("Fraction: ")
    except ValueError:
        print("x or y is not an integer")
    except ZeroDivisionError:
        print ("denominater can't be 0")
    else:
        if x < y:
            x,y