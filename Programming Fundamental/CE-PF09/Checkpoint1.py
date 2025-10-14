import random as rd

data = [rd.randint(1,100) for i in range(20)]
print("Display 1st time = ", data)

for i in range(3):data.append(rd.randint(1,100))
print("Display 2nd time = ", data)

data.insert(5,rd.randint(1,100)); data.insert(15,rd.randint(1,100))
print("Display 3rd time = ", data)