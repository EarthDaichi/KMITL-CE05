#Pongsakorn Sinsuwan 68200609 KMITL PCC
#Write a program to calculate for Summary and Average of numbers in range 1000-2000
sum = 0
for number in range(1000,2000) :
    sum += number
print(f"Summation = {sum}")
print(f"Average = {sum/len(range(1000,2000))}")