import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^[0-255]\.[0-255]\.[0-255]\.[0-255]\.$", ip)
    if matches:
        return True
    return False


if __name__ == "__main__":
    main()