#!/usr/bin/python3
"""
class Rectangle that inherits from BaseGeometry 7-base_geometry.py
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
        self.integer_validator("_width", width)
        self.integer_validator("_height", height)
        self._width = width
        self._height = height

