print("******** Parking Lot ********")
max, soi, operation, car = input("Enter max of car,car in soi,operation : ").split(" ")

soi_list = [int(i) for i in soi.split(",")]
car = int(car)

if 0 in soi_list:
    soi_list = []

if operation == "arrive":
    if len(soi_list) >= int(max):
        print(f"car {car} cannot arrive : Soi Full")
    elif car in soi_list:
        print(f"car {car} already in soi")
    else:
        soi_list.append(car)
        print(f"car {car} arrive! : Add Car {car}")
else:
    if not soi_list:
        print(f"car {car} cannot depart : Soi Empty")
    elif car not in soi_list:
        print(f"car {car} cannot depart : Dont Have Car {car}")
    else:
        temp_soi = []
        last_car = soi_list.pop()
        while last_car != car:
            temp_soi.append(last_car)
            last_car = soi_list.pop()
        print(f"car {car} depart ! : Car {car} was remove")
        while temp_soi:
            soi_list.append(temp_soi.pop())
print(soi_list)