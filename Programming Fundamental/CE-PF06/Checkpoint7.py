n = int(input("Enter integer number: "))
for i in range (-n,n+1):
    for j in range(-n,n+1):
        if(i==0 or j==0):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()