#!/usr/bin/python3
""" Unittest for Base class """

import unittest
import os
import json


from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """ Testing instantiation of Base class """

    def test_no_instance_creation(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_instance_creation_with_id(self):
        base1 = Base(10)
        self.assertEqual(base1.id, 10)

    def test_more_creation(self):
        base1 = Base(11)
        base2 = Base(42)
        base3 = Base(1337)
        self.assertEqual(base1.id, 11)
        self.assertEqual(base2.id, 42)
        self.assertEqual(base3.id, 1337)

    def test_None_id(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_negative_id(self):
        self.assertEqual(-5, Base(-5).id)

    def test_float_id(self):
        self.assertEqual(3.14, Base(3.14).id)

    def test_zero_id(self):
        self.assertEqual(0, Base(0).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)


if __name__ == '__main__':
    unittest.main()