class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def append(self, data):
        if self.isEmpty():
            self.head = Node(data)
            return
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = Node(data)

    def add_head(self, head):
        head.next = self.head
        self.head = head

    def isEmpty(self):
        return self.head is None
    
    def go(self, source, destination):
        output = ""
        current_node = self.head
        count = -1
        while current_node != None:
            if current_node.data == source:
                output += current_node.data
                output += "->"
                count = 0
            elif current_node.data != destination and count >= 0:
                output += current_node.data
                output += "->"
                count += 1
            elif current_node.data == destination and count >= 0:
                output += current_node.data
                count += 1
                return output + "," + str(count)
            
            if current_node.next is None:
                current_node = self.head
            else:
                current_node = current_node.next

    def __str__(self):
        output = ""
        current_node = self.head
        output += current_node.data
        while current_node.next != None:
            current_node = current_node.next
            output += " "
            output += current_node.data
        return output
    
    def reverse(self):
        temp_linked_list = LinkedList()
        current_node = self.head
        while current_node:
            temp_linked_list.add_head(Node(current_node.data))
            current_node = current_node.next
        self.head = temp_linked_list.head

print("***Railway on route***")
station_list, inp2 = input("Input Station name/Source, Destination, Direction(optional): ").split("/")
inp2_list = inp2.split(",")

if len(inp2_list) > 2:
    source, destination, direction = inp2_list[0],inp2_list[1],inp2_list[2]
else:
    source, destination = inp2_list[0],inp2_list[1]
    direction = "X"

station_link = LinkedList()
station_list_split = station_list.split(",")

for station in station_list_split:
    station_link.append(station)
    
if direction == "F":
    print(f"Forward Route: {station_link.go(source, destination)}")
elif direction == "B":
    station_link.reverse()
    print(f"Backward Route: {station_link.go(source, destination)}")
else:
    forward, forward_count = station_link.go(source, destination).split(",")
    station_link.reverse()
    backward, backward_count = station_link.go(source, destination).split(",")
    if int(forward_count) < int(backward_count):
        print(f"Forward Route: {forward},{forward_count}")
    elif int(forward_count) > int(backward_count):
        print(f"Backward Route: {backward},{backward_count}")
    else:
        print(f"Forward Route: {forward},{forward_count}")
        print(f"Backward Route: {backward},{backward_count}")