#Pongsakorn Sinsuwan 68200609 KMITL PCC
#Write a program to calculate BMI
Height = float(int(input("Enter your Height(cm) : "))/100)
Weight = float(input("Enter your Weight(kg) : "))
BMI = float(Weight/(Height*Height))

if BMI < 18.50 :
    print(f"Your BMI : {BMI} , You are Thin")
elif BMI >= 18.50 and BMI < 23.00 :
    print(f"Your BMI : {BMI} , You are Good Shape")
elif BMI >= 23.00 and BMI < 25.00 :
    print(f"Your BMI : {BMI} , You are Chubby")
elif BMI >= 25.00 and BMI < 30.00 :
    print(f"Your BMI : {BMI} , You are Fat")
else :
    print(f"Your BMI : {BMI} , You are Very Fat")