input = input("Input: ")
vowel = ["A","E","I","O","U","a","e","i","o","u"]
for i in input:
    if i in vowel:
        print("", end="")
    else:
        print(i)