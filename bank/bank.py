message = input("Greeting: ")

if message.strip().capitalize() == "Hello" or message == "Hello, Newman":
    print("$0")
elif message[0].capitalize() == "H":
    print("$20")
else:
    print("$100")
