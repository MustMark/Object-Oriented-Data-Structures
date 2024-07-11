do = input("Enter Input : ").split(",")
stack = []

for i in do:
    if len(i) > 1:
        char, num = i.split(" ")
        stack.append(num)
        print(f"Add = {num} and Size = {len(stack)}")
    else:
        if len(stack) != 0:
            print(f"Pop = {stack.pop()} and Index = {len(stack)}")
        else:
            print(-1)

if len(stack) == 0:
    print("Value in Stack = Empty")
else:
    val = " ".join(stack)
    print(f"Value in Stack = {val}")