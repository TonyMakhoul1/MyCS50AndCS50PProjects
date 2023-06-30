import emoji
list = emoji
text = input("Input: ")
text.replace("_","")

for i in list:
    if list[i] == text:
        print("Output: " + list[i])
