fruits = {
    "Apple": "130",
    "Avocado": "50",
    "Sweet Cherries": "100"
}
item = input("Item: ")
for item in fruits:
    if item in fruits:
        print("Calories:", item)