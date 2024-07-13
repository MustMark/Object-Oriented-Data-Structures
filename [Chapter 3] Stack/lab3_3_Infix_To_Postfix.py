class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return not self.items

convert = {"(" : 0, "+" : 1, "-" : 1, "*" : 2, "/" : 2, "^" : 3}
inp = input("Enter Infix : ")

stack = Stack()

print("Postfix : ", end="")

for i in inp:
    if i  == "(":
        stack.push(i)
    elif i == ")":
        last = stack.pop()
        while last != "(":
            print(last, end="")
            last = stack.pop()
    elif i in "+-*/^":
        if not stack.isEmpty() and convert[i] < convert[stack.peek()]:
            while not stack.isEmpty() and stack.peek() != "(":
                print(stack.pop(), end="")
        elif not stack.isEmpty() and convert[i] == convert[stack.peek()]:
            print(stack.pop(), end="")
        stack.push(i)
    else:
        print(i, end="")

while not stack.isEmpty():
    print(stack.pop(), end="")