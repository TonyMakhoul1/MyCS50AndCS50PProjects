def main():
    question = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    yes_or_no(question)


def yes_or_no(n):
        rn = n.rstrip()
        ln = n.lstrip()
        if n == "42" or n == "forty-two" or n == "forty two" or n == "FoRty TwO" or rn or ln:
            print("yes", end="")
            return
        else:
            print("no", end="")
            return
main()