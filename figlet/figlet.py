from pyfiglet import Figlet
import sys
import random


if len(sys.argv) == 1:
    afont = random.choice(fonts)
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):

else:
    sys.exit(1)

input = input("Input: ")
fonts = figlet.getFonts()


