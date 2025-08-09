#Pongsakorn Sinsuwan 68200609 KMITL PCC 
#Write a program to process and output result ( A = 2, B = 1, C = 3, D = 2.5, E = 3.5)
# a. A*B+E**B
# b. 3*A//2+C*D
# c. (D//2)+(C/A*C%2)
# d. E-(A%2)+(B%2)+(C%2)
A=2
B=1
C=3
D=2.5
E=3.5
answer = int(input("Input number of answer you want \n 1. A*B+E**B \n 2. 3*A//2+C*D \n 3. (D//2)+(C/A*C%2) \n 4. E-(A%2)+(B%2)+(C%2)\n : "))
if answer == 1 :
    print(f"{A*B+E**B}")
elif answer == 2 :
    print(f"{3*A//2+C*D}")
elif answer == 3 :
    print(f"{(D//2)+(C/A*C%2)}")
elif answer == 4 :
    print(f"{E-(A%2)+(B%2)+(C%2)}")
else :
    print(f"error")