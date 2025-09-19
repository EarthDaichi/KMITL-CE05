h = int(input("Enter your height (cm) : "))
w = int(input("ENter your weight (kg) : "))
cal = h-w
if(cal>115):
    print("You are thin")
elif(cal<= 115 and cal>=100):
    print("You are good shape")
else:
    print("You are fat")