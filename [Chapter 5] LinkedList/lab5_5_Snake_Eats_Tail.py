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
    
    def __str__(self):
        baby = False
        output = "("
        current_node = self.head
        output += str(current_node.data) + ")"
        while current_node.next != None:
            baby = True
            current_node = current_node.next
            output += "->"
            output += str(current_node.data)
        if not baby:
            output += "->Empty"
        return output

    def have_baby(self):
        return self.head.next is not None
    
    def reverse(self):
        temp_linked_list = LinkedList()
        current_node = self.head
        while current_node:
            temp_linked_list.add_head(Node(current_node.data))
            current_node = current_node.next
        return temp_linked_list
    
    def swap_head_tail(self):
        old_head_next = self.head.next
        current_node = self.head
        while current_node.next != None:
            if current_node.next.next == None:
                old_tail = current_node.next
                current_node.next = self.head
                current_node.next.next = None
                self.head = old_tail
                self.head.next = old_head_next
            current_node = current_node.next
    
    def swap_baby(self):
        previous_node = self.head
        current_node = self.head.next
        while current_node != None:
            if current_node.next != None:
                temp_next_node = current_node.next.next
                previous_node.next = current_node.next
                current_node.next.next = current_node
                current_node.next = temp_next_node
                previous_node = current_node
                current_node = current_node.next
            else:
                previous_node.next = None
                return

    def delete_bigger(self):
        output = "["
        previous_node = self.head
        current_node = self.head.next
        while current_node != None:
            if int(current_node.data) > int(self.head.data):
                if output == "[":
                    output += str(current_node.data)
                else:
                    output += ", " + str(current_node.data)
                previous_node.next = current_node.next
                current_node = current_node.next
            else:
                previous_node = current_node
                current_node = current_node.next
        output += "]"
        return output
    
    def compare_data(self, reverse_line, num):
        output = "]"
        current_node = reverse_line.head
        while current_node.next != None:
            if int(current_node.data) == 0 or int(num) % int(current_node.data) != 0:
                output += " ," + str(current_node.data)
                reverse_line.head = current_node.next
            else:
                output += "["
                self.head = reverse_line.reverse().head
                if output != "][":
                    output = output[0] + output[3::]
                return output[::-1]
            current_node = current_node.next
        self.swap_head_tail()
        return "[]"

snake_game = True
while snake_game:     
    input_snake_family, input_play = input("Snake Game : ").split("/")
    snake_family = input_snake_family.split(" ")
    play_list = input_play.split(",")

    line = LinkedList()

    for snake in snake_family:
        line.append(snake)

    print(line)

    for play in play_list:
        if play == "SW":
            line.swap_baby()
            print(f"Swap success!")
        elif play == "SH":
            output = line.delete_bigger()
            print(f"Shake success!->{output}")
        elif play[0] == "F":
            char, num = play.split(" ")
            line.append(num)
            print(f"Steal success!->{num}")
        elif play[0] == "D":
            char, num = play.split(" ")
            output = line.compare_data(line.reverse(), num)
            print(f"Play success!->{output}")
        print(line)
        print(f"------------------------------")
        if not line.have_baby():
            print("Mom is dead")
            break