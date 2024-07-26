def new_print(i, count, num):
    if count <= num:
        if i < count:
            print(chr(i),end="")
            new_print(i+1, count, num)
        elif i == count:
            print(chr(i))
            new_print(i+1, count, num)
        else:
            new_print(ord("A"), count+1, num)
    elif ord("A") < num < count:
        if i < num-1:
            print(chr(i),end="")
            new_print(i+1, count, num)
        elif i == num-1:
            print(chr(i))
            new_print(i+1, count, num)
        else:
            new_print(ord("A"), count, num-1)

char = input("Enter input: ")

new_print(ord("A"), ord("A"), ord(char.upper()))