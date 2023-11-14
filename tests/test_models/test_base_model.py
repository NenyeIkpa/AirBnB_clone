#!/usr/bin/python3
"""
    Unit tests for BaseModel class
"""

import os
from time import sleep
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

    def test__str__(self):
        date_now = datetime.now()
        date_now_repr = repr(date_now)
        bm = BaseModel()
        bm.id = "123456789"
        bm.created_at = bm.updated_at = date_now
        bm_str = bm.__str__()
        self.assertIn("[BaseModel] (123456789)", bm_str)
        self.assertIn("'id': '123456789'", bm_str)
        self.assertIn("'created_at': " + date_now_repr, bm_str)
        self.assertIn("'updated_at': " + date_now_repr, bm_str)


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class """

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_contains_valid_keys(self):
        bm1 = BaseModel()
        self.assertIn("id", bm1.to_dict())
        self.assertIn("created_at", bm1.to_dict())
        self.assertIn("updated_at", bm1.to_dict())
        self.assertIn("__class__", bm1.to_dict())

    def test_to_dict_contains_new_attributes(self):
        bm2 = BaseModel()
        bm2.name = "November"
        bm2.my_number = 49
        self.assertIn("name", bm2.to_dict())
        self.assertIn("my_number", bm2.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        bm3 = BaseModel()
        bm3_dict = bm3.to_dict()
        self.assertEqual(str, type(bm3_dict["created_at"]))
        self.assertEqual(str, type(bm3_dict["updated_at"]))

    def test_to_dict_print(self):
        date_now = datetime.now()
        bm4 = BaseModel()
        bm4.id = "123456789"
        bm4.created_at = bm4.updated_at = date_now
        bm4_dict = {
            'id': '123456789',
            '__class__': 'BaseModel',
            'created_at': date_now.isoformat(),
            'updated_at': date_now.isoformat()
        }
        self.assertDictEqual(bm4.to_dict(), bm4_dict)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def test_save_first_time(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_save_after_multiple_updates(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
