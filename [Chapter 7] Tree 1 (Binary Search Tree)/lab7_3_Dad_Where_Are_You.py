class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def father(previous_node, data, current_node):
    result = None
    
    print(f"1 : {previous_node}, {data}, {current_node}")
    if current_node.left != None:
        previous_node = current_node
        result = father(previous_node, data, current_node.left)
        if result != None:
            return result
    if current_node.right != None:
        previous_node = current_node
        result = father(previous_node, data, current_node.right)
        if result != None:
            return result
    print(f"2 : {previous_node}, {data}, {current_node}")
    if current_node.data == data:
        return previous_node.data
    return result

tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.create(e)
printTree90(tree.root)
print(father(tree.root, data[1], tree.root))