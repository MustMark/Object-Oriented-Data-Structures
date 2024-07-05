class Calculator :
    def __init__(self, number):
        self.number = number

    def __add__(self, num2):
        return self.number + num2.number

    def __sub__(self, num2):
        return self.number - num2.number
    
    def __mul__(self, num2):
        return self.number * num2.number
    
    def __truediv__(self, num2):
        return self.number / num2.number

x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))

print(x+y,x-y,x*y,x/y,sep = "\n")