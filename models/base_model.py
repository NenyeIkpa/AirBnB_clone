#!/usr/bin/python3
"""
    BaseModel  module
"""
import uuid
from datetime import datetime


class BaseModel:
    """ parent class, BaseModel """

    def __init__(self):
        """ initialization function for an object of the BaseModel class """
        # assign a unique id to each object
        BaseModel.id = str(uuid.uuid4())
        self.created_at = datetime.now()

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
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict
