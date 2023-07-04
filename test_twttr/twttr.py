def main():
    name = input("Name: ")
    output = shorten(name)
    print(output)

def shorten(word):
    wrd = ""
    vowel = ["A","E","I","O","U","a","e","i","o","u"]
    for i in word:
        if i not in vowel:
            wrd = wrd + i
    return wrd

if __name__ == "__main__":
    main()