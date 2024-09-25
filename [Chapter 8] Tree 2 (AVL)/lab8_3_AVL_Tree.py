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

    def insert(self, data):
        data = int(data)
        if self.root == None:
            self.root = AVLTree.AVLNode(data)
        else:
            self.root = AVLTree._insert(self.root, data)

    def _insert(root, data):
        if root is None:
            return AVLTree.AVLNode(data)
        elif data < root.data:
            root.left = AVLTree._insert(root.left, data)
        else:
            root.right = AVLTree._insert(root.right, data)
        
        root.setHeight()
        balance = root.balanceValue()
        
        if balance > 1:
            print("Left Left Rotation")
            if data < root.right.data:
                root.right = AVLTree.rotateRightChild(root.right)
            return AVLTree.rotateLeftChild(root)
        elif balance < -1:
            print("Right Right Rotation")
            if data >= root.left.data:
                root.left = AVLTree.rotateLeftChild(root.left)
            return AVLTree.rotateRightChild(root)
        return root

    def rotateLeftChild(root):
        right = root.right
        if right == None:
            return root
        root.right = right.left
        right.left = root
        root.setHeight()
        right.setHeight()
        return right

    def rotateRightChild(root):
        left = root.left
        if left == None:
            return root
        root.left = left.right
        left.right = root
        root.setHeight()
        left.setHeight()
        return left

    def postOrder(self):
        print("AVLTree post-order : ", end="")
        AVLTree._postOrder(self.root)
        print()

    def _postOrder(root):
        if not root is None:
            AVLTree._postOrder(root.left)
            AVLTree._postOrder(root.right)
            print(root.data, end=" ")

    def printTree(self):
        AVLTree._printTree(self.root)

    def _printTree(node , level=0):
        if not node is None:
            AVLTree._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            AVLTree._printTree(node.left, level + 1)


myTree = AVLTree() 
root = None

print(" *** AVL Tree Insert Element ***")
data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    myTree.insert(e)
    myTree.printTree()
    print("====================")