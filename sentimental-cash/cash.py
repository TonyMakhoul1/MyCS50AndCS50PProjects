# TODO
from cs50 import get_float

while True:
    cents = get_float("Cents: ")
    if cents > 0:
        break
amount = cents * 100
coins = {25, 10, 5, 1}
countcoins = 0

for i in coins:
    while amount >= i:
        amount -= i
        countcoins += 1
print(f"{countcoins} coins")