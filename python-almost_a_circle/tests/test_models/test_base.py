#!/usr/bin/python3

import unittest, json
from models.base import Base

""" Create a test class for the Base class """


class testBase(unittest.TestCase):
    """ Testing base """

    id_value = Base(id)
    test_instance = Base(id_value)

    def test_more_creation(self):
        self.test_instance.id_value = 11
        test2 = Base(42)
        test3 = Base(1337)
        self.assertEqual(self.test_instance.id_value, 11)
        self.assertEqual(test2.id, 42)
        self.assertEqual(test3.id, 1337)

    def test_None_id(self):
        self.test_instance = Base(None)
        test2 = Base(None)
        self.assertEqual(self.test_instance.id, test2.id - 1)

    def test_automatically_assigned_id(self):
        """ Automatically assigned id """
        self.test_instance = Base(20)
        self.assertEqual(self.test_instance.id, 20)

    def test_id_string(self):
        """ id string """
        self.test_instance = Base("string")
        self.assertEqual(self.test_instance.id, "string")

    def test_id_negative(self):
        """ id negative """
        self.test_instance = Base(-10)
        self.assertEqual(self.test_instance.id, -10)

    def test_id_float(self):
        """ id float """
        self.test_instance = Base(1.5)
        self.assertEqual(self.test_instance.id, 1.5)

    def test_id_is_zero(self):
        """ id is zero """
        self.test_instance = Base(0)
        self.assertEqual(self.test_instance.id, 0)

    def test_id_list(self):
        """ id is a list """
        self.test_instance = Base([1, 2, 3])
        self.assertEqual(self.test_instance.id, [1, 2, 3])

    def test_id_dict(self):
        """ id is a dictionary """
        self.test_instance = Base({"a": 1, "b": 2})
        self.assertEqual(self.test_instance.id, {"a": 1, "b": 2})

    def test_id_tuple(self):
        """ id is a tuple """
        self.test_instance = Base((1,))
        self.assertEqual(self.test_instance.id, (1,))

if __name__ == '__main__':
    unittest.main()
