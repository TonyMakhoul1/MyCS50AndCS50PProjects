import sys
import csv
def main():
        addinglist = []
        list = []
        callist = []
        prilist = []
        check_cmd()
        with open(sys.argv[1]) as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        list.append(row)




        while True:
            print("""
                    1)       Menu
                    2)       Add your meal
                    3)       Withdraw a meal
                    4)       exit
                  """)

            try:
                 Option = int(input("Enter option: "))
                 print()
            except Exception as e:
                 print("Error:", e)
                 print("Enter 1, 2, 3 or 4 only")
                 continue

            if Option == 1:

                try:
                    with open(sys.argv[1]) as file:
                        reader = csv.DictReader(file)
                        for row in reader:
                            list.append(row)
                        for row in list:
                             print(row)



                except FileNotFoundError:
                    print(f"Could not read {sys.argv[1]}")
                    sys.exit(1)


            if Option == 2:

                name = input("What do you want to add? ").capitalize()
                for row in list:
                    if row["Name"] == name:
                        addinglist.append(row)
                print("The new list")
                print()
                print()
                print(addinglist)


            if Option == 3:
                 rem = input("What do you want to remove? ").capitalize()
                 for row in addinglist:
                      if row["Name"] == rem:
                           addinglist.remove(row)
                      print("The new list")
                      print()
                      print()
                      print(addinglist)


            if Option == 4:

                for row in addinglist:
                    calories = check_calories(row["Calories"])
                    price = check_price(row["Price"])
                    callist.append({"Name":name, "Description": calories, "Cost":price})

                    #prilist.append(price)

                print(callist)
                #print(prilist)



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
     if int(cal) < 150:
          return "To all weight"
     elif int(cal) < 300:
          return "To 120 Kg"
     elif int(cal) < 400:
          return "To 100 Kg"
     else:
          return "To 80 Kg"



def check_price(pri):
     if int(pri) < 15:
          return "Low cost"
     elif int(pri) < 25:
          return "Well cost"
     else:
          return "High cost"



if __name__ == "__main__":
    main()