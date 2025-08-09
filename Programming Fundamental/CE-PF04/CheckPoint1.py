#Pongsakorn Sinsuwan 68200609 KMITL PCC
#Write a program to input a number and output multiply tables from 1 to 12 of input number
n = int(input("Enter a number : "))
for i in range(1,13,1) :
    print(f"{n} x {i} = {n*i}")