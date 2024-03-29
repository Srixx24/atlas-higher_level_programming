#!/usr/bin/python3
"""
Class Student that defines a student based on 10-student.py
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
        else:
            return {attr: getattr(self, attr) for attr in
                    attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Loads data for Student"""
        self.__dict__.update(json)
