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

def father(data, current_node, previous_node = None):
    result = "Not Found Data"
    if current_node == None:
        return "Not Found Data"
    if current_node.data == data:
        if previous_node != None:
            return previous_node.data
        else:
            return f"None Because {data} is Root"
    else:
        result = father(data, current_node.left, current_node)
        if result != "Not Found Data":
            return result
        result = father(data, current_node.right, current_node)
        if result != "Not Found Data":
            return result
    return result

tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.create(int(e))
printTree90(tree.root)
print(father(int(data[1]), tree.root))