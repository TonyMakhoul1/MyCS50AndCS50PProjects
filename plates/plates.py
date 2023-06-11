def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6:
        return False
    else:
        if s[0:2].isdigit() or s[0:2].isalpha.lower():
            return False




main()