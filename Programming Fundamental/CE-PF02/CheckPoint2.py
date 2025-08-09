#Pongsakorn Sinsuwan 68200609 KMITL PCC 
#Write a program to process and output result (a=2,b=1,c=3,d=2.5,e=3.5)
# 1. a*b+e/b+d*c
# 2. (c*d)*2+(e-a)*c
# 3. (a+c)*(b*2)+3**e
# 4. 6-(a%2)+(b%2)+(c%2)
# 5. (c)+(3*a%2)+e*d
a=2
b=1
c=3
d=2.5
e=3.5
answer = int(input("Input number of answer you want \n 1. a*b+e/b+d*c \n 2. (c*d)*2+(e-a)*c \n 3. (a+c)*(b*2)+3**e \n 4. 6-(a%2)+(b%2)+(c%2) \n 5. (c)+(3*a%2)+e*d \n : "))
if answer == 1 :
    print(f"{a*b+e/b+d*c}")
elif answer == 2 :
    print(f"{(c*d)*2+(e-a)*c}")
elif answer == 3 :
    print(f"{(a+c)*(b*2)+3**e}")
elif answer == 4 :
    print(f"{6-(a%2)+(b%2)+(c%2)}")
elif answer == 5 :
    print(f"{(c)+(3*a%2)+e*d}")
else :
    print(f"error")