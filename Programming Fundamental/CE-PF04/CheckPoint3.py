#Pongsakorn Sinsuwan 68200609 KMITL PCC
#Add Summary and Average to a program
sum = 0
a= range(1,101,5)
print("Number of data =", len(a))
#Display data
for i in a :
    print(i ,end = ", ")
    sum+= i
print("\nSummary : ", sum)
print("Average : ", (sum/len(a)))