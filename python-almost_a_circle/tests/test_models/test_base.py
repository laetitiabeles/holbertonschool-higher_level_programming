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

    def test_no_instance_creation(self):
        self.test_instance = Base()
        test_instance2 = Base()
        self.assertEqual(self.test_instance.id, test_instance2.id - 1)


if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()