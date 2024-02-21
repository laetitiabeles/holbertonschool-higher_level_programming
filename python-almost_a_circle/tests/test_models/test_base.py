#!/usr/bin/python3

import unittest, json
from models.base import Base

""" Create a test class for the Base class """


class testBase(unittest.TestCase):
    """ Testing base """

    @classmethod
    def setUpClass(cls):
        """ setUpClass """
        cls.test_instance = Base()
        """ Structure qui associe un value à un test """
        cls.id_values = {
            'test_id_none': None,
            'test_id': 12,
            'test_id_string': "string",
            'test_id_negative': -5,
            'test_id_float': 6.5,
            'test_id_is_zero': 0,
            'test_id_list': [1, 2, 3],
            'test_id_dict': {"id": 109},
            'test_id_tuple': (8,),
            'test_automatically_assigned_id': cls.test_instance
        }

    def test_automatically_assigned_id(self):
        """ Automatically assigned id """
        b1 = Base(id= 20)
        self.assertEqual(b1.id, 20)

    def test_id_none(self):
        """ id none """
        id_value = self.id_values[self._testMethodName]
        self.test_instance.id = id_value
        self.assertIsNone(self.test_instance.id)

    def test_id(self):
        """ id """
        id_value = self.id_values[self._testMethodName]
        self.test_instance.id = id_value
        self.assertEqual(self.test_instance.id, id_value)

    def test_id_string(self):
        """ id string """
        id_value = self.id_values[self._testMethodName]
        self.test_instance.id = id_value
        self.assertEqual(self.test_instance.id, id_value)

    def test_id_negative(self):
        """ id negative """
        id_value = self.id_values[self._testMethodName]
        self.test_instance.id = id_value
        self.assertEqual(self.test_instance.id, id_value)

    def test_id_float(self):
        """ id float """
        id_value = self.id_values[self._testMethodName]
        self.test_instance.id = id_value
        self.assertEqual(self.test_instance.id, id_value)

    def test_id_is_zero(self):
        """ id is zero """
        id_value = self.id_values[self._testMethodName]
        self.test_instance.id = id_value
        self.assertEqual(self.test_instance.id, id_value)

    def test_id_list(self):
        """ id is a list """
        id_value = self.id_values[self._testMethodName]
        self.test_instance.id = id_value
        self.assertEqual(self.test_instance.id, id_value)

    def test_id_dict(self):
        id_value = self.id_values[self._testMethodName]
        self.test_instance.id = id_value
        self.assertEqual(self.test_instance.id, id_value)

    def test_id_tuple(self):
        id_value = self.id_values[self._testMethodName]
        self.test_instance.id = id_value
        self.assertEqual(self.test_instance.id, id_value)

if __name__ == '__main__':
    unittest.main()
