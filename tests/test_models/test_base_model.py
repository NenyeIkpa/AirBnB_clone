#!/usr/bin/python3
"""
    Unit tests for BaseModel class
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ holds test cases for the BaseModel class """
    def test_init(self):
        """  test function for __init__ of BaseModel class """
        bm1 = BaseModel()
        self.assertNotEqual(bm1.id, '')
        self.assertNotEqual(bm1.created_at, '')

    def test_args(self):
        """ tests for args passed to BaseModel """
        bm2 = BaseModel()
        bm2.my_number = 89
        bm2.name = 'My First Model'
        self.assertNotEqual(bm2.id, '')
        self.assertEqual(bm2.name, 'My First Model')
        self.assertEqual(bm2.my_number, 89)
        self.assertEqual(type(bm2), BaseModel)
