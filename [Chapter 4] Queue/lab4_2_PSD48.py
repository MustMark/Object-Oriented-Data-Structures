do = input("Enter Input : ").split(",")
queue  = []

for i in do:
    if len(i) > 1:
        char, num = i.split(" ")
        if char == "EN":
            queue.append([char, num])
        else:
            temp_queue = []
            while queue and queue[-1][0] == "EN":
                temp_queue.append(queue.pop())
            queue.append([char, num])
            while temp_queue:
                queue.append(temp_queue.pop())
    else:
        if queue:
            print(queue.pop(0)[1])
        else:
            print("Empty")