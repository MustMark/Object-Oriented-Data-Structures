def find_max(num_list, max = None):
    if num_list:
        if max == None:
            max = int(num_list[-1])
        elif int(num_list[-1]) > int(max):
            max = num_list[-1]
        num_list.pop()
        return find_max(num_list, max)
    else:
        return max

num_list = input("Enter Input : ").split(" ")
print(find_max(num_list))