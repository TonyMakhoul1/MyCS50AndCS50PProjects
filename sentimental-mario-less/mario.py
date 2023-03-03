# TODO
from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height >= 1 and height <= 8:
        break
i = 1
j = 1
k = 1
for i  in range(height):
    for j in range(height - i):
        print(" ", end = "")
    for k in range(i):
        print("#")