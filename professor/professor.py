import random


def main():
    get_level()


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
    while True:
        try:
            input = input("generate level: ")
            input = random.randint(1,level)
            



if __name__ == "__main__":
    main()