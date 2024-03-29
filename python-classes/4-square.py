#!/usr/bin/python3
"""
This module defines the Square class.
"""


class Square:
    """
    A class representing a square.

    Attributes:
         __size (int): The size of the square (private).
    """
    def __init__(self, size=0):
        """
        Starts new instance of the square class

        Args:
            size (int, optional): size of square, 0
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set size

        Parameter:
            value (int): size
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns area

        Return:
            int: area
        """
        return self.__size ** 2
