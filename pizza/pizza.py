import sys
import csv
from tabulate import tabulate
def main():
    check_command()
    try:
        pizz = []
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                pizz.append({"Sicilian Pizza":row["Sicilian Pizza"], "Small":row["Small"], "Large":row["Large"]})
            for piz in pizz:
                #print(piz["Sicilian Pizza"], piz["Small"], piz["Large"])
                print(tabulate(piz, headers = ["Sicilian Pizza", "Small", "Large"], tablefmt="grid"))

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
