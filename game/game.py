import random
while True:
    try:
        level = int(input("Level: "))
        #level = random.randint(0,100)
        guess = int(input("Guess: "))
        if guess < level:
            print("Too small!")
            break
        elif guess > level:
            print("Too large!")
            break
        else:
            print("Just right!")
            break
    except:
        print()
        exit()