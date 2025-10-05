n = int(input("Enter count of numbers you want to find summation : "))
n_list = []
for i in range(n):
    n_list.append(int(input(f"Enter {i+1}. Number :")))

def find_sum(n_list,n):
    if(n == 0):return 0
    else:
        sum = n_list[n-1] + find_sum(n_list,n-1)
        return sum
print(find_sum(n_list,n))