# TODO
from cs50 import get_int

while height < 1 | height > 8:
    height = get_int("Height: ")

for i in range(height):
    for j in range(height - i):
        print(" ")

        for k in range(i):
            print("#")