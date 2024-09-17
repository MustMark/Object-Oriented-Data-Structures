def somethingDROME(numbers):
    increase = False
    decrease = False
    same = False
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            decrease = True
        elif numbers[i] < numbers[i+1]:
            increase = True
        else:
            same = True
    if increase and not decrease:
        if same:
            return "Plaindrome"
        else:
            return "Metadrome"
    elif not increase and decrease:
        if same:
            return "Nialpdrome"
        else:
            return "Katadrome"
    elif not increase and not decrease and same:
        return "Repdrome"
    else:
        return "Nondrome"

inp = [int(i) for i in input("Enter Input : ")]
print(somethingDROME(inp))