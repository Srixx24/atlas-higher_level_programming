#!/usr/bin/python3
"""
Class Square
"""


class Square:
    """
    A class representing a square.
    """
    def __init__(self, size=0):
        """
        Starts new instance of the square class

        Args:
            size (int, optional): size of square, 0
                raises:
                TypeError: If size is not an integer.
                ValueError: If size is less than 0.
        """
        self.__size = size

    @property
    def size(self):
        """Getting size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set to size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return area"""
        return self.__size ** 2

    def my_print(self):
        """Print square with #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
