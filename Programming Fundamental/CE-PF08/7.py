def trade(money):
    ten = five = two = one = 0
    if(money>=10):
        ten = money // 10
        money = money % 10
    if(money>=5):
        five = money // 5
        money = money % 5
    if(money>=2):
        two = money // 2
        money = money % 2
    if(money>=1):
        one = money // 1
        money = money % 1
    return ten,five,two,one

money = int(input("Enter your money : "))
print(f"Your coins are:\nTen Bath : {trade(money)[0]}\nFive Bath : {trade(money)[1]}")
print(f"Two Bath : {trade(money)[2]}\nOne Bath : {trade(money)[3]}")