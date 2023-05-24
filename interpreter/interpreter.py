def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    
    if y == "+":
        result = float(x + z)
        #round(result,1)
        print(result)
    elif y == "-":
        result = float(x - z)
        #round(result,1)
        print(result)
    elif y == "/":
        z != 0
        result = float(x / z)
        #round(result,1)
        print(result)
    elif y == "%":
        z != 0
        result = float(x % z)
        #round(result,1)
        print(result)

main()