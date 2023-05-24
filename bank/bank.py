message = input("Greeting: ")

if message.capitalize() == "Hello":
    print("$0")
elif message[0] == "H":
    print("$20")
else:
    print("$100")
