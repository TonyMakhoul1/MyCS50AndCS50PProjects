amount = 50

while amount > 0:
    print("Amount Due: ", amount)
    insert = int(input("Insert Coin: "))
    if insert in [5, 10, 20]:
        amount = amount - insert

Change_Owed = 