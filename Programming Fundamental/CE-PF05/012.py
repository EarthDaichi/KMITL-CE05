i = 1
count = 0
while(i<101):
    if(i%7 == 0):
        print(i, end= " | ")
        count = count + 1
    i = i + 1
print("Count = ", count)