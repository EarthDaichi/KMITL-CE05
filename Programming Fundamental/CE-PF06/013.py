n = int(input("Enter integer number: "))
for i in range(1,2*n):
    for j in range(1,2*n):
        if (i+j >= n+1) and (j-i < n):
            print('*',end='')
        else:
            print(' ',end='')
    print()
