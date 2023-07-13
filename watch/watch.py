import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"^<\w+https?://(www\.)?youtube\.com/(.+)/\w+$", s, re.IGNORECASE):
        print("yes")


if __name__ == "__main__":
    main()