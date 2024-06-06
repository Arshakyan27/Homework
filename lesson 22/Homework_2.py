# 2. Class Exercise:
# Create a Python class representing a basic calculator with methods for addition,
# subtraction, multiplication, and division

class Calculator:
    def __init__(self) -> None:
        pass
    def add(self, *args):
        sum = 0
        for i in args:
           sum += i
        return sum 
    
    def min(self, *args):
        sum = args[0]
        for i in args[1:]:
           sum -= i
        return sum
    
    def divide(self, *args):
        sum = args[0]
        for i in args[1:]:
           sum /= i
        return sum
    
    def multiple(self, *args):
        sum = args[0]
        for i in args[1:]:
           sum *= i
        return sum
    
example = Calculator()
print(example.divide(45,15,3))