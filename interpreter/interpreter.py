def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")

    if y == "+":
        result = x + z
        float(result)
        #round(result,1)
        print(result)
    elif y == "-":
        result = x - z
        float(result)
        #round(result,1)
        print(result)
    elif y == "/":
        z != 0
        result = x / z
        float(result)
        #round(result,1)
        print(result)
    elif y == "%":
        z != 0
        result = x % z
        float(result)
        #round(result,1)
        print(result)

main()