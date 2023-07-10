import sys
import csv

def main():
    check_command
    try:
        list = []
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                list.append(row)
            print(list[0])
        '''
        with open(sys.argv[2]) as cs:
            writer = csv.writer(cs)
            writer.writerow({"name":name, "house":house})
        '''
    except FileNotFoundError:
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)

def check_command():
    if len(sys.argv) < 3 :
        print("Too few arguments")
        sys.exit(1)
    if len(sys.argv) > 3 :
        print("Too many arguments")
        sys.exit(1)
    if ".csv" not in sys.argv[1] :
        print("Not a CSV file")
        sys.exit(1)

if __name__ == "__main__":
    main()