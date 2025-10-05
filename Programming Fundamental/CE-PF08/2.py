n = int(input("Enter count of number to square : "))
listA = []
for i in range(n):
    listA.append(int(input(f"Enter {i+1} Number : ")))
def Square(listA):
    for i in range(len(listA)):
        listA[i] = listA[i]*listA[i]
    print(listA)
Square(listA)