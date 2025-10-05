def ProfitCalculator(cost,sale):
    if sale < 0 :
        print("Sales < 0")
    elif cost < 0 :
        print("Cost < 0")
    else:
        profit = sale-cost
        return profit

cost = int(input("Enter cost : "))
sale = int(input("Enter sale : "))
print(f"Profit = {ProfitCalculator(cost,sale)}")