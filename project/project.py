import sys
import csv
def main():

        check_cmd()
        try:
             with open(argv[1]) as file:
                  reader = csv.Dictreader(file)
                  for row in reader:
                       print(row)
        except FileNotFoundError:
             print(f"Could not read {argv[1]}")
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


#def function_2():



#def function_n():


if __name__ == "__main__":
    main()