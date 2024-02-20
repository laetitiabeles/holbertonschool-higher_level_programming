#!/usr/bin/python3

import unittest
from models.base import Base

""" Create a test class for the Base class """


class testBase(unittest.TestCase):
    """ Testing base """

    def test_no_id(self):
        """ no id """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id(self):
        """ id """
        b2 = Base(12)
        self.assertEqual(b2.id, 12)

    def test_id_string(self):
        """ id string """
        b3 = Base("string")
        self.assertEqual(b3.id, "string")

    def test_id_negative(self):
        """ id negative """
        b4 = Base(-5)
        self.assertEqual(b4.id, -5)

    def test_id_float(self):
        """ id float """
        b5 = Base(5.5)
        self.assertEqual(b5.id, 5.5)

    def test_id_is_zero(self):
        """ id is zero """
        b6 = Base(0)
        self.assertEqual(b6.id, 0)

if __name__ == '__main__':
    unittest.main()
