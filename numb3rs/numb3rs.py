import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^([0-9]+\.){4}$", ip):
        print(ip)


if __name__ == "__main__":
    main()