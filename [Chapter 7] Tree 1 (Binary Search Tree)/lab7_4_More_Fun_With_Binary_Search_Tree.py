class Node:
    def __init__(self, data,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def append(self, data):
        pass

    def cut(self, data):
        pass
                    
    def preorder(self, node,stop):
        pass

    def inorder(self, node,stop):
        pass

    def postorder(self, node,stop):
        pass
            
    def printMirrorTree(self, node, level=0):
        pass

    def printTree(self, node, level=0):
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