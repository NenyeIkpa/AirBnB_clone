#!/usr/bin/python3
"""
    Unit tests for the Review class
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_no_args_instances(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_class_attributes_are_public(self):
        rvw = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rvw))
        self.assertNotIn("place_id", rvw.__dict__)

        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rvw))
        self.assertNotIn("user_id", rvw.__dict__)

        rv = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rvw))
        self.assertNotIn("text", rvw.__dict__)

    def test_two_reviews_have_unique_ids(self):
        rvw1 = Review()
        rvw2 = Review()
        self.assertNotEqual(rvw1.id, rvw2.id)

    def test_two_reviews_have_different_created_at(self):
        rvw1 = Review()
        sleep(0.05)
        rvw2 = Review()
        self.assertLess(rvw1.created_at, rvw2.created_at)

    def test__str__(self):
        date_now = datetime.now()
        date_now_repr = repr(date_now)
        rvw = Review()
        rvw.id = "0001"
        rvw.created_at = rvw.updated_at = date_now
        rvw_str = rvw.__str__()
        self.assertIn("[Review] (0001)", rvw_str)
        self.assertIn("'id': '0001'", rvw_str)
        self.assertIn("'created_at': " + date_now_repr, rvw_str)
        self.assertIn("'updated_at': " + date_now_repr, rvw_str)

    def test_args_unused(self):
        rvw = Review(None)
        self.assertNotIn(None, rvw.__dict__.values())

    def test_instantiation_with_kwargs(self):
        date_now = datetime.now()
        date_now_iso = date_now.isoformat()
        rvw = Review(
                id="0001",
                created_at=date_now_iso,
                updated_at=date_now_iso
                )
        self.assertEqual(rvw.id, "0001")
        self.assertEqual(rvw.created_at, date_now)
        self.assertEqual(rvw.updated_at, date_now)


class TestReview_save(unittest.TestCase):
    """Unittests for testing save method of the Review class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def test_save_first_time(self):
        rvw = Review()
        sleep(0.05)
        first_updated_at = rvw.updated_at
        rvw.save()
        self.assertLess(first_updated_at, rvw.updated_at)

    def test_save_after_multiple_updates(self):
        rvw = Review()
        sleep(0.05)
        first_updated_at = rvw.updated_at
        rvw.save()
        second_updated_at = rvw.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        rvw.save()
        self.assertLess(second_updated_at, rvw.updated_at)

    def test_save_with_arg(self):
        rvw = Review()
        with self.assertRaises(TypeError):
            rvw.save(None)

    def test_save_updates_file(self):
        rvw = Review()
        rvw.save()
        rvw_id = "Review." + rvw.id
        with open("file.json", "r") as f:
            self.assertIn(rvw_id, f.read())

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass


class TestReview_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Review class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_contains_valid_keys(self):
        rvw = Review()
        self.assertIn("id", rvw.to_dict())
        self.assertIn("created_at", rvw.to_dict())
        self.assertIn("updated_at", rvw.to_dict())
        self.assertIn("__class__", rvw.to_dict())

    def test_to_dict_contains_new_attributes(self):
        rvw = Review()
        rvw.others = "Awesome!"
        rvw.my_number = 49
        self.assertEqual("Awesome!", rvw.others)
        self.assertIn("my_number", rvw.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        rvw = Review()
        rvw_dict = rvw.to_dict()
        self.assertEqual(str, type(rvw_dict["id"]))
        self.assertEqual(str, type(rvw_dict["created_at"]))
        self.assertEqual(str, type(rvw_dict["updated_at"]))

    def test_to_dict_print(self):
        date_now = datetime.now()
        rvw = Review()
        rvw.id = "0001"
        rvw.created_at = rvw.updated_at = date_now
        rvw_dict = {
            'id': '0001',
            '__class__': 'Review',
            'created_at': date_now.isoformat(),
            'updated_at': date_now.isoformat(),
        }
        self.assertDictEqual(rvw.to_dict(), rvw_dict)


if __name__ == "__main__":
    unittest.main()
