def main():
    text = input("")
    convert(text)
    print(text)


def convert(text):
    x = text.find(":)")
    if x == ':)':
        newx = text.replace(":)","🙂")
        print(newx)

    y = text.find(":(")
    if y == ':(':
        newy = text.replace(":(","🙁")
        print(newy)

main()