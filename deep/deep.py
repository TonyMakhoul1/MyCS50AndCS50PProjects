def main():
    question = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    yes_or_no(question)


def yes_or_no(n):
        yes = "yes"
        no = "no"
        if n == "42" | n == "forty-two" | n == "forty two" :
            return yes
        else:
            return no
main()