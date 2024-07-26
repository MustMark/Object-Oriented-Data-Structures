def perket(item_list, result=[], i=0, j=0):
    j = i+1
    if i == len(item_list) - 1:
        return min(result)
    else:
        if j == len(item_list) - 1:
            s1, b1 = item_list[i].split(" ")
            s2, b2 = item_list[i+1].split(" ")
            sweet = int(s1) * int(s2)
            bitter = int(b1) + int(b2)
            result.append(abs(sweet-bitter))
        if j == len(item_list):
            return perket(item_list, result, i, j+1)
        else:
            return perket(item_list, result, i+1)


item_list = input("Enter Input : ").split(",")

print(perket(item_list))