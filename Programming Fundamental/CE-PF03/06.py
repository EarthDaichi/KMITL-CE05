salary = int(input("Enter your salary : "))
Myear = salary*12
if(Myear >1000000):
    ptax = Myear*0.1
    print('You will pay personal tax = ', ptax)
elif(Myear >= 750000):
    ptax = Myear*0.08
    print('You will pay personal tax = ', ptax)
elif(Myear >= 500000):
    ptax = Myear*0.05
    print('You will pay personal tax = ', ptax)
else:
    print("You are attemp personal tax")