import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search("^([0-9]+\.){3}[0-9]+$", ip):
        list = ip.split(".")
        for s in list:
            if s > 255 or s < 0:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()