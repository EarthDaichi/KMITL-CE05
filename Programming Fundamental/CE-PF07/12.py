bill,hour,min = list(map(int,input("Enter bill , park hours and minutes :").split(",")))
if(0<min<=60):
    hour+=1
if(bill >= 1000):
    if(hour>4):
        print(f"parking cost = {(hour-4) *30}")
    else:
        print("Free parking cost")
else:
    if(hour>2):
        print(f"parking cost = {(hour-2) *30}")
    else:
        print("Free parking cost")
