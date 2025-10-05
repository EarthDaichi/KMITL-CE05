import random as rd

Data = []
def MinValue(RData):
    minValue = min(RData)
    print(minValue)
def MaxValue(RData):
    maxValue = max(RData)
    print(maxValue)
    MinValue(RData)
def randomValue(RData):
    for i in range(15):
        n = rd.randint(1,50)
        RData.append(n)
    MaxValue(RData)
    return RData

print(randomValue(Data))
print(sorted(Data))