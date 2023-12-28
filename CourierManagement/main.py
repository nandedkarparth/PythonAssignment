import Users as U, Courier as C, Employee as E, Location as L, CourierCompany as CC, Payment as P

print("--------Main Menu----------")
print("1.Courier\n2.Add Entity\n3.Remove Entity\n4.Get Details")

while True:
    print("------------------------------------------------------")
    ch = int(input("Enter your choice for main menu : "))
    if ch == 1:
        print("")
    elif ch == 2:
        print("1.Add User\n2.Add Employee\n3.Add Location")
        ch2 = int(input("Enter your choice : "))
        if ch2 == 1:
            U.Users('x')
        elif ch2 == 2:
            E.Employee('x')
        elif ch2 == 3:
            L.Location('x')
        else:
            print("Enter valid choice!!")
    elif ch == 3:
        pass
    elif ch == 4:
        print("1.Users\n2.Couriers\n3.Employees\n4.Location\n5.Courier Services\n6.Payments")
        ch2 = int(input("Enter your choice : "))
        if ch2 == 1:
            id = int(input("Enter User ID : "))
            U.Users(id).get_info()
        elif ch2 == 2:
            id = int(input("Enter CourierID : "))
            C.Courier(id).get_info()
        elif ch2 == 3:
            id = int(input("Enter Employee ID : "))
            E.Employee(id).get_info()
        elif ch2 == 4:
            id = int(input("Enter Location ID : "))
            L.Location(id).get_info()
        elif ch2 == 5:
            id = int(input("Enter Courier Sevice ID : "))
            CC.CourierCompany(id).get_info()
        elif ch2 == 6:
            id = int(input("Enter Payment ID : "))
            P.Payment(id).get_info()
        else:
            print("Enter valid choice!!")

    elif ch == 0:
        exit(0)
    else:
        print("Enter valid choice!")