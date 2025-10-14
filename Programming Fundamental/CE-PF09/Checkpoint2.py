import random as rd

data = [rd.randint(0,500) for i in range(30)]
print("Display 1st time = ", data)
data[13] = 333
print("Display 2nd time = ", data)
for i in range(3): data.pop()
print("Display 3rd time = ", data)
for i in range(3):data.pop(0)
print("Display 4th time = ", data)
print("Sorted = ", sorted(data))
print("Summation = ", sum(data))
print("Average = ", sum(data)/len(data))
print("Maximum = ", max(data))
print("Minimum = ", min(data))