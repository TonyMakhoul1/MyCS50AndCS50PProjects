# TODO
from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height >= 1 and height <= 8:
        break
i = 1
for i in range(height):
    print((height - i) * " ",end = "")
    print((height) * "#")