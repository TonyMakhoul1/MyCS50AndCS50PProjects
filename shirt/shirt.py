import sys
import os

def main():
    check_command()
    print("hello")
    try:

    except FileNotFoundError:
        print("Input does not exist")
        sys.exit(1)

def check_command():
    if len(sys.argv) < 3 :
        print("Too few arguments")
        sys.exit(1)
    if len(sys.argv) > 3 :
        print("Too many arguments")
        sys.exit(1)
    file1 = os.path.splitext(sys.argv[1])
    file2 = os.path.splitext(sys.argv[2])
    if file1[1] not in [".jpeg", ".jpg",".png"]:
        print("Invalid output")
        sys.exit(1)
    if file2[1] not in [".jpeg", ".jpg",".png"]:
        print("Invalid output")
        sys.exit(1)

    if file1[1] != file2[1]:
        print("Input and output have different extensions")
        sys.exit(1)



if __name__ == "__main__":
    main()