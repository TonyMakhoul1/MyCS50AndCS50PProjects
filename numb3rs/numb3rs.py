import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip = re.search(r"^[0-255]\.[0-255]\.[0-255]\.[0-255]\.$")
    if ip:
        return True
    return False


if __name__ == "__main__":
    main()