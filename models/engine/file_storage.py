#!/usr/bin/python3

"""
This file contains the FileStorage class that converts between str and dict
"""

import json

from models.base_model import BaseModel


class FileStorage:
    """ The JSON FileStorage class """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """

        with open(self.__file_path, "w") as filename:
            storage_dict = {}

            for key, value in self.__objects.items():
                storage_dict[key] = value.to_dict()

            json.dump(storage_dict, filename)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """

        try:
            with open(self.__file_path, encoding="utf-8") as filename:
                for obj in json.load(filename).values():
                    self.new(eval(obj["__class__"])(**obj))

        except FileNotFoundError:
            return
