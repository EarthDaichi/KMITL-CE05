def promotion(cost,sales):
    if(0 <= sales <= 100 or cost >= 0):
        bonus = cost*sales/100
        cost = cost - bonus
        return cost
    return cost

cost = int(input("Enter cost of product : "))
sales = int(input("Enter a percent : "))
print(f"You have to pay {promotion(cost,sales)} for this product")