# TODO
from cs50 import get_string

text = get_string("Text: ")

def count_letters(text):
    counter = 0
    for i in text:
        if text[i].islower() | text[i].isupper:
            counter += 1
    return counter

letters = count_letters(text)

def count_words(text):
    counter = 1
    for i in text:
        if text[i] == 32:
            counter += 1
    return counter
words = count_words(text)

def count_sentences(text):
    counter = 0
    for i in text:
        if text[i] in {33, 46,63}:
            counter += 1
    return counter
sentences = count_sentences(text)

L = (letters / words) * 100
S = (sentences / words) * 100

index = round((0.0588 * L) - (0.296 * S) - 15.8)

print(f"Text: {text}")

if (index < 1):
    print("Before Grade 1")
    elif (indes)

