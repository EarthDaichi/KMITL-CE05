Jacob = 127550.84; Kevin = 35242.75; Jeno = 76219.35
pincode = int(input("Please, enter your code 7 digits : "))
#Jacob's Account
if pincode == 1744355:
    print("Hello Jacob, you have %.2f Bath" %Jacob)
    print("------- Menu -------")
    print("Press 1: Withdraw")
    print("Press 2: Deposite")
    print("Press 3: Transfer")
    print("Press 4: Exit")
    choice = int(input("Please, select menu: "))
    if choice == 1:
        print("Withdraw your money")
        WMoney = float(input("Please, enter money: "))
        if WMoney <= Jacob:
            print(f"Withdraw = {WMoney} Bath")
            print(f"Please, get your money")
            print(f"Now, your balance = {Jacob-WMoney} Bath")
        else:
            print("Your money is not enough. Please, try again")
    elif choice == 2:
        print("Deposite your money")
        DMoney = float(input("Please, enter money: "))
        print(f"Now, you have money = {Jacob+DMoney} Bath")
    elif choice == 3:
        print("Transfer your money")
        Account = int(input("Enter Account Number 10 digits : "))
        if Account == 1691600607:
            print("Now, you require to transfer money to Kevin")
            TMoney = float(input("Please, enter money: "))
            if TMoney <= Jacob:
                print(f"Transfer = {TMoney} Bath")
                Kevin = Kevin+TMoney
                print(f"Now, your balance = {Jacob-TMoney} Bath")
            else:
                print("Your money is not enough. Please, try again")
        elif Account == 8030487371:
            print("Now, you require to transfer money to Jeno")
            TMoney = float(input("Please, enter money: "))
            if TMoney <= Jacob:
                print(f"Transfer = {TMoney} Bath")
                Jeno = Jeno+TMoney
                print(f"Now, your balance = {Jacob-TMoney} Bath")
            else:
                print("Your money is not enough. Please, try again")
        else:
            print("Please, enter account number again")
    elif choice == 4:
        print("Goodbye, see you again next time")
    else:
        print("Please, select menu again")
#Kevin's Account
elif pincode == 5002587:
    print("Hello Kevin, you have %.2f Bath" %Kevin)
    print("------- Menu -------")
    print("Press 1: Withdraw")
    print("Press 2: Deposite")
    print("Press 3: Transfer")
    print("Press 4: Exit")
    choice = int(input("Please, select menu: "))
    if choice == 1:
        print("Withdraw your money")
        WMoney = float(input("Please, enter money: "))
        if WMoney <= Kevin:
            print(f"Withdraw = {WMoney} Bath")
            print(f"Please, get your money")
            print(f"Now, your balance = {Kevin-WMoney} Bath")
        else:
            print("Your money is not enough. Please, try again")
    elif choice == 2:
        print("Deposite your money")
        DMoney = float(input("Please, enter money: "))
        print(f"Now, you have money = {Kevin+DMoney} Bath")
    elif choice == 3:
        print("Transfer your money")
        Account = int(input("Enter Account Number 10 digits : "))
        if Account == 4380902154:
            print("Now, you require to transfer money to Jacob")
            TMoney = float(input("Please, enter money: "))
            if TMoney <= Kevin:
                print(f"Transfer = {TMoney} Bath")
                Jacob = Jacob+TMoney
                print(f"Now, your balance = {Kevin-TMoney} Bath")
            else:
                print("Your money is not enough. Please, try again")
        elif Account == 8030487371:
            print("Now, you require to transfer money to Jeno")
            TMoney = float(input("Please, enter money: "))
            if TMoney <= Kevin:
                print(f"Transfer = {TMoney} Bath")
                Jeno = Jeno+TMoney
                print(f"Now, your balance = {Kevin-TMoney} Bath")
            else:
                print("Your money is not enough. Please, try again")
        else:
            print("Please, enter account number again")
    elif choice == 4:
        print("Goodbye, see you again next time")
    else:
        print("Please, select menu again")
#Jeno's Account
elif pincode == 1776809:
    print("Hello Jeno, you have %.2f Bath" %Jeno)
    print("------- Menu -------")
    print("Press 1: Withdraw")
    print("Press 2: Deposite")
    print("Press 3: Transfer")
    print("Press 4: Exit")
    choice = int(input("Please, select menu: "))
    if choice == 1:
        print("Withdraw your money")
        WMoney = float(input("Please, enter money: "))
        if WMoney <= Jeno:
            print(f"Withdraw = {WMoney} Bath")
            print(f"Please, get your money")
            print(f"Now, your balance = {Jeno-WMoney} Bath")
        else:
            print("Your money is not enough. Please, try again")
    elif choice == 2:
        print("Deposite your money")
        DMoney = float(input("Please, enter money: "))
        print(f"Now, you have money = {Jeno+DMoney} Bath")
    elif choice == 3:
        print("Transfer your money")
        Account = int(input("Enter Account Number 10 digits : "))
        if Account == 4380902154:
            print("Now, you require to transfer money to Jacob")
            TMoney = float(input("Please, enter money: "))
            if TMoney <= Jeno:
                print(f"Transfer = {TMoney} Bath")
                Jacob = Jacob+TMoney
                print(f"Now, your balance = {Jacob-TMoney} Bath")
            else:
                print("Your money is not enough. Please, try again")
        elif Account == 1691600607:
            print("Now, you require to transfer money to Kevin")
            TMoney = float(input("Please, enter money: "))
            if TMoney <= Jeno:
                print(f"Transfer = {TMoney} Bath")
                Kevin = Kevin+TMoney
                print(f"Now, your balance = {Jeno-TMoney} Bath")
            else:
                print("Your money is not enough. Please, try again")
        else:
            print("Please, enter account number again")
    elif choice == 4:
        print("Goodbye, see you again next time")
    else:
        print("Please, select menu again")
else:
    print("There are no Account. Please, enter pincode again")