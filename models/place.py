#!/usr/bin/python3
"""
    PLace Module
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ holds attributes of the place of a user """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0
    longitude = 0
    amenity_ids = []
