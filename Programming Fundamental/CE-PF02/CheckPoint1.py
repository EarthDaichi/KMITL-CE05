#Pongsakorn Sinsuwan 68200609 KMITL PCC CE05
#write a program to Define 3 variables in 1 line and use input to set data,then multiply them and output the result
a,b,c = map(int, input("Enter 3 Numbers(Ex. : 1 2 3) : ").split())
print(f"{a*b*c}")