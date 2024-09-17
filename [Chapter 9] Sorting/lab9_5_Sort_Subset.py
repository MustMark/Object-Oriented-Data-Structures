def bubble_sort(numbers):
    for last in range(len(numbers) - 1, 0, -1):
        swapped = False
        for i in range(last):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True
        if not swapped:
            break
    return numbers

def subset_sort(subset_list):
    for last in range(len(subset_list) - 1, 0, -1):
        swapped = False
        for i in range(last):
            if len(subset_list[i]) > len(subset_list[i+1]):
                subset_list[i], subset_list[i+1] = subset_list[i+1], subset_list[i]
                swapped = True
        if swapped is False:
            break
    return subset_list

def find_subset(target, numbers, index = 0, result = None, current_subset = None):  
    if result is None:  
        result = []
    if current_subset is None:
        current_subset = []
    if index >= len(numbers):    
        return result
    current_subset.append(numbers[index])
    if sum(current_subset) == target:  
        result.append(current_subset.copy())

    result = find_subset(target, numbers, index + 1, result, current_subset) 
    current_subset.pop()
    result = find_subset(target, numbers, index + 1, result, current_subset)
    return result

inp_target, inp_number = input("Enter Input : ").split("/")
target = int(inp_target)
number_list = [int(i) for i in inp_number.split(" ")]

result = find_subset(target, bubble_sort(number_list))

if result:
    for subset in subset_sort(result):
        print(subset)
else:
    print("No Subset")