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
                if key == "id":
                    self.id = value
                if key == "created_at":
                    self.created_at = datetime.fromisoformat(value)
                if key == "updated_at":
                    self.updated_at = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            # assign a unique id to each object
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
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
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = str(self.created_at)
        obj_dict['updated_at'] = str(self.updated_at)
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict
