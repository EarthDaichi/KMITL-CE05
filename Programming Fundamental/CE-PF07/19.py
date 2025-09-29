n = int(input("Enter a number : "))
for i in range(-n-1,n+1):
    for j in range(-n-1,n+1):
        print("*", end="") if(abs(i-j)<n and abs(i+j)<n) else print(" ",end="")
    print()