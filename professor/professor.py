import random


def main():
    level = get_level()
    score = rounds(level)
    print("Score: ", score)




def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 3 and level >= 1:
                break
        except:
            pass
    return level



def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
    else:
        raise ValueError
    return x,y

def round(x,y):
    i = 3
    while i > 0:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                i -= 1
                print("EEE")
        except:
            i -= 1
            print("EEE")
    print(f"{x} + {y} = {x + y}")
    return False

def rounds(level):
    i = 10
    score = 0
    while i >= 1:
        x,y = generate_integer(level)
        result = round(x,y)
        if result == True:
            score += 1
        i -= 1
    return score

if __name__ == "__main__":
    main()