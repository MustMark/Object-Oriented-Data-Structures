do = input("Enter Input : ").split(",")
queue  = []

for i in do:
    if len(i) > 1:
        char, num = i.split(" ")
        queue.append(num)
        print(f"Add {num} index is {len(queue)-1}")
    else:
        if len(queue) != 0:
            print(f"Pop {queue.pop(0)} size in queue is {len(queue)}")
        else:
            print(-1)

if len(queue) == 0:
    print("Empty")
else:
    print(f"Number in Queue is :  {queue}")