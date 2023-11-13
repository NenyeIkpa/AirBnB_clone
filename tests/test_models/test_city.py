#!/usr/bin/python3
"""
    Unit tests for City class
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class"""

    def test_no_args_instance(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        cty = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cty))
        self.assertNotIn("state_id", cty.__dict__)

    def test_name_is_public_class_attribute(self):
        cty = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cty))
        self.assertNotIn("name", cty.__dict__)

    def test_two_cities_have_unique_ids(self):
        cty1 = City()
        cty2 = City()
        self.assertNotEqual(cty1.id, cty2.id)

    def test_two_cities_have_different_created_at(self):
        cty1 = City()
        sleep(0.05)
        cty2 = City()
        self.assertLess(cty1.created_at, cty2.created_at)

    def test__str__(self):
        date_now = datetime.now()
        date_now_repr = repr(date_now)
        cty = City()
        cty.id = "000789"
        cty.created_at = cty.updated_at = date_now
        cty_str = cty.__str__()
        self.assertIn("[City] (000789)", cty_str)
        self.assertIn("'id': '000789'", cty_str)
        self.assertIn("'created_at': " + date_now_repr, cty_str)
        self.assertIn("'updated_at': " + date_now_repr, cty_str)

    def test_args_unused(self):
        cy = City(None)
        self.assertNotIn(None, cy.__dict__.values())

    def test_instantiation_with_kwargs(self):
        date_now = datetime.now()
        date_now_iso = date_now.isoformat()
        cty = City(
                id="111222",
                created_at=date_now_iso,
                updated_at=date_now_iso
                )
        self.assertEqual(cty.id, "111222")
        self.assertEqual(cty.created_at, date_now)
        self.assertEqual(cty.updated_at, date_now)


class TestCity_save(unittest.TestCase):
    """Unittests for testing save method of the City class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def test_save_first_time(self):
        cty = City()
        sleep(0.05)
        first_updated_at = cty.updated_at
        cty.save()
        self.assertLess(first_updated_at, cty.updated_at)

    def test_save_after_multiple_updates(self):
        cty = City()
        sleep(0.05)
        first_updated_at = cty.updated_at
        cty.save()
        second_updated_at = cty.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        cty.save()
        self.assertLess(second_updated_at, cty.updated_at)

    def test_save_with_arg(self):
        cy = City()
        with self.assertRaises(TypeError):
            cy.save(None)

    def test_save_updates_file(self):
        cty = City()
        cty.save()
        cty_id = "City." + cty.id
        with open("file.json", "r") as f:
            self.assertIn(cty_id, f.read())

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass


class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_valid_keys(self):
        cty = City()
        self.assertIn("id", cty.to_dict())
        self.assertIn("created_at", cty.to_dict())
        self.assertIn("updated_at", cty.to_dict())
        self.assertIn("__class__", cty.to_dict())

    def test_to_dict_contains_new_attributes(self):
        cty = City()
        cty.code = "AKV"
        cty.my_number = 84
        self.assertEqual("AKV", cty.code)
        self.assertIn("my_number", cty.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        cy = City()
        cy_dict = cy.to_dict()
        self.assertEqual(str, type(cy_dict["id"]))
        self.assertEqual(str, type(cy_dict["created_at"]))
        self.assertEqual(str, type(cy_dict["updated_at"]))

    def test_to_dict_print(self):
        date_now = datetime.now()
        cty = City()
        cty.id = "1234"
        cty.created_at = cty.updated_at = date_now
        cty_dict = {
            'id': '1234',
            '__class__': 'City',
            'created_at': date_now.isoformat(),
            'updated_at': date_now.isoformat(),
        }
        self.assertDictEqual(cty.to_dict(), cty_dict)


if __name__ == "__main__":
    unittest.main()
