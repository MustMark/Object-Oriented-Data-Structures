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
    
    def append(self, data):
        if self.isEmpty():
            self.head = Node(data)
            return
        if self.head.data == "|":
            self.add_head(Node(data))
        else:
            previous_node = self.head
            current_node = self.head.next
            while current_node.data != "|":
                previous_node = current_node
                current_node = current_node.next
            previous_node.next = Node(data)
            previous_node.next.next = current_node

    def swap_cursor_left(self):
        if self.head.data == "|":
            return
        else:
            previous_node = self.head
            current_node = self.head.next
            while current_node.data != "|":


    def swap_cursor_right(self):
        pass

    def delete_left(self):
        pass

    def delete_right(self):
        pass

    def isEmpty(self):
        return self.head is None
    
    def __str__(self):
        output = ""
        current_node = self.head
        output += current_node.data
        while current_node.next != None:
            current_node = current_node.next
            output += " "
            output += current_node.data
        return output

command_list = input("Enter Input : ").split(",")

text = LinkedList(Node("|"))

for command in command_list:
    if len(command) > 1:
        mode, word = command.split(" ")
        text.append(word)
    elif command == "L":
        text.swap_cursor_left()
    elif command == "R":
        text.swap_cursor_right()
    elif command == "B":
        text.delete_left()
    elif command == "D":
        text.delete_right()
    print(text)