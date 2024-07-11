print("*** Fun with Drawing ***")

num = input("Enter input : ")
size = ((int(num)-1)*4)+1

for row in range(size):
    for col in range(size):
        top = row%2 ==0 and row <= col <= size-1-row
        bottom = row%2 == 0 and size-1-row <= col <= row
        left = col%2 == 0 and col <= row <= size-1-col
        right = col%2 == 0 and size-1-col  <= row <= col
        if top or bottom or left or right:
            print("#", end="")
        else:
            print(".", end="")
    print()