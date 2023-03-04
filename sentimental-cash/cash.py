# TODO
from cs50 import get_float

while True:
    cents = get_float("Cents: ")
    if cents > 0:
        break
amount = cents * 100
coins = {25, 10, 5, 1}