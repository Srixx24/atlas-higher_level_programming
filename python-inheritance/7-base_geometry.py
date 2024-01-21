#!/usr/bin/python3
"""
Class BaseGeometry based on 6-base_geometry.py
"""


class BaseGeometry:
    """
    A class representing geometric objects
    """
    def area(self):
        """Area of a geometric object"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value

        Args:
            name: name of value
            value: value to be checked
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))
