def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")
    


def pounds_to_float(d):
    new = d.replace("£", "")
    new = float(new)
    return new

def percent_to_float(p):
    new = p.replace("%", "")
    new = int(new)
    new = new/100
    return new

main()
