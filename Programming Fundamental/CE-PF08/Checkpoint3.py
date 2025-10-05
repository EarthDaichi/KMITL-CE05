def Question():
    day = (input("Enter your OT day : "))
    hr = int(input("Enter your OT time : "))
    wc = int(input("Enter your wage : "))
    return day,hr,wc

def calculate():
    day,hr,wc = list(Question())
    if((day == "Sunday") or (day =="sunday")):wage = wc * hr * 3
    else:wage = wc * hr * 1.5
    print(f"Your OT wage = {wage}")

print(f"{"*"*8} OverTime Wage Calculator {"*"*8}")
print("-"*42)
calculate()
