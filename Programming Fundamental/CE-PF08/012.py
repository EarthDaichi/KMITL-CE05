import random as rd

Data = []
#Random number 1-50 into Data (15 value)
for i in range(15):
    n = rd.randint(1,50)
    Data.append(n)
print(Data)

#Find Maximum
maxValue = max(Data)
print(maxValue)
#Find Minimum
miniValue = min(Data)
print(miniValue)
#Sorting
print(sorted(Data))