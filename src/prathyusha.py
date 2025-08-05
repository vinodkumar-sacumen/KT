class ReverseANumber:
    """ 
    This class reverses a positive or negative integer number.
    """

    def __init__(self, a: int) -> None:
        """
        Initializes the class with an integer.

        :param a: Integer to be reversed
        """
        self.a = a
		
    def reverse(self) -> int:
        """
        Reverses the given integer and returns the reversed value.

        :return: Reversed integer
        """
        temp = abs(self.a)
        reversed_num = 0

        while temp > 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp = temp // 10

        return reversed_num

r=ReverseANumber(-1234)
print(r.reverse())
