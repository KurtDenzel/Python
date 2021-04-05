import os
os.system('cls')

#Built-in Method Functions to be invoked.
class arithmetic:
    def __init__(self, num1, num2):
        self.num1 = num1   
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        return float(self.num1 / self.num2)

n1 = int(input("Enter first integer: "))
n2 = int(input("Enter second integer: "))
test = arithmetic(n1, n2)

print("-------"*5)
print ("Sum: ", test.add())
print ("Difference: ", test.subtract())
print ("Product: ", test.multiply())
print ("Quotient: ", test.divide())

print("-------"*5)
print("NAME: KURT DENZEL CALACDAY")
print("STUDENT NUMBER: 20201125680")
print("-------"*5)