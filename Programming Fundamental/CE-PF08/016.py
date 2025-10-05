def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

num = int(input("Enter integer number >> "))

print('Fibonacci sequence: ')
for i in range(num):
    print(fibonacci(i), end = ', ')