def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    x = int(x)
    z = int(z)
    if y == "+":
        result = float(x + z)
        #round(result,1)
        print(result)
    elif y == "-":
        result = float(x - z)
        print(result)
    elif y == "*":
        result = float(x * z)
        print(result)
    elif y == "/":
        z != 0
        result = float(x / z)
        print(result)
    elif y == "%":
        z != 0
        result = float(x % z)
        print(result)

main()