class Queue:
    def __init__(self, i = None):
        if i is None:
            i = []
        self.items = i

    def __str__(self):
        return f"Queue : {self.items} by Mark Sud Lhor"

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

def get_max_number(n):
    i = 0
    while n > 0:
        n //= 10
        i += 1
    return i

def get_number(n, d):
    for i in range(d):
        n //= 10
    return n % 10

def radix_sort(l):
    result = Queue(l)
    max_number = get_max_number(max(l))
    qDigit =[Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue()]
    for i in range (0, max_number):
        while not result.isEmpty():
            num = result.deQueue()
            num_number = get_number(num, i)
            qDigit[num_number].enQueue(num)
        for j in qDigit:
            while not j.isEmpty() :
                result.enQueue(j.deQueue())
    return result.items

x = [64, 8, 216, 512, 27, 729, 0, 1, 343, 125]
print(radix_sort(x))

# def move(n, A, C, B):
#     if n == 1:
#         print(n, 'from', A, 'to', C)
#     else:
#         move(n-1, A, B, C)
#         print(n, 'from', A, 'to', C)
#         move(n-1, B, C, A)

# print(move(4, "A", "C", "B"))
