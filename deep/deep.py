def main():
    question = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    yes_or_no(question)


def yes_or_no(n):
        yes = "yes"
        no = "no"
        if n == "42" or n == "forty-two" or n == "forty two" :
            print("yes")
            return
        else:
            print("no")
            return 
main()