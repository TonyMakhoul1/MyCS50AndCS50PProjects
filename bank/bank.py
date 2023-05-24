message = input("Greeting: ")

if message.capitalize() == "Hello":
    print("$0",end="")
elif message[0].capitalize() == "H":
    print("$20")
elif message.capitalize() == "Hello, Newman":
    print("$0",end="")
else:
    print("$100")
