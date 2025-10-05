def Stars(n):
    for i in range(-n,n):
        for j in range(-n,n):
            if (abs(i+j)+1 <= n and abs(j-i)+1 <= n):
                print("*",end="")
            else:
                print(" ",end="")
        print()

n = int(input("Enter a number : "))
Stars(n)