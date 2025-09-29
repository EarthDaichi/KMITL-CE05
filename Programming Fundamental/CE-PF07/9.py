n = int(input("n : "))
if(n==0):
    print("zero")
else:
    if(n>0):
        print("positive even") if(n%2==0) else print("positive odd")
    else:
        print("negative even") if(n%2==0) else print("negative odd")