class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
    
    def new_ord(self, data):
        if len(data) == 1:
            return ord(data)
        else:
            return int("".join([str(ord(i)) for i in data]))

    def new_print(self, node_data, stop):
        if node_data <= stop:
            print(self.new_ord(node_data), end = " ")
        else:
            print(node_data, end = " ")

    def append(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            current_node = self.root
            while True:
                if data < current_node.data:
                    if current_node.left == None:
                        current_node.left = Node(data)
                        return
                    else:
                        current_node = current_node.left
                elif data >= current_node.data:
                    if current_node.right == None:
                        current_node.right = Node(data)
                        return
                    else:
                        current_node = current_node.right

    def cut(self, data, current_node = None):
        if current_node == None:
            current_node = self.root
        if current_node.data == data:
            if current_node.right != None:
                current_node.right = None
            elif current_node.left != None:
                current_node.left = None
            else:
                print("Not thing change")
            return
        else:
            if current_node.left != None:
                self.cut(data, current_node.left)
            if current_node.right != None:
                self.cut(data, current_node.right)
            return
                    
    def preorder(self, node, stop):
        if node != None:
            self.new_print(node.data, stop)
            self.preorder(node.left, stop)
            self.preorder(node.right, stop)

    def inorder(self, node, stop):
        if node != None:
            self.inorder(node.left, stop)
            self.new_print(node.data, stop)
            self.inorder(node.right, stop)

    def postorder(self, node, stop):
        if node != None:
            self.postorder(node.left, stop)
            self.postorder(node.right, stop)
            self.new_print(node.data, stop)
            
    def printMirrorTree(self, node, level = 0):
        if node != None:
            self.printMirrorTree(node.left, level + 1)
            print('     ' * level, node)
            self.printMirrorTree(node.right, level + 1)

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
print("What is this a plum tree")
first,inp = input('Enter Input : ').split('/')
first = first.split()
for i in first:
    T.append(i)
print("FIrst look of this plum tree")
T.printTree(T.root)
print("********************************************")
inp = inp.split(',')
for i in inp:
    print(i)
    if i[:2] == "AP":
        T.append(i[3:])
        T.printTree(T.root)
    elif i[:2] == "CU":
        T.cut(i[3:])
        T.printTree(T.root)
    elif i[:2] == "CH":
        print('preorder  :',end=' ')
        T.preorder(T.root,i[3:])
        print('\ninorder   :',end=' ')
        T.inorder(T.root,i[3:])
        print('\npostorder :',end=' ')
        T.postorder(T.root,i[3:])
        print()
    elif i[:2] == "MI":
        T.printMirrorTree(T.root)
    print("********************************************")
print("the last result")
T.printTree(T.root)