import validators
input = input("What's your email? ")
true = validators.email(input)
if true:
    print("valid")
else:
    print("invalid")