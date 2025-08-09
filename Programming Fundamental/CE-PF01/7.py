#Pongsakorn Sinsuwan 68200609 KMITL PCC CE05
#Write a program to find x from ax^2 + bx + c by ((-b (+-) sqrt((b^2)-4ac))/2a)
from math import sqrt
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
root = sqrt((b*b)-(4*a*c))
x1 = ((-b + root)/(2*a))
x2 = ((-b - root)/(2*a))
print(f"x = {x1} , {x2}")