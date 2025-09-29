status = str(input("Traffic Status : "))
distance = float(input("travel distance : "))
if(status == "low"):
    cost = distance * 10
elif(status == "medium"):
    cost = distance * 12
elif(status == "high"):
    cost = distance * 15
else:print("Error")
print(f"Traffic is {status} travle cost = {cost}")