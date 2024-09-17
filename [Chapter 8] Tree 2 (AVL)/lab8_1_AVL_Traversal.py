class AVLTree:
    class AVLNode:
        def __init__(self, data, left = None, right = None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = self.setHeight()

        def __str__(self):
            return str(self.data)

        def setHeight(self):
                a = self.getHeight(self.left)
                b = self.getHeight(self.right)

                self.height = 1 + max(a,b)

                return self.height     

        def getHeight(self, node):
            return -1 if node == None else node.height

        def balanceValue(self):      
            return self.getHeight(self.right) - self.getHeight(self.left)
        

    def __init__(self, root = None):
        self.root = None if root is None else root

    def add(self, data):
        data = int(data)
        if self.root == None:
            self.root = AVLTree.AVLNode(data)
        else:
            AVLTree._add(self.root, data)

    def _add(root, data):
        current_node = root
        while True:
            if data < current_node.data:
                if current_node.left == None:
                    current_node.left = AVLTree.AVLNode(data)
                    break
                else:
                    current_node = current_node.left
            elif data >= current_node.data:
                if current_node.right == None:
                    current_node.right = AVLTree.AVLNode(data)
                    break
                else:
                    current_node = current_node.right

    def rotateLeftChild(root):
        pass

    def rotateRightChild(root):
        pass

    def postOrder(self):
        pass

    def _postOrder(root):
        pass

    def printTree(self):
        AVLTree._printTree(self.root)
        print()

    def _printTree(node , level=0):
        if not node is None:
            AVLTree._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            AVLTree._printTree(node.left, level + 1)


avl1 = AVLTree()

inp = input('Enter Input : ').split(',')

for i in inp:

    if i[:2] == "AD":

        avl1.add(i[3:])

    elif i[:2] == "PR":

        avl1.printTree()

    elif i[:2] == "PO":

        avl1.postOrder()