#!/usr/bin/python3
"""
class Square that inherits from Rectangle 9-rectangle.py
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
