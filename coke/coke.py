amount = 50

while amount > 0:
    print("Amount Due: ", amount)
    insert = int(input("Insert Coin: "))
    if insert in [5, 10, 25]:
        amount = amount - insert

Change_Owed = abs(amount)
print("Change_Owed: ", Change_Owed)