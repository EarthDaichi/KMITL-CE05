sum = 0
for num in range(1,101):
    if(num%5 == 0):
        sum = sum+num
        print("AT num = %d, sum = %d" %(num,sum))