import random as rd

data = [rd.randint(1,100) for i in range(20)]
print("Display 1st time = ", data)

data.pop(); data.pop()
print("Display 2nd time = ", data)