message = input("Greeting: ")

if message.capitalize() == "Hello":
    print("$0", end="")
elif message[0] == "H":
    print("$20")

