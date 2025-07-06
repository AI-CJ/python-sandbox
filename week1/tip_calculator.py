def calc_tip(bill: float, percent: float = .18) -> float:
    return round(bill * percent, 2)

if __name__ == "__main__":
    bill = float(input("Bill amount: $"))
    percent = float(input("Tip percent (e.g. 0.18): "))
    print("Tip = $", calc_tip(bill, percent))