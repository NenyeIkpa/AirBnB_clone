#!/usr/bin/python3
"""
    Unit tests for BaseModel class
"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ holds test cases for the BaseModel class """
    def test_init(self):
        """  test function for __init__ of BaseModel class """
        bm1 = BaseModel()
        self.assertNotEqual(bm1.id, '')
        self.assertNotEqual(bm1.created_at, '')

    def test_args(self):
        """tests for args passed to BaseModel """
        """
            bm2 = BaseModel({'my_number': 89, 'name': 'My First Model', '__class__': 'BaseModel', 'updated_at': '2017-09-28T21:05:54.119572',
            'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28T21:05:54.119427'})
            self.assertEqual(bm2.created_at, datetime(2017, 9, 28, 21, 5, 54, 119427))
        """

        """
            with self.assertRaises(TypeError):
            BaseModel([89, 'My First Model', 'BaseModel', '2017-09-28T21:05:54.119572', 'b6a6e15c-c67d-4312-9a75-9d084935e579', '2017-09-28T21:05:54.119427'])
        """
