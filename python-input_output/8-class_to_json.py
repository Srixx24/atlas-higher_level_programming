#!/usr/bin/python3
"""
Function that returns the dictionary description with simple data structure
"""


def class_to_json(obj):
    """
    Serialize the writable attributes of an object
    """
    return obj.__dict__
