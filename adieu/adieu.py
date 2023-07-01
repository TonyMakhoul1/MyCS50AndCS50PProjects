# JOIN WORDS INTO A LIST:

#mylist = p.join(("apple", "banana", "carrot"))
# "apple, banana, and carrot"

#mylist = p.join(("apple", "banana"))
# "apple and banana"

#mylist = p.join(("apple", "banana", "carrot"), final_sep="")
# "apple, banana and carrot"

import inflect
p = inflect.engine()
try:
    input = input("Input: ")
except:
    