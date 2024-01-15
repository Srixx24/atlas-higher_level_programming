#!/usr/bin/python3
"""
Class Rectangle that defines a rectangle based on 0-rectangle.py
"""


class Rectangle:
    """
    Class Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Starting a Rectangle instance.

        Args:
            width (int, optional): Width of rectangle
            height (int, optional): Height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getting width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setting width

        Args:
            value (int): Set width

        Raises:
            TypeError: If the width value is not an integer.
            ValueError: If the width value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getting height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setting height

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the height value is not an integer.
            ValueError: If the height value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
