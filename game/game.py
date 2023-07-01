import random
while True:
    try:
        level = input("Level: ")
        level = random.randint(0,100)
    except:
        print()
        exit()