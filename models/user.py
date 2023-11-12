#!/usr/bin/python3
"""
    User Module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ holds all attributes and methods of a user """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
