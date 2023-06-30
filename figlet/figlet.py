from pyfiglet import Figlet
import sys
from random import choice

figlet = Figlet()

if len(sys.argv) == 1:
    random = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    random = False
else:
    sys.exit(1)

input = input("Input: ")
figlet.getFonts()

if random == False:
    try:
        figlet.setFont(font = sys.argv[2])
        print(figlet.renderText(input))
    except:
        print("Invalid usage")
        sys.exit(1)

else:
    nfont = figlet.getFonts()
    randfont = choice(nfont)
    figlet.setFont(font = randfont)
    print(figlet.renderText(input))
