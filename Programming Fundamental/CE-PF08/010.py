Jacob = 127550.84; Kevin = 35242.75; Jeno = 76219.35
choice = 0
def AccountInfo(pincode):
    if pincode == 1744355:
        name = "Jacob"
        return name,Jacob
    elif pincode == 5002587:
        name = "Kevin"
        return name,Kevin
    elif pincode == 1776809:
        name = "Jeno"
        return name,Jeno
    else:
        return "NO name",0
def Display():
    print("------- Menu -------")
    print("Press 1: Withdraw")
    print("Press 2: Deposite")
    print("Press 3: Transfer")
    print("Press 4: Exit")
    print("--------------------")
    choice = int(input("Please, select only 1 menu: "))
    return choice
def Withdraw(name,Money):
    print("Withdraw your money")
    WMoney = float(input("Please, enter money: "))
    if WMoney <= Money:
        print(f"Withdraw = {WMoney} Bath")
        print(f"Please, get your money")
        print(f"Now, {name} remain money = {Money-WMoney} Bath")
    else:
        print("Your money is not enoough. Please, try again")
def Deposit(name,Money):
    print("Deposite your money")
    DMoney = float(input("Please, enter money: "))
    print(f"Now, {name} remain money = {Money+DMoney} Bath")
def Transfer(name,Money,AccountNo,Jacob,Kevin,Jeno):
    print("Transfer your money")
    if AccountNo == 4380902154:
        print(f"Now, {name} require to transfer money to Jacob")
        TMoney = float(input("Please, enter money: "))
        if TMoney <= Money:
            print(f"Transfer = {TMoney} Bath")
            Jacob = Jacob+TMoney
            print(f"Now, {name} remain money = {Money-TMoney} Bath")
        else:
            print("Your money is not enough. Please, try again")
    elif AccountNo == 1691600607:
        print(f"Now, {name} require to transfer money to Kevin")
        TMoney = float(input("Please, enter money: "))
        if TMoney <= Money:
            print(f"Transfer = {TMoney} Bath")
            Kevin = Kevin+TMoney
            print(f"Now, {name} remain money = {Money-TMoney} Bath")
        else:
            print("Your money is not enough. Please, try again")
    elif AccountNo == 8030487371:
        print(f"Now, {name} require to transfer money to Jeno")
        TMoney = float(input("Please, enter money: "))
        if TMoney <= Money:
            print(f"Transfer = {TMoney} Bath")
            Jeno = Jeno+TMoney
            print(f"Now, {name} remain money = {Money-TMoney} Bath")
        else:
            print("Your money is not enough. Please, try again")
    else:
        print("Please, enter account number again")
def Exit():
    print("Goodbye, see you next time")

pincode = int(input("Please, enter your pincode 7 digits: "))
name,Money = AccountInfo(pincode)
print(f"Hello {name}. You have {Money} Bath")
choice = Display()
if choice == 1:
    Withdraw(name,Money)
elif choice == 2:
    Deposit(name,Money)
elif choice == 3:
    AccountNo = int(input("Enter account number to transfer: "))
    Transfer(name,Money,AccountNo,Jacob,Kevin,Jeno)
elif choice == 4:
    Exit()
else:
    print("Please, select menu again")