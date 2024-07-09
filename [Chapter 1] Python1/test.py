print("*** Fun with permute ***")
origin_list = [int(i) for i in (input("input : ")).split(",")]
print("Original Cofllection: ", origin_list)
print("Collection of distinct numbers:")
temp_arr = []
result = []

def distributing(focus_index = 0) :
    if focus_index == len(origin_list) - 1 :
        for i in range(len(temp_arr) + 1) :
            temp_arr.insert(i, origin_list[focus_index])
            result.append(temp_arr.copy())
            temp_arr.pop(i)
            print(result)
        return
    else :
        for i in range(len(temp_arr) + 1) :
            temp_arr.insert(i, origin_list[focus_index])
            distributing(focus_index + 1)
            temp_arr.pop(i)
            print("break")

distributing()
print("", result)