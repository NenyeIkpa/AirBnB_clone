#!/usr/bin/python3
"""
    BaseModel  module
"""
import uuid
from datetime import datetime


class BaseModel:
    """ parent class, BaseModel """

    def __init__(self, *args, **kwargs):
        """ initialization function for an object of the BaseModel class """

        if kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "created_at":
                    self.created_at = datetime.fromisoformat(value)
                if key == "updated_at":
                    self.updated_at = datetime.fromisoformat(value)
        else:
            # assign a unique id to each object
            self.id = str(uuid.uuid4())

            date_format = '%Y-%m-%dT%H:%M:%S.%f'
            date_now = datetime.now()
            self.created_at = date_now.strftime(date_format)
            self.updated_at = self.created_at

    def __str__(self):
        """ returns a string representation the object """
        return "{} ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ sets time updated """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary representation of the object """
        obj_dict = self.__dict__
        obj_dict['created_at'] = str(self.created_at)
        obj_dict['updated_at'] = str(self.updated_at)
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict
