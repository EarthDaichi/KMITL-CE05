def Distance(a,b):
    d = a-b
    if d < 0:
        d = -d
    return d

a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
print(f"Distance = {Distance(a,b)}")