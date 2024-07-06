num_list = [int(i) for i in input("Enter Your List : ").split(" ")]
size = len(num_list)
ans_list = []

if size < 3:
    print("Array Input Length Must More Than 2")
else:
    for num1 in range(size):
        for num2 in range(num1+1, size):
            for num3 in range(num2+1, size):
                temp_list = [num_list[num1], num_list[num2], num_list[num3]]
                if sum(temp_list) == 5 and temp_list not in ans_list:
                    ans_list.append(temp_list)
    ans_set = set(tuple(sorted(ans)) for ans in ans_list)
    print([list(ans) for ans in ans_set])