#!/usr/bin/python3
"""
Function to read and print a file
"""


def read_file(filename=""):
    """
    Print file contents

    Args:
        filename:(str) Name of file to be read

    """
    with open(filename, encoding="utf-8") as myFile:
        print("{}".format(myFile.read()), end="")
