# TODO
import cs50
from cs50 import get_int
def get_cents():
    while True:
        cents = get_int("Cents: ")
        if cents > 0:
            break

def calculate_quarters(cents):
    q = cents / 25
    return q

def calculate_dimes(cents):
    d = cents / 10
    return d

def calculate_nickels(cents):
    n = cents / 5
    return n

def calculate_pennies(cents):
    p = cents / 1
    return p


def main():
    int 
    cents = get_cents()

    quarters = calculate_quarters(cents)
    cents = cents - quarters * 25

    dimes = calculate_dimes(cents)
    cents = cents - dimes * 10

    nickels = calculate_nickels(cents)
    cents = cents - nickels * 5

    pennies = calculate_pennies(cents)
    cents = cents - pennies * 1

    coins = quarters + dimes + nickels + pennies

    print(coins)

if __name__=='__main__':
    main()