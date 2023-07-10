import sys
import csv
from tabulate import tabulate
def main():
    check_command()
    try:
        pizz = []
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                pizz.append(row)
            #for piz in pizz:
                print(pizz)
                #print(tabulate(pizz, headers = ["Sicilian Pizza", "Small", "Large"], tablefmt="grid"))

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

if __name__ == "__main__":
    main()
