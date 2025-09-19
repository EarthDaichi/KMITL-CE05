#Pongsakorn Sinsuwan 68200609 KMITL PCC CE05
#Write a program to input 3 data which are Student ID , Name and Entry year ,then arrange them and output
print(f"กรุณาป้อนข้อมูลดังต่อไปนี้")
SID = str(input("Enter your Student ID : "))
Name = str(input("Enter your name : "))
Year = str(input("Enter your entry year : "))
print(f"Student ID : {SID:<10}| Name       : {Name}")
print(f"Year Entry : {Year:<10}| Department : Computer Engineering")