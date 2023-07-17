def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    number_string = d.replace('$', '')
    float_value = float(number_string)
    return float_value

def percent_to_float(p):
    # TODO
    percent_string = float(p.replace('%', ''))
    percentage = float(percent_string * .01)
    return percentage

main()