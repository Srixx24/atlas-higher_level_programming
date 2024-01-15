#!/usr/bin/python3
"""
Prints a square with the character #
"""


def print_square(size):
    """
    Prints a square with the character #

    Args:
        size (int): length of the square

    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
