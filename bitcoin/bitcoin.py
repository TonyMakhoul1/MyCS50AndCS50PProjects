import sys
import requests

if len(sys.argv) == 2:
    try:
        number = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    result = r.json()
    print(result[])
except requests.RequestException:
    print("Request Exception")
    sys.exit(1)