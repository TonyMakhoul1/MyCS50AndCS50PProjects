import validators
input = validators.email('someone@example.com')
if input:
    print("valid")
print("invalid")