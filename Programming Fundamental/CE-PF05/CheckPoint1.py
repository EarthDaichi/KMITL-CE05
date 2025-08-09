#Pongsakorn Sinsuwan 68200609 KMITL PCC
#Write a program to input a number and output multiply tables from 1 to 12 of input number (Use While Loop)
i = 1
n = int(input("Enter a Number : "))
while i < 13 :
    print(f"{n}x{i}={n*i}")
    i+=1