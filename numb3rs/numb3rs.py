import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search("^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+\.$", ip):
        list = ip.split(".")
        print(list)


if __name__ == "__main__":
    main()