class BST:
    class BSTNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
        
        def __str__(self):
            return str(self.data)
        
    def __init__(self):
        self.root = None

    def insert(self, node, data):
        data = int(data)
        if self.root == None:
            self.root = self.BSTNode(data)
        else:
            if node == None:
                return self.BSTNode(data)
            elif data < node.data:
                node.left = self.insert(node.left, data)
            else:
                node.right = self.insert(node.right, data)
        return node
    
    def search_subtree(self, root, key):
        if root == None:
            return None
        else:
            if key == root.data:
                return root
            elif key < root.data:
                return self.search_subtree(root.left, key)
            else:
                return self.search_subtree(root.right, key)
    
    def delete_subtree(self, root, key):
        if root == None:
            return None
        else:
            if root.data == key:
                return None  
            elif key < root.data:
                root.left = self.delete_subtree(root.left, key)
            else:
                root.right = self.delete_subtree(root.right, key)
        return root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print("    " * level + str(node.data))
            self.printTree(node.left, level + 1)

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
            if data < root.right.data:
                root.right = AVLTree.rotateRightChild(root.right)
            return AVLTree.rotateLeftChild(root)
        elif balance < -1:
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

    def inorder_traversal(self, root):
        if root is None:
            return []
        return (self.inorder_traversal(root.left) + [root.data] + self.inorder_traversal(root.right))
    
    def bst_to_avl(self, root):
        inorder_data = self.inorder_traversal(root)

        for data in inorder_data:
            self.insert(data)

    def printTree(self, node, level = 0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print("    " * level + str(node.data))
            self.printTree(node.left, level + 1)


inp1, inp2 = input("Enter the val of tree and node to cut: ").split("/")
bst = BST()
for i in inp1.split():
    bst.insert(bst.root, int(i))
print("Before cut:")
bst.printTree(bst.root)

avl1, avl2 = AVLTree(), AVLTree()

print("Cutted Tree:")
subtree_root = bst.search_subtree(bst.root, int(inp2))
avl1.bst_to_avl(subtree_root)
avl1.printTree(avl1.root)

print("Left Tree:")
bst.root = bst.delete_subtree(bst.root, int(inp2))
avl2.bst_to_avl(bst.root)
avl2.printTree(avl2.root)