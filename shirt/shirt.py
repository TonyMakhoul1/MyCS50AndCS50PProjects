import sys

def main():
    check_command()
    print("hello")

def check_command():
    if len(sys.argv) < 3 :
        print("Too few arguments")
        sys.exit(1)
    if len(sys.argv) > 3 :
        print("Too many arguments")
        sys.exit(1)
    


if __name__ == "__main__":
    main()