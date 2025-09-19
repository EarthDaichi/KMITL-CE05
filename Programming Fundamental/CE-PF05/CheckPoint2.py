#Pongsakorn Sinsuwan 68200609 KMITL PCC
#Write a program to calculate for Summary and Average of numbers in range 1000-2000 (Use While Loop)
sum = 0
number = 1000
while(number <= 2000):
    sum += number
    number+=1
print(f"Summation = {sum}")
print(f"Average = {sum/len(range(1000,2000))}")