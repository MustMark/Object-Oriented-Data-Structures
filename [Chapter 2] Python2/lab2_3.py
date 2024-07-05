def odd_even(type, data, mode):
    if type == "S":
        if mode == "Odd":
            print(data[::2])
        else:
            print(data[1::2])
    else:
        old_list = data.split(" ")
        new_list = []
        if mode == "Odd":
            for i in old_list[::2]:
                new_list.append(i)
            print(new_list)
        else:
            for i in old_list[1::2]:
                new_list.append(i)
            print(new_list)
            
print("*** Odd Even ***")
input_1,input_2,input_3 = input("Enter Input : ").split(",")
odd_even(input_1,input_2,input_3)