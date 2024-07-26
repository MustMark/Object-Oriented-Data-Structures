def reverse_sort(input_list, length=0, cur=0):
    if length == len(input_list):
        return input_list
    else:
        if cur+1 < len(input_list):
            if input_list[cur] < input_list[cur+1]:
                input_list[cur], input_list[cur+1] = input_list[cur+1],input_list[cur]
            return reverse_sort(input_list, length,cur+1)
        else:
            return reverse_sort(input_list, length+1)

input_list = [int(i) for i in input("Enter your List : ").split(",")]

print(f"List after Sorted : {reverse_sort(input_list)}")