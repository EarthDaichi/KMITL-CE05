#Pongsakorn Sinsuwan 68200609 KMITL PCC CE05
#Write and program to input Hours,Minutes and Seconds then arrange to HH:MM:SS
Hr = str(input("Enter Current Hour : "))
Min = str(input("Enter Current Minutes : "))
Sec = str(input("Enter  Current Seconds : "))
if int(Hr) > 24 : print(f"Error Hour is more than 24")
elif int(Min) > 60 : print(f"Error Minutes is more than 60")
elif int(Sec) > 60 : print(f"Error Seconds is more than 60")
else : print(f"Current time = {Hr}:{Min}:{Sec}")