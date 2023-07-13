import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    link = re.search(r"^(\W|\w)+https?://(www\.)?youtube\.com/(.+)/(\w|\W)+$", s, re.IGNORECASE)
    if link:
        group_link = link.groups()
        return group_link


if __name__ == "__main__":
    main()