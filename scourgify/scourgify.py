import sys
import csv

def main():
    check_command
    list = []
    try:

        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"].split(",")
                list.append({"first": name[1].lstrip(), "last": name[0], "house": row["house"]})
            



        with open(sys.argv[2],"w") as cs:
            writer = csv.DictWriter(cs, filednames=["first", "last", "house"])
            for s in list:
                writer.writerow({"first": s["first"], "last":s["last"], "house":s["house"]})


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
    if ".csv" not in (sys.argv[1] or sys.argv[2]) :
        print("Not a CSV file")
        sys.exit(1)

if __name__ == "__main__":
    main()