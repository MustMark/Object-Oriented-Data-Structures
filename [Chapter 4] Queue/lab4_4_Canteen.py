people_list, do_list = input("Enter Input : ").split("/")
people = people_list.split(",")
people_dict = {}
queue = []

do = do_list.split(",")

for i in do:
    if len(i) > 1:
        group, id = i.split(" ")
        queue_count = len(queue)
        if not queue:
            queue.append(id)
        else:
            temp_queue = []
            while queue and queue[-1][0] != id[0]:
                temp_queue.append(queue.pop())
            if queue_count == len(temp_queue):
                while temp_queue:
                    queue.append(temp_queue.pop())
                queue.append(id)
            else:
                queue.append(id)
                while temp_queue:
                    queue.append(temp_queue.pop())
    else:
        if queue:
            print(queue.pop(0))
        else:
            print("Empty")