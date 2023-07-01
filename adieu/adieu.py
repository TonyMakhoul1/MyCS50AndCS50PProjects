import inflect
p = inflect.engine()
list = []
while True:
    try:
        str = input("Input: ")
        list.append(str)
    except EOFError:
        mylist = p.join(list)
        print("Adieu, adieu, to", mylist)
        exit()