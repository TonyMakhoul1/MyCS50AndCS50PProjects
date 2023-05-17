def main():
    text = input("")
    convert(text)



def convert(text):

    if ':)' or ':(' in text :
        if ':)':
        x = text.replace(":)","🙂")
        print(x)
        if ':(':
        y = text.replace(":(","🙁")
        print(y)

main()