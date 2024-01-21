#!/usr/bin/python3
"""
class Square that inherits from Rectangle 9-rectangle.py and 10-square.py
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square inheriting from Rectangle
    """
    def __init__(self, size):
        """
        Starts instance of a square
        """
        self.integer_validator("_size", size)
        super().__init__(size, size)
        self._size = size
   
    def area(self):
        """Area for square"""
        return self._size ** 2

    def __str__(self):
        """String for square"""
        return "[Square] {size}/{size}".format(size=self.__size)
