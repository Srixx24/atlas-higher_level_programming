#!/usr/bin/python3
"""
Function that returns an object represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Create an object from a JSON
    """
    return json.loads(my_str)
