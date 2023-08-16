import sys
import csv
def main():

        check_cmd()
        list = []
        try:
             with open(sys.argv[1]) as file:
                  reader = csv.DictReader(file)
                  for row in reader:

        except FileNotFoundError:
             print(f"Could not read {sys.argv[1]}")
             sys.exit(1)


def check_cmd():
    if len(sys.argv) < 3:
        print("Too few arguments")
        sys.exit(1)
    if len(sys.argv) > 3:
        print("Too many arguments")
        sys.exit(1)
    if ".csv" not in (sys.argv[1] and sys.argv[2]):
        print("Not csv file")
        sys.exit(1)


def check_calories(cal):
     if int(cal) < 



#def function_n():


if __name__ == "__main__":
    main()