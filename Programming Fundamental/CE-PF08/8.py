def FutureValue(P,R,n):
    FV = P*((1+R/100)**n)
    return FV
def collect_data():
    P = int(input("Enter Principal : "))
    R = int(input("Enter Rate (%): "))
    n = int(input("Enter Investment time (Years) : "))
    return (FutureValue(P,R,n))

print(f" FV = {collect_data():.2f}")