n = int(input("Enter a number : "))
for i in range (-n,n+1):
    for j in range(-n,n+1):
        print("*",end=" ") if(i==0 or j==0) else print(" ",end=" ")
    print()