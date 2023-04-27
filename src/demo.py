"""Demo python file."""

def my_func(name: str)-> str:
    return f"Hello {name}, welcome to Sacumen." 

print(my_func("Python developer"))


def add(num1: int, num2: int)-> int:
    """Sum of 2 numbers.

    Args:
        num1 (int): a number.
        num2 (int): another number.

    Returns:
        int: result of int which is sum of num1 and num2.
    """
    return num1 + num2
    

