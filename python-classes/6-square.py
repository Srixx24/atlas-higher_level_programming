#!/usr/bin/python3
"""
Class Square
"""


class Square:
    """
    A class representing a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Starts new instance of the square class
        Args:
            size (int, optional): size of square, 0
            position (tuple, optional): position of square
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getting position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the position"""
        if not isinstance((value, tuple) or len(value) != 2 or not all(isinstance(num, int) and num >=0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return area"""
        return self.__size ** 2

    def my_print(self):
        """Print square with #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
