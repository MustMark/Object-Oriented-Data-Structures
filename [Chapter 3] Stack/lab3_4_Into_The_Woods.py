class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return ""

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return ""

    def isEmpty(self):
        return not(self.items)

    def size(self):
        return len(self.items)

stack = Stack()
do = input('Enter Input : ').split(',')

for i in do:
    if len(i) > 1:
        char, num = i.split(" ")
        stack.push(int(num))
    else:
        count = 0
        temp_stack = Stack()
        if not stack.isEmpty():
            highest = stack.pop()
            temp_stack.push(highest)
            count += 1
        while not stack.isEmpty():
            temp_item = stack.pop()
            if temp_item > highest:
                highest = temp_item
                count += 1
            temp_stack.push(temp_item)
        print(count)
        while not temp_stack.isEmpty():
            stack.push(temp_stack.pop())