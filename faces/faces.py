def main():
    text = input("")
    convert(text)
    print(text)


def convert(text):
    text = text.replace(":)","🙂")
    text = text.replace(":(","🙁")



main()