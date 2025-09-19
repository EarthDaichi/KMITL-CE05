#Pongsakorn Sinsuwan 68200609 KMITL PCC
#PF subject score max 100
#A  : Score >= 80       |   #B+ : 80 > Score >= 75   |   #B  : 75 > Score >= 70   |   #C+ : 70 > Score >= 65
#C  : 65 > Score >= 60  |   #D+ : 60 > Score >= 55   |   #D  : 55 > Score >= 50   |   #F  : 50 > Score
score = float(input("Enter your score : "))
if score >= 80 :
    print(f"You obtain grade A")
elif score >= 75 :
    print(f"You obtain grade B+")
elif score >= 70 :
    print(f"You obtain grade B")
elif score >= 65 :
    print(f"You obtain grade C+")
elif score >= 60 :
    print(f"You obtain grade C")
elif score >= 55 :
    print(f"You obtain grade D+")
elif score >= 50 :
    print(f"You obtain grade D")
else :
    print(f"You obtain grade F, See you again next semester")
