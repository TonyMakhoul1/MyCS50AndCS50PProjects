import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    um = re.findall(r"\W+um\W", s)
    print(um)


if __name__ == "__main__":
    main()