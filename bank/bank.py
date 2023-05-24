message = input("Greeting: ")

if message.capitalize() == "Hello" or message.capitalize() == "Hello, Newman":
    print("$0",end="")
elif message[0].capitalize() == "H":
    print("$20")
else:
    print("$100")
