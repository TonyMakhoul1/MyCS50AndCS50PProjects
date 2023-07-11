import sys

def main():
    check_command()

def check_command():
    if len(sys.argv) < 3 :
        print("Too few arguments")
        sys.exit(1)
    if len(sys.argv) > 3 :
        print("Too many arguments")
        sys.exit(1)
    if (".jpeg" or "jpg" or "png") not in (sys.argv[1] or sys.argv[2]) :
        print("Not a CSV file")
        sys.exit(1)


if __name__ == "__main__":
    main()