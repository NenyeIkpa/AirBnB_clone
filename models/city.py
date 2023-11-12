#!/usr/bin/python3
"""
    City Module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ holds city of user(name and id) """

    state_id = ""
    name = ""
