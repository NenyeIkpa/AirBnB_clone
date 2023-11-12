#!/usr/bin/python3
"""
    File Storage Module
"""
import json
import os
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ saves objects to and reloads objects from file """
    __file_path = 'file.json'
    __objects = {}


    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
            with open(self.__file_path, "w") as f:
                json.dump(obj_dict, f)

    def reload(self):
        """  deserializes the JSON file to __objects """
        # if os.path.exists(FileStorage.__file_path):
        try:
            """ reads the JSON file,filename, and creates an object from it """
            with open(self.__file_path, "r") as the_file:
                obj_dict = json.load(the_file)
                for key, value in obj_dict.items():
                    classname, obj_id = key.split('.')
                    if classname in class_map:
                        obj_cls = class_map[classname]
                        obj = obj_cls(**value)
                        self.__objects[key] = obj
        except FileNotFoundError:
            pass

# A dictionary mapping class names to their corresponding classes
class_map  = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
        }
