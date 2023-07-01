import random


def main():
    get_level()


def get_level():
    while True:
        try:
            level = input("Level: ")
            if level <= 3 or level >= 1:
                break
        except:
            pass
    return level



#def generate_integer(level):



if __name__ == "__main__":
    main()