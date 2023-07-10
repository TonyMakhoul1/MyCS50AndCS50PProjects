import sys

def main():
    check_command()
    try:
        

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)




def check_command():
    if len(sys.argv) < 2 :
        print("Too few arguments")
        sys.exit(1)
    if len(sys.argv) > 2 :
        print("Too many arguments")
        sys.exit(1)
    if ".csv" not in sys.argv[1] :
        print("Not a CSV file")
        sys.exit(1)
