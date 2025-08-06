class Math:
   def __init__(self, a: float, b: float) -> None:
       self.a: float = a
       self.b: float = b

   def add(self) -> float:
       return self.a + self.b

   def subtract(self) -> float:
       return self.a - self.b

   def multiply(self) -> float:
       return self.a * self.b

   def divide(self) -> float | str:
       if self.b == 0:
          return "Cannot divide by zero"
       return self.a / self.b


if __name__ == "__main__":
   calc = Math(10, 5)
   print("Addition:", calc.add())
   print("Subtraction:", calc.subtract())
   print("Multiplication:", calc.multiply())
   print("Division:", calc.divide())
