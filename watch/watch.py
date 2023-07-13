import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"^(\W|\w)+https?://(www\.)?youtube\.com/(.+)/(\w|\W)+$", s, re.IGNORECASE):
        


if __name__ == "__main__":
    main()