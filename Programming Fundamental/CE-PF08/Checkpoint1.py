import math
m = -1
def triangle(x):
    area = math.sqrt(3)/4*x*x
    return area
def square(x,y):
    area = x*y
    return area
def cube(x):
    volume = x*x*x
    return volume
def sphere(r):
    volume = 4/3 * 3.142*r*r*r
    return volume
while(m!=0):
    print(f"{"-"*8}Menu{"-"*8}")
    print(" 1.area of triangle")
    print(" 2.area of square")
    print(" 3.volume of cube")
    print(" 4.volume of sphere")
    print(f"{"-"*20}")
    m = int(input("Select : "))
    if(m==1):
        x = int(input("Enter side lenght of triangle : "))
        print(f"area of triangle = {triangle(x)}")
    elif(m==2):
        x = int(input("Enter lenght of side A : "))
        y = int(input("Enter lenght of side B : "))
        print(f"area of square = {square(x,y)}")
    elif(m==3):
        x = int(input("Enter side lenght of cube : "))
        print(f"volume of cube = {cube(x)}")
    elif(m==4):
        x = int(input("Enter radius of sphere : "))
        print(f"volume of sphere = {sphere(x)}")
    else:
        print("Error")
    m = input("Enter 0 to exit : ")