#Pongsakorn Sinsuwan 68200609 KMITL PCC
#Write a program to exchange currency between USD , Euro and Yuan and loop until user want to stop use it
letter = 'y'
while(letter != 'n'):
    print("----------------This is an currency exchange program----------------")
    print("Press A for USD to euro")
    print("Press B for Euro to USD")
    print("Press C for USD to Yuan")
    print("Press D for Yuan to USD")
    print("Press E for Euro to Yuan")
    print("Press F for Yuan to Euro")
    print("--------------------------------------------------------------------")
    choice = input("Select menu : ")
    if(choice == 'A' or choice == 'a'):
        USD = int(input("Enter USD money : "))
        print(f"{USD} USD = {USD/1.17} Euro")
    elif(choice == 'B' or choice == 'b'):
        Euro = int(input("Enter Euro money :"))
        print(f"{Euro} Euro = {Euro*1.17} USD")
    elif(choice == 'C' or choice == 'c'):
        USD = int(input("Enter USD money : "))
        print(f"{USD} USD = {USD*7.18} Yuan")
    elif(choice == 'D' or choice == 'd'):
        Yuan = int(input("Enter Yuan money :"))
        print(f"{Yuan} Yuan = {Yuan/7.18} USD")
    elif(choice == 'E' or choice == 'e'):
        Euro = int(input("Enter Euro money :"))
        print(f"{Euro} Euro = {Euro*8.30} Yuan")
    elif(choice == 'F' or choice == 'f'):
        Yuan = int(input("Enter Yuan money :"))
        print(f"{Yuan} Yuan = {Yuan/8.30} Yuan")
    letter = input("Press any letter to continue, n = terminated : ")