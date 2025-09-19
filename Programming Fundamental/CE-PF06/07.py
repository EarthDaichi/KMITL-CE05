row = int(input("Enter number of row: "))
col = int(input("Enter number of col: "))
for i in range(1,row):
    for j in range(1,col):
        if j>i:
            print(' ',end='')
        else:
            print('*',' ',end='')
    print()
    