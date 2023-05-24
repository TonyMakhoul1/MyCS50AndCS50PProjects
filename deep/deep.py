def main():
question = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
yes = "yes"
no = "no"
yes_or_no(question)


def yes_or_no(question):
        if question == 42 | question == "forty-two" | question == "forty two" :
            return yes
        else:
            return no
main()