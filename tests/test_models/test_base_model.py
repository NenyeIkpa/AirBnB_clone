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
        with self.assertRaises(TypeError):
            BaseModel(121)

        with self.assertRaises(TypeError):
            BaseModel("abx")
