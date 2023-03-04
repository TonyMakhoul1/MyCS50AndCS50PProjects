# TODO
from cs50 import get_string

text = get_string("Text: ")



L = (letters / words) * 100
S = (sentences / words) * 100

index = round((0.0588 * L) - (0.296 * S) - 15.8)

print(f"Text: {text}")

if (index < 1):
    print("Before Grade 1")
elif (index >= 16):
    print("Grade 16+")
else:
    print(f"Grade {index}")

