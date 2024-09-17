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

def median(numbers):
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n//2]
    else:
        return (numbers[(n//2)-1] + numbers[n//2])/2

l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "quick sort"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    number_list = []
    for i in l:
        number_list.append(i)
        median_index = (len(number_list)+1)/2
        print(f"list = {number_list} : median = {median(bubble_sort(number_list.copy())):.1f}")