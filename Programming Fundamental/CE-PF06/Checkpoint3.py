i=1
while(i<9):
    j=1
    while(j<9):
        if(i+j)%2==0:
            print('X', ' ',end='')
        else:
            print('O', ' ',end='')
        j+=1
    i+=1
    print()
    