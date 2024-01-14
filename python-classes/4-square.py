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
        self.size = size

    @property
    def size(self):
        """getting size"""
        return self.__size
    @property.setter
    def size(self, value):
        """Set to size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area"""
        return self.__size ** 2
