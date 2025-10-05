import random as rd
global rows,cols
rows,cols = (5,5)

def random():
    List = [[0 for i in range(rows)] for i in range(cols)]
    for i in range(1,((rows*cols)+1)):
        List[(i//rows)-1][(i%cols)] = rd.randint(0,100)
    return List

def summation(List):
    sum = 0
    for i in range(rows):
        for j in range(cols):
            sum = sum + List[i][j]
    return sum

def avg(List):
    sum = 0
    for i in range(rows):
        for j in range(cols):
            sum = sum = List[i][j]
    return sum/(rows*cols)

def min(List):
    min = 100
    for i in range(rows):
        for j in range(cols):
            if(List[i][j]<min):min = List[i][j]
    return min

def max(List):
    max = 0
    for i in range(rows):
        for j in range(cols):
            if(List[i][j]> max):max = List[i][j]
    return max

List = random()
print(List)
print(f"sum = {summation(List)}")
print(f"average = {avg(List)}")
print(f"min = {min(List)}")
print(f"max = {max(List)}")
