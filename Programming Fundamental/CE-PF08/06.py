print("Welcome to Exchange Money Program")
print("----- Menu for Exchange Money -----")
print("Press 1 : Thai-Bath to US Dollar")
print("Press 2 : Thai-Bath to Euro")
print("Press 3 : Thai-Bath to Chinese-Yuan")
print("Press 4 : Thai-Bath to Japanese-Yen")
print("Press 5 : Thai-Bath to South Korea-Won")
print("Press 6 : Thai-Bath to Rusia-Ruble")
print("-----------------------------------")

choice = int(input("Please, select only one menu: "))
if choice == 1:
    print("Currenly, you are converting Thai-Bath to US Dollar")
    Bath = float(input("Please, Enter your Thai money: "))
    USDollar = Bath/37.09 #last update 9 october 2023
    print(f"{Bath} Bath = {USDollar} Dollars")
elif choice == 2:
    print("Currenly, you are converting Thai-Bath to Euro")
    Bath = float(input("Please, Enter your Thai money: "))
    Euro = Bath/39.12 #last update 9 october 2023
    print(f"{Bath} Bath = {Euro} Euro")
elif choice == 3:
    print("Currenly, you are converting Thai-Bath to Chinese-Yuan")
    Bath = float(input("Please, Enter your Thai money: "))
    Yuan = Bath/5 #last update 9 october 2023
    print(f"{Bath} Bath = {Yuan} Yuan")
elif choice == 4:
    print("Currenly, you are converting Thai-Bath to Japanese-Yen")
    Bath = float(input("Please, Enter your Thai money: "))
    Yen = Bath*100/25 #last update 9 october 2023
    print(f"{Bath} Bath = {Yen} Yen")
elif choice == 5:
    print("Currenly, you are converting Thai-Bath to South Korea-Won")
    Bath = float(input("Please, Enter your Thai money: "))
    Won = Bath*1000/27 #last update 9 october 2023
    print(f"{Bath} Bath = {Won} Won")
elif choice == 6:
    print("Currenly, you are converting Thai-Bath to Russia-Ruble")
    Bath = float(input("Please, Enter your Thai money: "))
    Ruble = Bath*100/37 #last update 9 october 2023
    print(f"{Bath} Bath = {Ruble} Ruble")
else:
    print("Please, Select menu again")