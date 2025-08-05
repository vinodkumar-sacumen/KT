class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "Cannot divide by zero"
        return self.a / self.b



calc = Math(10, 5)
print("Addition:", calc.add())         
print("Subtraction:", calc.subtract()) 
print("Multiplication:", calc.multiply()) 
print("Division:", calc.divide())      
