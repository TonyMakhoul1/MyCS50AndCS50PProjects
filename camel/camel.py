camelCase = input("camelCase: ")
print("snake_Case: ", end = "")

for s in camelCase :
    if s.isupper():
        print("_" + s.lower(), end = "")
    else :
        print(s, end = "")
print()

