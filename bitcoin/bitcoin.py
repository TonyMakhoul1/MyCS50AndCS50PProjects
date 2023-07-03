import sys
import requests

if sys.argv == 2:
    try:
        number = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
else:
    print("Missing command-line argument")
    sys.exit(1)