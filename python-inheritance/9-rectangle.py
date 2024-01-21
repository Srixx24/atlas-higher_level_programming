#!/usr/bin/python3
"""
Class Rectangle that inherits from BaseGeometry
7-base_geometry.py and 8-rectangle.py
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a Rectangle inheriting from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Starts instance of a rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """string for rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """area for rectangle"""
        return self.__width * self.__height
