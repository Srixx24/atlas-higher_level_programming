#!/usr/bin/python3
"""
Class Rectangle that defines a rectangle based on 2-rectangle.py
"""


class Rectangle:
    """
    Class Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Start of Rectangle instance.

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
        """Setting width"""
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
        """Setting height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returning area (width * height)"""
        return self.width * self.height

    def perimeter(self):
        """Returning perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns string representing rectangle with #"""
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += '#' * self.width
        return rectangle_str[:-1]

    def __repr__(self):
        """Returns string representing rectangle"""
        return "<3-rectangle.Rectangle object"
