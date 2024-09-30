def first_greater(index, length, left, right_value):
    if index > length:
        return "No First Greater Value"
    if left[index] > right_value:
        return left[index]
    else:
        return first_greater(index + 1, length, left, right_value)

inp = input('Enter Input : ').split('/')
left, right = list(map(int, inp[0].split())), list(map(int, inp[1].split()))
for i in right:
    print(first_greater(0, len(left) - 1,sorted(left), i))