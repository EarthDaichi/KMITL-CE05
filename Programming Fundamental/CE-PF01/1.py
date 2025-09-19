#Pongsakorn Sinsuwan 68200609 KMITL PCC CE05
#Write a program to find Area of Triangle
from math import sqrt
a = int(input("ระบุความยาวด้านที่ 1 ของสามเหลี่ยมด้านไม่เท่า : "))
b = int(input("ระบุความยาวด้านที่ 2 ของสามเหลี่ยมด้านไม่เท่า : "))
c = int(input("ระบุความยาวด้านที่ 3 ของสามเหลี่ยมด้านไม่เท่า : "))
s = float((a+b+c)/2)
Area = sqrt(s*(s-a)*(s-b)*(s-c))
print(f"พื้นที่ของสามเหลี่ยมด้านไม่เท่า คือ {Area} ตารางหน่วย")