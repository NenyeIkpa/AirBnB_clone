#!/usr/bin/python3
"""
    Unit tests for State class
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

    def test_no_args_instantiates(self):
        self.assertEqual(State, type(State()))

    def test_new_instance_stored(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_name_is_public_class_attribute(self):
        st = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(st))
        self.assertNotIn("name", st.__dict__)

    def test_two_states_have_unique_ids(self):
        st1 = State()
        st2 = State()
        self.assertNotEqual(st1.id, st2.id)

    def test_two_states_have_different_created_at(self):
        st1 = State()
        sleep(0.05)
        st2 = State()
        self.assertLess(st1.created_at, st2.created_at)

    def test__str__(self):
        date_now = datetime.now()
        date_now_repr = repr(date_now)
        st = State()
        st.id = "AB564"
        st.created_at = st.updated_at = date_now
        st_str = st.__str__()
        self.assertIn("[State] (AB564)", st_str)
        self.assertIn("'id': 'AB564'", st_str)
        self.assertIn("'created_at': " + date_now_repr, st_str)
        self.assertIn("'updated_at': " + date_now_repr, st_str)

    def test_args_unused(self):
        st = State(None)
        self.assertNotIn(None, st.__dict__.values())

    def test_instantiation_with_kwargs(self):
        date_now = datetime.now()
        date_now_iso = date_now.isoformat()
        st = State(
                id="AB564",
                created_at=date_now_iso,
                updated_at=date_now_iso
                )
        self.assertEqual(st.id, "AB564")
        self.assertEqual(st.created_at, date_now)
        self.assertEqual(st.updated_at, date_now)


class TestState_save(unittest.TestCase):
    """Unittests for testing save method of the State class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def test_save_first_time(self):
        st = State()
        sleep(0.05)
        first_updated_at = st.updated_at
        st.save()
        self.assertLess(first_updated_at, st.updated_at)

    def test_save_after_multiple_updates(self):
        st = State()
        sleep(0.05)
        first_updated_at = st.updated_at
        st.save()
        second_updated_at = st.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        st.save()
        self.assertLess(second_updated_at, st.updated_at)

    def test_save_with_arg(self):
        st = State()
        with self.assertRaises(TypeError):
            st.save(None)

    def test_save_updates_file(self):
        st = State()
        st.save()
        stid = "State." + st.id
        with open("file.json", "r") as f:
            self.assertIn(stid, f.read())

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass


class TestState_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the State class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_contains_valid_keys(self):
        st = State()
        self.assertIn("id", st.to_dict())
        self.assertIn("created_at", st.to_dict())
        self.assertIn("updated_at", st.to_dict())
        self.assertIn("__class__", st.to_dict())

    def test_to_dict_contains_new_attributes(self):
        st = State()
        st.motto = "Heartbeat of the Nation"
        self.assertEqual("Heartbeat of the Nation", st.motto)
        self.assertIn("motto", st.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        st = State()
        st_dict = st.to_dict()
        self.assertEqual(str, type(st_dict["id"]))
        self.assertEqual(str, type(st_dict["created_at"]))
        self.assertEqual(str, type(st_dict["updated_at"]))

    def test_to_dict_print(self):
        date_now = datetime.now()
        st = State()
        st.id = "123456"
        st.created_at = st.updated_at = date_now
        st_dict = {
            'id': '123456',
            '__class__': 'State',
            'created_at': date_now.isoformat(),
            'updated_at': date_now.isoformat(),
        }
        self.assertDictEqual(st.to_dict(), st_dict)


if __name__ == "__main__":
    unittest.main()
