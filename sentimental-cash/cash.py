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