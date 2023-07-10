import sys

def main():
    check_command()
    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()
        count = 0
        for line in lines:
            if check_countable(line) == False:
                count = count + 1
        print(count)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

def check_countable(line):
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    return False

def check_command():
    if len(sys.argv) < 2 :
        print("Too few arguments")
        sys.exit(1)
    if len(sys.argv) > 2 :
        print("Too many arguments")
        sys.exit(1)
    if ".py" not in sys.argv[1] :
        print("Not a python file")
        sys.exit(1)

if __name__ == "__main__":
    main()