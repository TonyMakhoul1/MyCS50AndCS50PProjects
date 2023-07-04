def main():
    name = input("Name: ")
    output = shorten(name)
    print(output)

def shorten(word):
    vowel = ["A","E","I","O","U","a","e","i","o","u"]
    for i in word:
        if i in vowel:
            print("", end="")
        else:
            print(i, end ="")
    print()
    return word

if __name__ == "__main__":
    main()