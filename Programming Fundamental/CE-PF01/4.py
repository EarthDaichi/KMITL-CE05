#Pongsakorn Sinsuwan 68200609 KMITL PCC CE05
#Write a program to calculate total score of Student's "Programming Fundamental" score from FInal , MidTerm and Homework
Final = int(input("Enter Final Score : "))
Mid = int(input("Enter Midterm Score : "))
HW = int(input("Enter Homework Score : "))
if Final > 50 : print(f"Error Final more than 50%")
elif Mid > 40 : print(f"Error Midterm more than 40%")
elif HW > 10 : print(f"Error Homework more than 10%")
else :
    Total = Final+Mid+HW
    print(f"total score is {Total}")