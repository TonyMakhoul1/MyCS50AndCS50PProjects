def main():
    text = input("")
    convert(text)
    


def convert(text):

    if ':)' in text :
        x = text.replace(":)","🙂")
        print(x)


    if ':(' in text :
        y = text.replace(":(","🙁")
        print(y)

main()