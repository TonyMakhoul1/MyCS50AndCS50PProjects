dict ={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0
while True:
    try:
        item = input("Item: ")
    except EOFError:
        item = input("Item: ")
    else:
        if item == "":
            quit()
        elif item in dict:
            total = total + dict[item]
            print("Total: $",end="")
            print(total)
        else:
            item = input("Item: ")