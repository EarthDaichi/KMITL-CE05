import random as rd

mySet = {rd.randint(1,100) for i in range(20)}

for i in mySet:print(i, end= " ")