# JOIN WORDS INTO A LIST:

#mylist = p.join(("apple", "banana", "carrot"))
# "apple, banana, and carrot"

#mylist = p.join(("apple", "banana"))
# "apple and banana"

#mylist = p.join(("apple", "banana", "carrot"), final_sep="")
# "apple, banana and carrot"

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