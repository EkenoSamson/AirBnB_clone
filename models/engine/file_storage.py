#!/usr/bin/python3
"""module contains the class FileStorage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.state import State


class FileStorage(object):
    """
    It is the storage engine.
    Attributes:
        __file_path - string path to json file.
        __objects - dictionary that stores all objects by <class name>.id

    Methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects.
    """

    __file_path = "file.json"
    __objects = {}
    class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "City": City,
            "Review": Review,
            "Place": Place,
            "Amenity": Amenity,
            "State": State
            }

    def all(self):
        """return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        o_dict = {key: val.to_dict() for key, val in self.__objects.items()}
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(o_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                d_dict = json.load(f)
            for key, value in d_dict.items():
                ob = self.class_dict[value["__class__"]](**value)
                self.__objects[key] = ob
        except FileNotFoundError:
            pass
