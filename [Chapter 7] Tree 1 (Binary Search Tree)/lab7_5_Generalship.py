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
    
    def printTree(self, node, level = 0):
        if self.root == None:
            return True
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def father(self, data_node, current_node, previous_node = None, child_position = None):
        result = "Not Found Data"
        if current_node == None:
            return "Not Found Data"
        if current_node == data_node:
            if previous_node != None:
                return previous_node, child_position
            else:
                return None, None
        else:
            result = self.father(data_node, current_node.left, current_node, "left")
            if result != "Not Found Data":
                return result
            result = self.father(data_node, current_node.right, current_node, "right")
            if result != "Not Found Data":
                return result
        return result
    
    def attack_more(self, node, value, path = None, remove_path_list = None, count = 0, remove_root = False):
        if path == None:
            path = []
        if remove_path_list == None:
            remove_path_list = []

        if node == self.root:
            print("--------------------------------------------------")
            print(f"Removing paths where the sum is greater than {value}:")
        if node != None:
            if len(path) > count:
                path[count] = node.data
            else:
                path.append(node.data)
            count += 1

            self.attack_more(node.left, value, path, remove_path_list, count)
            self.attack_more(node.right, value, path, remove_path_list, count)

            if node.left == None and node.right == None and sum(path) > value:
                father, child_position = self.father(node, self.root)
                if child_position == "left":
                    father.left = None
                elif child_position == "right":
                    father.right = None
                else:
                    remove_root = True
                remove_path_list.append(path.copy())
            path.pop()

        if count == 1 and node == self.root:
            if remove_root:
                self.root = None
            if not remove_path_list:
                print(f"No paths were removed.")
            for i in range(len(remove_path_list)):
                print(f"{i+1}) {'->'.join(map(str, remove_path_list[i]))} = {sum(remove_path_list[i])}")

    def attack_less(self, node, value, path = None, remove_path_list = None, count = 0, remove_root = False):
        if path == None:
            path = []
        if remove_path_list == None:
            remove_path_list = []

        if node == self.root:
            print("--------------------------------------------------")
            print(f"Removing paths where the sum is less than {value}:")
        if node != None:
            if len(path) > count:
                path[count] = node.data
            else:
                path.append(node.data)
            count += 1

            self.attack_less(node.left, value, path, remove_path_list, count)
            self.attack_less(node.right, value, path, remove_path_list, count)
            if node.left == None and node.right == None and sum(path) < value:
                father, child_position = self.father(node, self.root)
                if child_position == "left":
                    father.left = None
                elif child_position == "right":
                    father.right = None
                else:
                    remove_root = True
                remove_path_list.append(path.copy())
            path.pop()

        if count == 1 and node == self.root:
            if remove_root:
                self.root = None
            if not remove_path_list:
                print(f"No paths were removed.")
            for i in range(len(remove_path_list)):
                print(f"{i+1}) {'->'.join(map(str, remove_path_list[i]))} = {sum(remove_path_list[i])}")

    def attack_equal(self, node, value, path = None, remove_path_list = None, count = 0, remove_root = False):
        if path == None:
            path = []
        if remove_path_list == None:
            remove_path_list = []

        if node == self.root:
            print("--------------------------------------------------")
            print(f"Removing paths where the sum is equal to {value}:")
        if node != None:
            if len(path) > count:
                path[count] = node.data
            else:
                path.append(node.data)
            count += 1

            self.attack_equal(node.left, value, path, remove_path_list, count)
            self.attack_equal(node.right, value, path, remove_path_list, count)

            if node.left == None and node.right == None and sum(path) == value:
                father, child_position = self.father(node, self.root)
                if child_position == "left":
                    father.left = None
                elif child_position == "right":
                    father.right = None
                else:
                    remove_root = True
                remove_path_list.append(path.copy())
            path.pop()

        if count == 1 and node == self.root:
            if remove_root:
                self.root = None
            if not remove_path_list:
                print(f"No paths were removed.")
            for i in range(len(remove_path_list)):
                print(f"{i+1}) {'->'.join(map(str, remove_path_list[i]))} = {sum(remove_path_list[i])}")


T = BST()
city_A, city_B = input("Enter <Create City A (BST)>/<Create conditions and deploy the army>: ").split('/')
city_A = city_A.split()
for i in city_A:
    T.append(int(i))
print("(City A) Before the war:")
T.printTree(T.root)
city_B = city_B.split(',')
for i in city_B:
    if i[:1] == "M":
        T.attack_more(T.root, int(i[1:]))
    elif i[:1] == "L":
        T.attack_less(T.root, int(i[1:]))
    elif i[:2] == "EQ":
        T.attack_equal(T.root, int(i[2:]))
    print("--------------------------------------------------")
    print("(City A) After the war:")
    if T.printTree(T.root):
        print("City A has fallen!")
        break