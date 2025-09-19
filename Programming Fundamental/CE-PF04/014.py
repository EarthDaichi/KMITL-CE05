count = 0
for i in range(1,101):
    if(i%4==0) and (i%5==0):
        count += 1
        print(i, end= " ")

print('\nNumber of count = ', count)