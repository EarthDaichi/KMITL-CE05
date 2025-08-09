#Pongsakorn Sinsuwan 68200609 KMITL PCC 
#Write a program to process and output result (A = 'B', B = 'a', C = -5.5, D = 2)
# 1.  (not(A != 'A') and ((C//2) > D)
# 2. (B <= 'T') or ((D-C) > 0)
# 3. (A <= 'a') and ((C+D) == 3)
# 4. (C**D) > (C*D)
A = 'B'
B='a'
C=-5.5
D=2
answer = int(input("Input number of answer you want \n 1. (not(A != 'A') and ((C//2) > D) \n 2.  (B <= 'T') or ((D-C) > 0) \n 3.  (A <= 'a') and ((C+D) == 3) \n 4. (C**D) > (C*D) \n : "))
if answer == 1 :
    print(f"{(not(A != 'A')) and ((C//2) > D)}")
elif answer == 2 :
    print(f"{ (B <= 'T') or ((D-C) > 0)}")
elif answer == 3 :
    print(f"{(A <= 'a') and ((C+D) == 3)}")
elif answer == 4 :
    print(f"{(C**D) > (C*D)}")
else :
    print(f"error")