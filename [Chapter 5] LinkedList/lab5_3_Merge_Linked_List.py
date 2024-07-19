class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def add_head(self, head):
        head.next = self.head
        self.head = head

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

l = [[],[]]

inp_list = input("Enter Input (L1,L2) : ").split(" ")

for i in range(len(inp_list)):
    inp_list_split = inp_list[i].split("->")
    l[i] = LinkedList(Node(inp_list_split[0]))
    current_node = l[i].head
    for i in range(1, len(inp_list_split)):
        current_node.next = Node(inp_list_split[i])
        current_node = current_node.next

print(f"L1    : {l[0]}")
print(f"L2    : {l[1]}")

l[1].reverse()

print(f"Merge : {l[0]} {l[1]}")