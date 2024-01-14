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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
