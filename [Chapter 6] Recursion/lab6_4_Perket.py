def perket(sweet_list, bitter_list, index = 0, number = 0, s = 1, b = 0):
    if index == len(perket_items_list):
        if number != 0:
            return [abs(b-s)]
        return []
    
    sum_s = s * int(sweet_list[index])
    sum_b = b + int(bitter_list[index])
    
    in_loop = perket(sweet_list, bitter_list, index + 1, number, s, b)
    out_loop = perket(sweet_list, bitter_list, index + 1, number + 1, sum_s, sum_b)

    return in_loop + out_loop

perket_items_list = input("Enter Input : ").split(",")

sweet_list = []
bitter_list = []

for perket_items in perket_items_list:
    sweet, bitter = perket_items.split()
    sweet_list.append(sweet)
    bitter_list.append(bitter)

print(min(perket(sweet_list, bitter_list)))