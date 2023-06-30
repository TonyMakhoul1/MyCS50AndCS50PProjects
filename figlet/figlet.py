from pyfiglet import Figlet
import sys
import random

input = input("Input: ")
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    afont = random.choice(fonts)

