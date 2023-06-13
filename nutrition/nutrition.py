fruits = {
    "Apple": "130",
    "Avocado": "50",
    "Sweet Cherries": "100"
}
item = input("Item: ")
for i in fruits:
    if item[i] in fruits:
        print("Calories:", item)