#Pongsakorn Sinsuwan 68200609 KMITL PCC
#Add Summary and Average to a program
count = 0
sum = 0
for i in range(1,101):
    if(i%4==0) and (i%5==0):
        count+=1
        print(i ,end = " ")
        sum+=i
    
avg = sum/count
print("\nNumber of count = ",count)
print("Summary = ",sum)
print("Average = ",avg)