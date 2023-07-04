def main():
    message = input("Greeting: ")
    output = value(message)
    print(f"${output}")
    
def value(greeting):
    v = 0
    if greeting.strip().capitalize() == "Hello" or greeting == "Hello, Newman":
        v = 0
    elif greeting[0].capitalize() == "H":
        v = 20
    else:
        v = 100
    return v


if __name__ == "__main__":
    main()