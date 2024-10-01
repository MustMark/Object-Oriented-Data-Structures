class Hash:
    def __init__(self, table_size, max_collision, threshold):
        self.table = [None] * int(table_size)
        self.max_collision = int(max_collision)
        self.threshold = int(threshold)
        self.newest_index = None
    
    def add(self, data):
        count = 1
        base_index = index = int(data) % len(self.table)
        while count <= self.max_collision:
            if not self.table[index]:
                self.table[index] = data
                self.newest_index = index
                if self.check_data():
                    self.add(data)
                break
            else:
                print(f"collision number {count} at {index}")
                if count < self.max_collision:
                    index = (base_index + (count**2)) % len(self.table)
                    count += 1
                else:
                    print("****** Max collision - Rehash !!! ******")
                    self.table = self.rehash(self.double_more_prime(len(self.table)), self.max_collision, self.threshold, self.table)
                    self.add(data)
                    break

    def double_more_prime(self, num):
        num *= 2
        while not self.prime(num):
            num += 1
        return num
    
    def prime(self, num):
        for i in range(2,num):
            if num % i == 0:
                return False
        return True
    
    def check_data(self):
        data_percentage = 100 - (self.table.count(None) / len(self.table) * 100)
        if data_percentage > float(self.threshold):
            print("****** Data over threshold - Rehash !!! ******")
            self.table[self.newest_index] = None
            self.table = self.rehash(self.double_more_prime(len(self.table)), self.max_collision, self.threshold, self.table)
            return True

    def rehash(self, table_size, max_collision, threshold, old_hash_table):
        new_hash = Hash(table_size, max_collision, threshold)
        for i in reversed(old_hash_table):
            if i:
                new_hash.add(i)
        return new_hash.table
        

    def display_table(self):
        for i in range(len(self.table)):
            print(f"#{i + 1}\t{self.table[i]}")
        print("----------------------------------------")
        if not None in self.table:
            return True


print(" ***** Rehashing *****")
inp1, inp2 = input("Enter Input : ").split("/")

table_size, max_collision, threshold = inp1.split(" ")
data_list = inp2.split(" ")

hash = Hash(table_size, max_collision, threshold)
print("Initial Table :")
hash.display_table()

for i in data_list:
    print(f"Add : {i}")
    hash.add(i)
    hash.display_table()