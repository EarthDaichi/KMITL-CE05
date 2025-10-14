import random as rd

data = [rd.randint(1,50) for i in range(20)]
print("Display 1st time = ", data)
print("Display 2nd time = ", sorted(data))
print("Summation = ", sum(data))
print("Average = ", sum(data)/len(data))
print("Maximum = ", max(data))
print("Minimum = ", min(data))