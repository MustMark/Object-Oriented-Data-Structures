inp = [int(i) for i in input("Enter Input : ").split(" ")]
check = True
for i in range(len(inp) - 1):
    if not inp[i] < inp[i+1]:
        print("No")
        check = False
        break

if check:
    print("Yes")