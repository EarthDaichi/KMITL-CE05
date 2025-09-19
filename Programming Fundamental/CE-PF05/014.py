letter = 'y'
while(letter != 'n'):
    print('----- This is rectilinear motion calculation -----')
    print('Press A: v = s/t')
    print('Press B: v = u + a*t')
    choice = input("Select menu: ")
    if(choice == 'A'):
        s = float(input("Enter distance (meter) : "))
        t = float(input("Enter time in second : "))
        v = s/t
        print('Velocity (v) = ', v, "m/s")
    elif(choice == 'B'):
        u = float(input("Enter initial velocity (m/s) : "))
        a = float(input("Enter acceleration (m/s^2) : "))
        t = float(input("Enter time in second : "))
        v = u+(a*t)
        print('Velocity (v) = ', v ,'m/s')
    else:
        print('please, select A or B')
    letter = input("Press any letter to continue, n = terminated : ")