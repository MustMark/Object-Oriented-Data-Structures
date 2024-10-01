class AVLTree:
    class AVLNode:
        def __init__(self, data, parent = None, left = None, right = None):
            self.data = data
            self.parent = parent
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

    def _insert(root, data, parent = None):
        if root is None:
            return AVLTree.AVLNode(data, parent)
        elif data < root.data:
            root.left = AVLTree._insert(root.left, data, root)
        else:
            root.right = AVLTree._insert(root.right, data, root)
        
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
        right.parent = root.parent
        if root.parent is not None:
            if root == root.parent.left:
                root.parent.left = right
            else:
                root.parent.right = right
        root.right = right.left
        right.left = root
        root.parent = right
        root.setHeight()
        right.setHeight()
        return right

    def rotateRightChild(root):
        left = root.left
        if left == None:
            return root
        left.parent = root.parent 
        if root.parent is not None:
            if root == root.parent.left:
                root.parent.left = left
            else:
                root.parent.right = left
        root.left = left.right
        left.right = root
        root.parent = left
        root.setHeight()
        left.setHeight()
        return left

    def burn(self, data):
        node = self.find_node(int(data))
        if node:
            queue = [node]
            visited = {node}
            print(node)
            while queue:
                this_minute_count = len(queue)
                for i in range(this_minute_count):
                    current_node = queue.pop(0)
                    if current_node.left and current_node.left not in visited:
                        queue.append(current_node.left)
                        visited.add(current_node.left)
                        print(current_node.left, end=" ")
                    if current_node.right and current_node.right not in visited:
                        queue.append(current_node.right)
                        visited.add(current_node.right)
                        print(current_node.right, end=" ")
                    if current_node.parent and current_node.parent not in visited:
                        queue.append(current_node.parent)
                        visited.add(current_node.parent)
                        print(current_node.parent, end=" ")
                print()
        else:
            print(f"There is no {data} in the tree.")
    
    def find_node(self, data):
        return AVLTree._find_node(self.root, data)

    def _find_node(root, data):
        if root is None:
            return None
        if root.data == data:
            return root
        elif data < root.data:
            return AVLTree._find_node(root.left, data)
        else:
            return AVLTree._find_node(root.right, data)
        

    def inorder_traversal(self, root):
        if root is None:
            return []
        return (self.inorder_traversal(root.left) + [root.data] + self.inorder_traversal(root.right))
    
    def print_tree_level(self, nodes, level, max_level):
        if not any(nodes):
            return
        current_indent = int(2 ** (max_level - level + 1) - 1)
        between_spaces = int(2 ** (max_level - level + 2) - 1)

        line = " " * (current_indent - 1)
        new_nodes = []
        for node in nodes:
            if node is None:
                line += " " * (between_spaces + 1)
                new_nodes.extend([None, None])
            else:
                line += f"{node}"
                new_nodes.extend([node.left, node.right])
                line += " " * between_spaces
        print(line.rstrip())
        self.print_tree_level(new_nodes, level + 1, max_level)

    def print_tree(self):
        height = self.root.height + 1
        self.print_tree_level([self.root], 1, height)


node_inp, burn_node = input("Enter node and burn node : ").split("/")
node_list = list(map(int, node_inp.split(" ")))

avl = AVLTree()
for node in node_list:
    avl.insert(node)

avl.print_tree()
avl.burn(burn_node)