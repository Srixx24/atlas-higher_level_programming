#!/usr/bin/python3
"""
Function that returns True if the object is exactly
an instance of the specified class, otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Check if object is of type a_class
    """
    return type(obj) is a_class
