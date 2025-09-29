print(f"{"ATM":>15}\n Only 1000, 500, 100 banknotes")
money = int(input("Input money : "))
if(100<= money <= 20000):
    while(money != 0):
        print(f"Banknote : \n number of 1000 banknote = {money//1000}")
        money = money % 1000
        print(f" number of 500 banknote = {money//500}")
        money = money % 500
        print(f" number of 100 banknote = {money//100}")
        money = money % 100
else:
    print("Please, enter 100-20000")