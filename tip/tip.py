def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO

    float(d)
    format(d, 2)





def percent_to_float(p):
    # TODO
    p = x / 100
    return p


main()