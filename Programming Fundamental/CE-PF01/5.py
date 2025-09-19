#Pongsakorn Sinsuwan 68200609 KMITL PCC CE05
#Write a program to calculate mean of 4 inputs
x1,x2,x3,x4 = list(map(int, input("Enter 4 Numbers (Ex. 1 2 3 4) : ").split()))
Mean = ((x1+x2+x3+x4)/4)
print(f"Mean = {Mean}")