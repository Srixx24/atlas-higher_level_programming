#!/usr/bin/python3
"""
Class Base used as base for all other classes in this project.
"""
import json


class Base:
    """
    Class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Start of class Base instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as file:
                json_string = file.read
                dict_list = cls.from_json_string(json_string)
                inst_list = [cls.create(**dictionary) for dictionary in dict_list]
                return inst_list

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation"""
        with open("{}.json".format(cls.__name__), 'w') as ofile:
            if list_objs:
                ofile.write(cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs]
                ))
            else:
                ofile.write("[]")

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set"""
        args = []
        while True:
            try:
                dummy = cls(*args)
                break
            except TypeError:
                args.append(1)
        dummy.update(**dictionary)
        return dummy
