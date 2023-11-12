#!/usr/bin/python3
"""
    BaseModel  module
"""
import uuid
from datetime import datetime
import models



class BaseModel:
    """ parent class, BaseModel """

    def __init__(self, *args, **kwargs):
        """ initialization function for an object of the BaseModel class """

        if kwargs:
            """ create basemodel from dictionary """
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "id":
                    self.id = value
                elif key == "created_at":
                    self.created_at = datetime.strptime(value, date_format)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, date_format)
                else:
                    setattr(self, key, value)
        else:
            # assign a unique id to each object
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ returns a string representation the object """
        return "{} ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ sets time updated """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary representation of the object """
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict
