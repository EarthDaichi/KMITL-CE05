#Pongsakorn Sinsuwan 68200609 KMITL PCC
#Add Summary and Average to a program
count = 0
sum = 0
i = 1
while(i < 101):
    print(i,end= " ")
    i = i+5
    count = count + 1
    sum+= i
avg = sum/count
print("\nCount = %d" %count)
print("Summary = %d" %sum)
print("Average = %d" % avg)