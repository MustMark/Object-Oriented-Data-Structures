class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self, table_size, max_collision):
        self.table = [None] * int(table_size)
        self.max_collision = int(max_collision)
    
    def add(self, key, value):
        count = 1
        base_index = index = self.sum_ascii(key) % len(self.table)
        while count <= self.max_collision:
            if not self.table[index]:
                self.table[index] = Data(key, value)
                break
            else:
                print(f"collision number {count} at {index}")
                if count < self.max_collision:
                    index = (base_index + (count**2)) % len(self.table)
                    count += 1
                else:
                    print("Max of collisionChain")
                    break

    def sum_ascii(self, inp_str):
        sum = 0
        for i in inp_str:
            sum += ord(i)
        return sum

    def display_table(self):
        for i in range(len(self.table)):
            print(f"#{i + 1}\t{self.table[i]}")
        print("---------------------------")
        if not None in self.table:
            return True


print(" ***** Fun with hashing *****")
inp1, inp2 = input("Enter Input : ").split("/")

table_size, max_collision = inp1.split(" ")
data_list = inp2.split(",")

Hash = hash(table_size, max_collision)

for i in range(len(data_list)):
    key, value = data_list[i].split(" ")
    Hash.add(key, value)
    if Hash.display_table():
        print("This table is full !!!!!!")
        break