"""Module to reverse a positive or negative integer."""


# pylint: disable=too-few-public-methods
class ReverseANumber:
    """This class reverses a positive or negative integer number."""

    def __init__(self, input_number: int) -> None:
        """
        Initialize the class with an integer.

        :param input_number: Integer to be reversed
        """
        if not isinstance(input_number, int):
            raise TypeError(f"Expected int, got {type(input_number).__name__}")
        self.input_number = input_number

    def reverse(self) -> int:
        """
        Reverses the given integer and returns the reversed value.

        :return: Reversed integer with sign preserved
        """
        temp = abs(self.input_number)
        reversed_num = 0

        while temp > 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp = temp // 10

        if self.input_number < 0:
            return -reversed_num
        return reversed_num


if __name__ == "__main__":
    r = ReverseANumber(-124)
    print(r.reverse())
