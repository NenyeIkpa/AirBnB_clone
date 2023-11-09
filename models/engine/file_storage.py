#!/usr/bin/python3
"""
    File Storage Module
"""
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """ saves objects to and reloads objects from file """
    __file_path = 'file.json'
    __objects = {}


    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
            with open(FileStorage.__file_path, "w") as f:
                json.dump(obj_dict, f)

    def reload(self):
        """  deserializes the JSON file to __objects """
        # if os.path.exists(FileStorage.__file_path):
        try:
            """ reads the JSON file,filename, and creates an object from it """
            with open(FileStorage.__file_path, "r") as the_file:
                obj_dict = json.load(the_file)
                for key, value in obj_dict.items():
                    classname, obj_id = key.split('.')
                    if classname in class_map:
                        obj_cls = class_map[classname]
                        obj = obj_cls(**value)
                        FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

# A dictionary mapping class names to their corresponding classes
class_map  = {
        "BaseModel": BaseModel
        }
