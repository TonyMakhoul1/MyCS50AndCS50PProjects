def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    while len(s) <= 6:
        for i in s:
            if i.lower():
                print("Invalid")
                exit()
            if i = '0':



main()