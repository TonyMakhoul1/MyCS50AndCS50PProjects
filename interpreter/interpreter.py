expression = input("Expression: ")
x, y, z = expression.split(" ")

if y == "+":
    result = x + z
    float(result)
    round(result,1)
elif y == "-":
    result = x - z
    float(result)
    round(result,1)
elif y == "/":
    z != 0
    result = x / z
    float(result)
    round(result,1)
elif y == "%":
    z != 0
    result = x % z
    float(result)
    round(result,1)
