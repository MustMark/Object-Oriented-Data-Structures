class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            current_node = self.root
            while True:
                if data < current_node.data:
                    if current_node.left == None:
                        current_node.left = Node(data)
                        return self.root
                    else:
                        current_node = current_node.left
                elif data >= current_node.data:
                    if current_node.right == None:
                        current_node.right = Node(data)
                        return self.root
                    else:
                        current_node = current_node.right
        return self.root

    def find_below(self, number, current_node):
        result = []

        if current_node.left != None:
            result.extend(self.find_below(number, current_node.left))

        if current_node.data < number:
            result.append(current_node.data)

        if current_node.right != None:
            result.extend(self.find_below(number, current_node.right))

        return result
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
inp, number = input('Enter Input : ').split("|")
tree = inp.split()

for i in tree:
    root = T.insert(int(i))

T.printTree(root)

print("--------------------------------------------------")

result = T.find_below(int(number), root)

print(f"Below {number} :", end=" ")

if result == []:
    print("Not have")
else:
    for i in result:
        print(i, end=" ")