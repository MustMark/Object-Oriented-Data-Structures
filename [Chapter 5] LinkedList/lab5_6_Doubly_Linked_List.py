class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.isEmpty():
            new_node = Node(item)
            self.head = new_node
            self.tail = new_node
        else:
            new_tail = Node(item)
            self.tail.next = new_tail
            new_tail.previous = self.tail
            self.tail = new_tail

    def addHead(self, item):
        if self.isEmpty():
            new_node = Node(item)
            self.head = new_node
            self.tail = new_node
        else:
            old_head = self.head
            self.head = Node(item)
            self.head.next = old_head
            old_head.previous = self.head

    def insert(self, pos, item):
        if self.isEmpty():
            new_node = Node(item)
            self.head = new_node
            self.tail = new_node
            return
        count = 0
        if pos >= 0:
            current_node = self.head
            while current_node.next != None:
                if count == pos:
                    new_node = Node(item)
                    previous_node = current_node.previous
                    previous_node.next = new_node
                    new_node.previous = previous_node
                    current_node.previous = new_node
                    new_node.next = current_node
                    return
                count += 1
                current_node = current_node.next
            self.append(item)
        else:
            current_node = self.tail
            while current_node.previous != None:
                if count == pos + 1:
                    new_node = Node(item)
                    previous_node = current_node.previous
                    previous_node.next = new_node
                    new_node.previous = previous_node
                    current_node.previous = new_node
                    new_node.next = current_node
                    return
                count -= 1
                current_node = current_node.previous
            self.addHead(item)

    def search(self, item):
        current_node = self.head
        while current_node.next != None:
            if current_node.value == item:
                return "Found"
            current_node = current_node.next
        return "Not Found"

    def index(self, item):
        count = 0
        current_node = self.head
        while current_node.next != None:
            if current_node.value == item:
                return count
            count += 1
            current_node = current_node.next
        return -1

    def size(self):
        if self.head == None:
            return 0
        else:
            count = 1
            current_node = self.head
            while current_node.next != None:
                count += 1
                current_node = current_node.next
            return count

    def pop(self, pos):
        if self.isEmpty():
            return "Out of Range"
        count = 0
        current_node = self.head
        if count == pos and self.size() == 1:
            self.head = None
            return "Success"
        while current_node.next != None:
            if count == pos:
                previous_node = current_node.previous
                next_node = current_node.next
                previous_node.next = next_node
                next_node.previous = previous_node
                return "Success"
            count += 1
            current_node = current_node.next
        return "Out of Range"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())