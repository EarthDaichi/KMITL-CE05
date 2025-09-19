#Pongsakorn Sinsuwan 68200609 KMITL PCC
#Add Summary and Average to a program
i = 1
count = 0
sum = 0
while(i<101):
    if(i%4==0) and (i%5==0):
        print(i ,end= " | ")
        count = count + 1
        sum += i
    i = i + 1
    
avg = sum/count
print("Count = ",count)
print("Summary = ",sum)
print("Average = ",avg)