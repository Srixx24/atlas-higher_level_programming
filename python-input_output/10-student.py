#!/usr/bin/python3
"""
Class Student that defines a student based on 9-student.py
"""


class Student:
    """
    Defines class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Start of student instance

        Args:
            first_name: First name of student
            last_name: Last name of student
            age: Student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a representation of a Student
        """
        if attrs is None:
            return self.__dict__
