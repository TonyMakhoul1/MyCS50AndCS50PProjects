def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0:2].isalpha() == False:
        return False
    for i in s:
        if i == "0":
            return False
        




main()