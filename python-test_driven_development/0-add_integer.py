#!/usr/bin/python3
"""
Adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): Second number, set at 98
    Raises:
        TypeError: If a is not an integer or float.
        TypeError: If b is not an integer or float.
    Return:
        int: a + b = return

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    a = int(a)
    b = int(b)

    return a + b
