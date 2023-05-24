message = input("Greeting: ")

if message.capitalize().strip() == "Hello":
    print("$0",end="")
elif message[0].capitalize() == "H":
    print("$20")
else:
    print("$100")
