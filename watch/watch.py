import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    link = re.search(r"^(\W|\w)+https?://(www\.)?youtube\.com/(\w+)/(\w+)(\w|\W)+$", s, re.IGNORECASE)
    if link:
        group_link = link.groups()
        return f"https://youtu.be/{group_link[3]}"


if __name__ == "__main__":
    main()