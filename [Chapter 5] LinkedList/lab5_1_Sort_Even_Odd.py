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
    
    def isEmpty(self):
        return self.head is None
    
    def merge(self, linked_list):
        if self.isEmpty():
            self.head = linked_list.head
            return
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = linked_list.head

    def __str__(self):
        output = "["
        current_node = self.head
        output += str(current_node.data)
        while current_node.next != None:
            current_node = current_node.next
            output += ", "
            output += str(current_node.data)
        output += "]"
        return output
    
inp = input("Enter the numbers list: ").split(" ")

even = LinkedList()
odd = LinkedList()

for i in inp:
    i = int(i)
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

even.merge(odd)

print(f"Rearranged list: {even}")