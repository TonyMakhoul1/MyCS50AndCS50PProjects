def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    new_d = d.replace("$", "")
    float_d = float(new_d)
    return float_d

def percent_to_float(p):
    new_p = p.replace("%", "")
    float_p = float(new_p)
    float_p = float_p / 100
    return float_p


main()