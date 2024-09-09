def print_binary(num, i = 0):
    if int(num) < 0:
        print("Only Positive & Zero Number ! ! !")
    elif i > 2**num - 1:
        return
    else:
        print(f"{bin(i)[2:]:0>{num}}")
        print_binary(num, i+1)

num = input("Enter Number : ")
print_binary(int(num))