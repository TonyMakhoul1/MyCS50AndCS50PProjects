dict = {}
while True:
    try:
        item = input().lower()
        if item in dict:
            dict[item] = dict[item] + 1
        else:
            dict[item] = 1
    except EOFError:
        for item in dict:
            print(dict[item], item.upper())
        break

