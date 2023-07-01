import random
while True:
    try:
        level = int(input("Level: "))
        #level = random.randint(0,100)

    except:
        pass

number = 
while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < level:
                print("Too small!")
                break
            elif guess > level:
                print("Too large!")
                break
            else:
                print("Just right!")
                break