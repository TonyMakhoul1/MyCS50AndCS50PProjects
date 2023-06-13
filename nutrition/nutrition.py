fruits = {
    "Apple": "130",
    "Avocado": "50",
    "Sweet Cherries": "100"
}
item = input("Item: ")
if item in fruits:
    print("Calories:", fruits[item])