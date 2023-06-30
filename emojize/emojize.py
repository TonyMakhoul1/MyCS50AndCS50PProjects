import emoji

text = input("Input: ")
text.replace("_","")

for i in emoji:
    if emoji[i] == text:
        print("Output: " + emoji[i])
        