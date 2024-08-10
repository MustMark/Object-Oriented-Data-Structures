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
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)