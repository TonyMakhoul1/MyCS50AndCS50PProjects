fruits = {
    "apple": "130",
    "Avocado": "50",
    "Sweet Cherries": "100",
    "Kiwifruit": "90",
    "pear": "100"
}
item = input("Item: ")
if item in fruits:
    print("Calories:", fruits[item])